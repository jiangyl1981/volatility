# Volatility
# Copyright (C) 2008 Volatile Systems
# Copyright (c) 2008 Brendan Dolan-Gavitt <bdolangavitt@wesleyan.edu>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details. 
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA 
#

"""
@author:       AAron Walters and Brendan Dolan-Gavitt
@license:      GNU General Public License 2.0 or later
@contact:      awalters@volatilesystems.com,bdolangavitt@wesleyan.edu
@organization: Volatile Systems
"""

#pylint: disable-msg=C0111

from forensics.object2 import Profile
from forensics.win32.regtypes import regtypes
from forensics.win32.domcachedump import dump_memory_hashes
import forensics.commands
from vutils import load_and_identify_image

class cachedump(forensics.commands.command):
    "Dump (decrypted) domain hashes from the registry"
    # Declare meta information associated with this plugin
    
    meta_info = forensics.commands.command.meta_info 
    meta_info['author'] = 'Brendan Dolan-Gavitt'
    meta_info['copyright'] = 'Copyright (c) 2007,2008 Brendan Dolan-Gavitt'
    meta_info['contact'] = 'bdolangavitt@wesleyan.edu'
    meta_info['license'] = 'GNU General Public License 2.0 or later'
    meta_info['url'] = 'http://moyix.blogspot.com/'
    meta_info['os'] = 'WIN_32_XP_SP2'
    meta_info['version'] = '1.0'

    def parser(self):
        forensics.commands.command.parser(self)
        self.op.add_option('-y', '--sys-offset', help='SYSTEM hive offset (virtual)',
            action='store', type='int', dest='syshive')
        self.op.add_option('-s', '--sec-offset', help='SECURITY hive offset (virtual)',
            action='store', type='int', dest='sechive')

    def execute(self):
        (addr_space, _symtab, types) = load_and_identify_image(self.op, self.opts)
        
        # In general it's not recommended to update the global types on the fly,
        # but I'm special and I know what I'm doing ;)
        types.update(regtypes)

        if not self.opts.syshive or not self.opts.sechive:
            self.op.error("Both SYSTEM and SECURITY offsets must be provided")
        
        dump_memory_hashes(addr_space, types, self.opts.syshive, self.opts.sechive, Profile())

