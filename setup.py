import os
import shutil

import setuptools

import pymifapi

if not os.path.exists('pymifapi'):
    os.mkdir('pymifapi')
shutil.copyfile('pymifapi.py', 'pymifapi/__init__.py')

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
    'requests>=2.25.1'
]

setuptools.setup(
    name="pymifapi",
    version=pymifapi.__version__,
    author="Evgeny Varnavskiy",
    author_email="varnavruz@gmail.com",
    description="Modern Image Formats (JPEG XL and AVIF) Web API client library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/varnav/pymifapi",
    keywords=["jpeg", "jpeg-xl", "avif", "webapi", "transcoder"],
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Utilities",
        "Topic :: Multimedia :: Graphics",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires='>=3.7',
    entry_points={
        "console_scripts": [
            "pymifapi = pymifapi:main",
        ]
    }
)
