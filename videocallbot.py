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
from twx.botapi import TelegramBot, ReplyKeyboardMarkup
import json
import requests

# Main function to creation of the room, the message, and send
# the reply to the user.
@route('/', method='POST')
def handle():
    updateJson = request.body.read().decode('utf-8')
    update = json.loads(updateJson)

    chat = extractChat(update)

    if update['message']['text'] == '/start':
        keyboard = createKeyboard()
        bot.send_message(chat, '', reply_markup=keyboard).wait()

    if update['message']['text'] == 'Create video call room':
        message = createMessage(update)
        bot.send_message(chat, message).wait()

# Extract chat identifier
def extractChat(update):
    return update['message']['chat']['id']

# Create custom application keyboard
def createKeyboard():
    keyboard = [['Create video call room']]
    return ReplyKeyboardMarkup.create(keyboard)

# Create the message to be sent. This function will be accountable for
# create all elements of a message.
def createMessage(update):
    senderName = extractSenderName(update)
    roomAddress = createRoom()
    return  'Hi, ' + senderName + 'wants to make a video call with you!\n'\
    + 'Click at the address ' + roomAddress + '\n\n'\
    + '@VideoCallBot, bringing video calls to Telegram!'

# Extract sender name from the update message
def extractSenderName(update):
    senderFirstName = update['message']['from']['first_name']
    senderLastName = update['message']['from']['last_name']
    senderName = senderFirstName + ' ' + senderLastName
    return senderName

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
