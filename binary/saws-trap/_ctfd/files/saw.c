#include <stdio.h>
#include <stdlib.h>

void init() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

int main() {
	init();

	char buf[0x40];
	puts("Nyahahahaha its me SAW from hit movie SAW I have metaphorically trapped you within this binary");
	puts("You must escape, or you'll have to bear the weight of the accursed 'skill issue'");

	gets(buf);
}
