//gcc -g -O0 -fno-omit-frame-pointer -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 -fno-stack-protector -z execstack -no-pie 1.c -o 1.out
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void hello_routine(){
    char str[128] = {};
    char tmp[256] = {};
    printf("Hello, what's your name?\n");
    fgets(tmp, 256, stdin);
    memcpy(str, tmp, strlen(tmp));
    memset(tmp, 0, 256);
    printf("Cool to meet you %s", str);
}

int main(){
    hello_routine();
    return 0;
}
