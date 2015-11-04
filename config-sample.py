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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ---
# Copyright (C) 2015 - Filipe de O. Saraiva <mail@filipesaraiva.info>
#

from twx.botapi import InputFile, InputFileInfo

# Bot token provide by @BotFather
botToken = ''

# Public certificate for the webhook communication
certName = ''
certFile = open(certName, 'rb')
certInfo = InputFileInfo(certName, certFile, 'text/plain')
cert = InputFile(certificateFile, certInfo)

# Port to listen the requests - the value must to be one
# of the follow integer numbers: 443, 80, 88, or 8443
webhookPort = 

# Web address to listen the requests - the string operations
# below shows the example of URL presented by Telegram Bot API
webhookAddress = '' + botToken
