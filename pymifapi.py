import json
import os
from typing import Union

import requests

__version__ = "0.1.1"


def getfile(dl_uri: str, outfile: os.PathLike) -> int:
    """
    Get file from URL and save it to file (basically wget)
    :param dl_uri: Download URL
    :param outfile: Filesystem path
    :return: HTTP request status code
    """
    print("Saving from", dl_uri, "to", outfile)
    try:
        r = requests.get(dl_uri)
        with open(outfile, 'wb') as f:
            f.write(r.content)
            return r.status_code
    except Exception as e:
        print("Exception:", e)


def sendfile(infile: os.PathLike, asyncronous=False, filetype='jxl', codec='aom') -> Union[str, None]:
    """
    Send file to mifapi for conversion
    :param infile: Path to file
    :param asyncronous: If yes, return immediately, convert later
    :param filetype: Resulting file. Can be jxl or avif.
    :param codec: AVIF encoder. Can be aom, svt, rav1e
    :return: URL to download resulting file
    """
    if filetype not in ['jxl', 'avif']:
        print("Error in filetype parameter")
        return
    if codec not in ['aom', 'svt', 'rav1e']:
        print("Error in filetype parameter")
        return
    if asyncronous:
        asyncronous = 'async'
    else:
        asyncronous = ''
    api_url = f'https://jxl.photos/api/v1/{filetype}/encode{asyncronous}?codec={codec}/'
    try:
        files = {'file': open(infile, 'rb')}
        getdata = requests.post(api_url, files=files)
        if getdata.status_code == 200:
            return json.loads(getdata.text)["dl_uri"]
        else:
            print("Error:", json.loads(getdata.text)["detail"])
    except Exception as e:
        print("Exception:", e)
