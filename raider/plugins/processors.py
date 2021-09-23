# Copyright (C) 2021 DigeeX
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Plugins used to process data.
"""

import urllib

from raider.plugins.common import Plugin, Processor


class Urlencode(Processor):
    """URL Encode the plugin."""

    def __init__(self, parent_plugin: Plugin) -> None:
        """Initializes the Urlencode plugin."""
        super().__init__(
            name=parent_plugin.name + "_urlencoded", function=self.urlencode
        )
        self.plugins = [parent_plugin]

    def urlencode(self) -> str:
        """URL encodes a plugin's value."""

        original = self.plugins[0].value
        encoded = urllib.parse.quote(original)
        return encoded


class Urldecode(Processor):
    """URL Decode the plugin."""

    def __init__(self, parent_plugin: Plugin) -> None:
        """Initializes the Urldecode plugin."""
        super().__init__(
            name=parent_plugin.name + "_urldecoded", function=self.urldecode
        )
        self.plugins = [parent_plugin]

    def urldecode(self) -> str:
        """URL decodes a plugin's value."""

        original = self.plugins[0].value
        decoded = urllib.parse.unquote(original)
        return decoded
