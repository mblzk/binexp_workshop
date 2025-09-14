#!/bin/bash
gcc -g -O0 -fno-omit-frame-pointer -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 1.c -o 1.out
gcc -g -O0 -fno-omit-frame-pointer -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 2.c -o 2.out
gcc -g -O0 -fno-omit-frame-pointer -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 3.c -o 3.out

