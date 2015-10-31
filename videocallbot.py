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

from bottle import route, run, request
from twx.botapi import TelegramBot
import requests

# Main function to creation of the room, the message, and send
# the reply to the user.
@route('/', method='POST')
def action():
    updateJson = request.body.read().decode('utf-8')
    update = json.loads(updateJson)

    chat = extractChat(update)
    roomAddress = createRoom()

    bot.send_message(chat, roomAddress).wait()

# Extract chat identifier
def extractChat(update):
    return update['message']['chat']['id']

# Function to create random room in the conferences website.
# For the moment it is using the appear.in API to create
# funny names for the rooms.
def createRoom():
    roomNameJson = requests.get('https://api.appear.in/random-room-name')
    roomName = roomNameJson.json()['roomName']
    roomAddress = conferencesSite + roomName
    return roomAddress

# Load config.py
exec(open('./config.py').read())

# Bot configuration
bot = TelegramBot(botToken)
bot.update_bot_info().wait()

# Website address for creation of video calls
conferencesSite = 'https://appear.in'

# The bot will listen for requests.
run(host=webhookAddress, port=webhookPort)
