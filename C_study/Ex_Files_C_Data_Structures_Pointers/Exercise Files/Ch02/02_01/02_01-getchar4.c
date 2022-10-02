#include <stdio.h>

int main()
{
	int ch1,ch2;

	printf("Type two characters: ");
	ch1 = getc(stdin);
	ch2 = getc(stdin);
	printf("Characters '%c' and '%c' received.\n",ch1,ch2);

	return(0);
}
