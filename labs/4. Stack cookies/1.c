//gcc -g -O0 -fno-omit-frame-pointer -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=0 -z execstack -no-pie -fstack-protector -std=c99 1.c -o 1.out
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct person {
    char name[8];
    char surname[8];
} Person;

void add_data(Person* people){
    char cmd[4] = {};
    char buffer[12] = {};
    int len = 0;
    printf("Enter your ID, citizen [0-8]: ");
    fgets(cmd, 4, stdin);
    cmd[strcspn(cmd, "\r\n")] = 0;

    printf("State your name: \n");
    fgets(buffer, 12, stdin);
    len = strcspn(buffer, "\r\n");
    memcpy(people[atoi(cmd)].name, buffer, len);
    
    printf("State your surname: \n");
    fgets(buffer, 12, stdin);
    len = strcspn(buffer, "\r\n");
    memcpy(people[atoi(cmd)].surname, buffer, len);
}

void verify_data(Person* people){
    char cmd[4];
    printf("Enter your ID, citizen [0-8]: ");
    fgets(cmd, 4, stdin);
    cmd[strcspn(cmd, "\r\n")] = 0;
     
    printf("Our current records state: \n");
    printf("NAME: %s\n", people[atoi(cmd)].name);
    printf("SURNAME: %s\n", people[atoi(cmd)].surname);
}

void census(){
    Person people[8] = {};
    char cmd[64] = {};
    printf("Welcome to the great census!\n");
    while (1){
        printf("Add yourself to the list, citizen: \n");
        printf("1 - Add your data\n");
        printf("2 - Verify your data\n");
        printf("3 - Go where all good citizens go (leave)\n");
        gets(cmd);
        if (strcmp(cmd, "1") == 0) 
        {
            add_data(people);
        } 
        else if (strcmp(cmd, "2") == 0)
        {
            verify_data(people);
        }
        else if (strcmp(cmd, "3") == 0)
        {
            printf("Thank you for your service, citizen.\n");
            return;

        }
        else
        {
            return;
        }

        memset(cmd, 0, 64); 

    }

}

int main(){
    census();
    printf("Unsurprisingly, you do what all good citizens do - die.");
    return 0;
}
