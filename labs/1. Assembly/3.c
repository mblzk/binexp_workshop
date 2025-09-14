//gcc -g -O0 -fno-omit-frame-pointer -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 3.c -o 3.out
#include <stdio.h>

typedef struct human {
    char name[16];
    int age;
    char description[64];
} Human;

void describe_human(Human human) {
    printf("You are now looking at the: %s of age %d\n", human.name, human.age);
    printf("He seems to be %s\n",human.description);
}
int main(){
    int test = 0x6969;
    Human human = { .name="IzaaK AAAA", .age=32, .description="A perfectly made human, capable of eating and even sleeping"};
    char str[] = "kajkoikokosz";
    describe_human(human);
    printf("Testing %d of %s", test, str);
    return 0;
}
