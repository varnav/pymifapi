from PIL import Image

from pymifapi import sendfile, getfile

# Generate test images
img = Image.new('RGB', (128, 128), color='white')
img.save('/tmp/testimage1.jpg')
img.save('/tmp/testimage2.jpg')


def test_sendfile():
    dl_uri = sendfile('/tmp/testimage1.jpg')
    assert type(dl_uri) == str


def test_getfile():
    dl_uri = sendfile('/tmp/testimage2.jpg')
    savepath = '/tmp/' + dl_uri.rsplit('/', 1)[1]
    getfile(dl_uri, savepath)
    assert savepath == "/tmp/testimage2.jxl"
