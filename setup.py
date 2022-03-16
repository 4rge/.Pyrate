#!/usr/bin/env python
from setuptools import setup

setup_info = dict(
    name='.PyrateBrowser',
    version='1.0',
    author='ZZZlax',
    author_email='theoriginalashketchum@protonmail.com',
    url='https://github.com/ZZZlax/.PyrateBrowser',
    download_url='https://github.com/ZZZlax/.PyrateBrowser',
    description='.PyrateBrowser',
    keywords = ["Browser"],
    long_description='Yarrrrrrrrrrrrrrrrrrrrrrrrrrrr!!!!!!!!!!!!!!!!!!!!!!!!!!!111',
    classifiers=[
        "Topic :: Utilities",
        'Development Status :: Production/Stable',
        'Environment :: X11 Applications',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=['requests', 'qrcode', 'urllib3', 'bs4', 'youtube_dl', 'wikipedia'], requires=['requests', 'qrcode', 'urllib3', 'bs4', 'youtube_dl', 'wikipedia']
)

setup(**setup_info)
