Pyflix
======

Command line tool to simultaneously watch and download a torrent with seek functionality.

torrent-dl -d ~/Downloads/ [ copy paste magnet link here ( Use quotes if neccessary ) ]

It will automatically launch vlc to play once it has downloaded 3.5% of the torrent.

Inspired by youtube-dl. Pull requests are welcome.

Requires .deb and pypi packaging


Installation on Ubuntu
-----------------------
sudo apt-get install libtorrent-rasterbar8 python-libtorrent vlc

pip install -r requirements.txt


Installation on Mac OS
----------------------

brew update

brew install caskroom/cask/brew-cask

brew cask install vlc

brew install boost --build-from-source --with-python --universal

brew install libtorrent-rasterbar --enable-python-binding --with-python --with-boost-python=mt

sudo ln -s /usr/local/lib/python2.7/site-packages/libtorrent.so /Library/Python/2.7/site-packages/.

sudo ln -s /usr/local/lib/python2.7/site-packages/python_libtorrent-1.0.3-py2.7.egg-info /Library/Python/2.7/site-packages/.


pip install -r requirements.txt


Usage
-----
pyflix [-h] [--serve] [--port PORT] [--download DOWNLOAD] [--verbose] [--player PLAYER] magnet


positional arguments:

  magnet                The magnet link to download


optional arguments:

  -h, --help            show this help message and exit

  --serve               Do not run VLC

  --port PORT, -p PORT  The port where the stream will be served

  --download DOWNLOAD, -d DOWNLOAD The path where the torrent will be downloaded

  --verbose             Show _all_ the logs

  --player PLAYER       Only _vlc_ for now


