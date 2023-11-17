#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LENGTH 0x80

void win(void);
void tomfoolery(void);

int main(void) {
    setvbuf(stdout, NULL, _IONBF, 0);
    tomfoolery();
}

void win(void) {
    FILE *file = fopen("flag.txt", "r");

    if (file == NULL) {
        printf("could not open the flag file\n");
        exit(1);
    }

    char *flag = NULL;
    size_t len = 0;
    getline(&flag, &len, file);

    for (int i = 0; i < len; i++) {
        putchar(flag[i]);
    }

    free(flag);
    exit(0);
}

void tomfoolery(void) {
    char name[LENGTH];

    printf("you will never find a way to leak the flag!!!!!\n");
    printf("you know what, ill even give you the pointer for main, free of charge: %p\n", main);
    printf("so what's your name? ");

    fgets(name, LENGTH, stdin);
    name[strcspn(name, "\n")] = 0;

    printf(name);
    printf(" huh?\n");
    printf("i don't think that's your real name\n");
}
