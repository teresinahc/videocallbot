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

from datetime import datetime as time
from twx.botapi import TelegramBot, Update, Chat, ReplyKeyboardMarkup, User
import json
import os.path
import requests

# Main function to creation of the room, the message, and send
# the reply to the user.
def handle(update):
    chat = extractChat(update)

    if update.message.text == '/start':
        keyboard = createKeyboard()
        bot.send_message(chat, '', reply_markup=keyboard).wait()

    if update.message.text == 'Create video call room':
        global numRooms
        message = createMessage(update)
        bot.send_message(chat, message).wait()
        numRooms = numRooms + 1
        writeLog(numRooms)

# Extract chat identifier
def extractChat(update):
    return update.message.chat.id

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
    senderFirstName = update.message.sender.first_name
    senderLastName = update.message.sender.last_name
    senderName = str(senderFirstName) + ' ' + str(senderLastName)
    return senderName

# Function to create random room in the conferences website.
# For the moment it is using the appear.in API to create
# funny names for the rooms.
def createRoom():
    roomNameJson = requests.get('https://api.appear.in/random-room-name')
    roomName = roomNameJson.json()['roomName']
    roomAddress = conferencesSite + roomName
    return roomAddress

# How many rooms were created? This function will write this
# information in a file for each 500 rooms created.
def writeLog(numRooms):
    if rooms % 500 == 0:
        file = open('numRooms.log', 'a')
        file.write(time.now().strftime('%Y-%m-%d') + ' ' + str(numRooms) + '\n')
        file.close()

# Read numRooms.log and initialize numRooms with the previous number
# of rooms created. If there is not numRooms.log file, initialize the
# number of rooms with 0.
def readNumRooms():
    if os.path.exists('numRooms.log'):
        file = open('numRooms.log', 'r')
        line = file.readlines()[-1]
        rooms = int(line.split(' ')[-1])
        file.close()
    else:
        rooms = 0
    return rooms

# Load config.py
exec(open('./config.py').read())

# Bot configuration
bot = TelegramBot(botToken)
bot.update_bot_info().wait()

# Website address for creation of video calls
conferencesSite = 'https://appear.in'

# Count the number of rooms created
numRooms = readNumRooms()

# Updates received
offset = 0

# The bot will get updates
while True:
    updates = bot.get_updates(offset=offset).wait()
    try:
        offset = updates[-1].update_id + 1
    except (IndexError):
        pass
    for update in updates:
        handle(update)
