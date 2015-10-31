#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ---
# Copyright (C) 2015 - Filipe de O. Saraiva <mail@filipesaraiva.info>
#

from twx.botapi import TelegramBot
import requests

# function to create random rooms in the conferences website
# for the moment it is using the appear.in API to create
# funny names for the rooms
def createRoom():
    roomNameJson = requests.get('https://api.appear.in/random-room-name')
    roomName = roomNameJson.json()['roomName']
    roomAddress = conferencesSite + roomName
    return roomAddress

# load config.py
exec(open('./config.py').read())

# bot configuration
bot = TelegramBot(botToken)
bot.update_bot_info().wait()

# website address for creation of video calls
conferencesSite = 'https://appear.in'
