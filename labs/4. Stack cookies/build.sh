#!/bin/sh
gcc -g -O0 -fno-omit-frame-pointer -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 -z execstack -no-pie -fstack-protector -std=c99 1.c -o 1.out
