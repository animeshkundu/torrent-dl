torrent-dl
==========

Popcorn Time was/is a really cool solution to play torrents directly while its being downloaded in the background, if you can get one of the installers to work. I really love Peerflix, it just works. 

This is a port of my beloved peerflix to python. I really need to get it to packaging it, so that I can just apt-get it :)

You can simultaneously watch and download a torrent at the same time. It also supports random and incremental seek functionality of the media player.

All you have to do is `torrent-dl [magnet link]`

It will automatically start playing once it has downloaded x% of the file.

Inspired by youtube-dl. Pull requests are welcome.

Requires .deb and pypi packaging


Installation on Ubuntu
-----------------------
sudo apt-get install libtorrent-rasterbar8 python-libtorrent

pip install -r requirements.txt


Installation on Mac OS
----------------------

brew update

brew install caskroom/cask/brew-cask

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


