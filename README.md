Pyflix
======

Command line tool to watch torrents


Installation
------------
sudo apt-get install libtorrent-rasterbar8

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
  --download DOWNLOAD, -d DOWNLOAD
                        The path where the torrent will be downloaded
  --verbose             Show _all_ the logs
  --player PLAYER       Only vlc for now

