# Sample file conversion with mifapi
# Batch processing through async API
# https://github.com/varnav/mifapi
# Evgeny Varnavskiy 2020
# MIT License

import datetime
from pymifapi import sendfile, getfile
from apscheduler.schedulers.background import BackgroundScheduler
import os
import pathlib
from typing import Iterable
import click

SUPPORTED_FORMATS = ['jpeg', 'jpg', 'png']


# Ported from: https://github.com/victordomingos/optimize-images
def search_files(dirpath: str, recursive: bool) -> Iterable[str]:
    if recursive:
        for root, dirs, files in os.walk(dirpath):
            for f in files:
                if not os.path.isfile(os.path.join(root, f)):
                    continue
                extension = os.path.splitext(f)[1][1:]
                if extension.lower() in SUPPORTED_FORMATS:
                    yield os.path.join(root, f)
    else:
        with os.scandir(dirpath) as directory:
            for f in directory:
                if not os.path.isfile(os.path.normpath(f)):
                    continue
                extension = os.path.splitext(f)[1][1:]
                if extension.lower() in SUPPORTED_FORMATS:
                    yield os.path.normpath(f)


scheduler = BackgroundScheduler(daemon=False)


@click.command()
@click.argument('directory', type=click.Path(exists=True))
@click.option('-r', '--recursive', is_flag=True, help='Recursive')
@click.option('-w', '--wait', default=5, help='Seconds to wait before file download')
def main(directory, wait, recursive=False):
    for filepath in search_files(str(directory), recursive=recursive):
        fp = pathlib.PurePath(filepath)
        newpath = fp.parent.joinpath(fp.stem + '.' + 'jxl')
        dl_uri = sendfile(fp, asyncronous=True)
        if dl_uri is not None:
            print("Scheduling download from", dl_uri)
            scheduler.add_job(getfile, 'date', args=[dl_uri, newpath], next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=wait))
    scheduler.start()


if __name__ == '__main__':
    main()
