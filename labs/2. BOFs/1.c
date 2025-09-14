//gcc -g -O0 -fno-omit-frame-pointer -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 -fno-stack-protector -z execstack -std=c99 -no-pie 1.c -o 1.out
#include <stdio.h>
#include <stdlib.h>

void win(){
    system("/bin/bash");
    exit(0);
}


void hello_routine(){
    char str[128] = {};
    printf("Hello, what's your name?\n");
    gets(str);
    printf("Cool to meet you %s", str);
}

int main(){
    hello_routine();
    return 0;
}
