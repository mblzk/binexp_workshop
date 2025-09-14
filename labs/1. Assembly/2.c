//gcc -g -O0 -fno-omit-frame-pointer -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 2.c -o 2.out
#include <stdio.h>


void hello_val(int val){
    printf("Hello from function with value: %d\n", val);
}

void hello_poi(char str[]){
    printf("Hello from function with pointer!\n");
    printf("Pointer value is: 0x%x\n",str);
    printf("And it points to: %s\n", str);
}

int main(){
    int test = 0x6969;
    char str[] = "kajkoikokosz";
    hello_val(test);
    hello_poi(str);
    return 0;
}
