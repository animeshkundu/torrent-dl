import argparse
import logging
import sys

from Pyflix.torrent import DownloadManager
from Pyflix.utils.logger import log_set_up
from libtorrent import version as libtorrent_version

log = logging.getLogger('pyflix.main')

def main():
    parser = argparse.ArgumentParser(description="Command line tool to watch torrents")
    parser.add_argument("magnet", help="The magnet link to download")

    parser.add_argument("--serve", action="store_true", help="Do not run VLC")
    parser.add_argument("--port", "-p", default="1149", help="The port where the stream will be served")
    parser.add_argument("--download", "-d", default=None, help="The path where the torrent will be downloaded")
    parser.add_argument("--verbose", action="store_true", default=None, help="Show _all_ the logs")
    parser.add_argument("--player", default='vlc', help="Only vlc for now")

    args = parser.parse_args()

    log_set_up(args.verbose)
    log.info("Starting Pyflix")
    log.debug("Running Pyflix %s on %r", sys.version_info, sys.platform)
    log.debug("Libtorrent version: %s", libtorrent_version)

    manager = DownloadManager(args.magnet, port=args.port, serve=args.serve, player=args.player, save_path=args.download)
    manager.start()

if __name__ == '__main__':
    main()
