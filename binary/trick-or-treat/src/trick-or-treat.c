#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>



bool get_candies(int num);
int get_int();
void print_flag();
void init();

int main() {
	init();

	puts("How many candies would you like to take?");
	int num_candies = get_int();

	srand(num_candies);

	if (get_candies(num_candies)) {
		print_flag();
	}
}

bool get_candies(int num) {
	char target = 0;
	char buf[rand() % 0x200];

	if (num > 1)
		puts("One day you will have to answer for your greed, and when that days comes they may not be as merciful as I.");
	puts("Wonderful, which ones would you like :)");

	gets(buf);

	return target;
}

int get_int() {
	char buf[0x20];

	fgets(buf, 0x20, stdin);

	return atoi(buf);
}

void print_flag() {
	char buf[0x40];

	FILE * f = fopen("flag.txt", "r");
	fread(buf, 1, 0x40, f);
	fwrite(buf, 1, 0x40, stdout);
}

void init() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}
