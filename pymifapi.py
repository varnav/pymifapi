import requests
import json

__version__ = "0.1.0"


def getfile(dl_uri, outfile):
    print("Saving from", dl_uri, "to", outfile)
    try:
        r = requests.get(dl_uri)
        with open(outfile, 'wb') as f:
            f.write(r.content)
    except Exception as e:
        print("Exception:", e)


def sendfile(infile, asyncronous=False, filetype='jxl', codec='aom'):
    if filetype not in ['jxl', 'avif']:
        print("Error in filetype parameter")
        exit(1)
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
