//gcc -g -O0 -fno-omit-frame-pointer -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 -fno-stack-protector -z execstack -no-pie 2.c -o 2.out
#include <stdio.h>
#include <stdlib.h>

void hello_routine(){
    char name[32] = {};
    char surname[32] = {};
    char country[32] = {};
    printf("Hello, what's your name?\n");
    fgets(name, 0x32, stdin);
    printf("And your surname?\n");
    fgets(surname, 32, stdin);
    printf("How about your country?\n");
    fgets(country, 32, stdin);
    printf("Cool to meet you %s", name);
}

int main(){
    hello_routine();
    return 0;
}
