import logging

from blessings import Terminal
from os import system
from time import sleep

from Pyflix.utils.helpers import get_interface

log = logging.getLogger('pyflix.utils.output')

class Output(object):
    def __init__(self, stream_url, parent):
        self.stream_url = stream_url
        self.parent = parent

    def run(self):
        player_command = self._player()
        command = "%s %s" % (player_command, "")
        log.debug("VLC command: %s" % command)
        system(command)

    def _player(self):
        return ""


class VLCOutput(Output):
    def _player(self):
        command = "vlc %s -q" % self.stream_url
        return command
