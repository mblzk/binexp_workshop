#!/usr/bin/env python3

from pwn import *
import os

# -----------------------
# Config
# -----------------------
BIN_PATH = "./lololol"  # change me
context.binary = ELF(BIN_PATH, checksec=True)

context.log_level = "info"
context.terminal = ["tmux", "splitw", "-h"]

gdbscript = """
# adjust breakpoints for your binary:
break *main
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
p.interactive()
