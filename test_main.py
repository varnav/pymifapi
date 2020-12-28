import pytest
from pymifapi import sendfile, getfile


from PIL import Image

# Generate test images
img = Image.new('RGB', (128, 128), color='white')
img.save('/tmp/testimage1.jpg')
img.save('/tmp/testimage2.jpg')
img.save('/tmp/testimage3.jpg')
img.save('/tmp/testimage4.jpg')
img.save('/tmp/testimage5.jpg')
img.save('/tmp/testimage6.jpg')
img.save('/tmp/testimage7.jpg')
img.save('/tmp/testimage8.jpg')


def test_sendfile():
    dl_uri = sendfile('/tmp/testimage8.jpg')
    assert type(dl_uri) == str