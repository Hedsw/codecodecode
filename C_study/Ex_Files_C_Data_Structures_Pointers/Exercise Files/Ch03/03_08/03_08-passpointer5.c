#include <stdio.h>

void change(char *s)
{
	*(s+1) = 'a';
}

int main()
{
	char pet[] = "cot";

	puts(pet);
	change(pet);
	puts(pet);

	return(0);
}
