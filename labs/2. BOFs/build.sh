#!/bin/sh
gcc -g -O0 -fno-omit-frame-pointer -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 -fno-stack-protector -z execstack -std=c99 -no-pie 1.c -o 1.out
gcc -g -O0 -fno-omit-frame-pointer -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 -fno-stack-protector -z execstack -no-pie 2.c -o 2.out
