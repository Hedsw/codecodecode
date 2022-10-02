#include <stdio.h>

int main()
{
	char text[10];

	printf("Type something: ");
	scanf("%9s",text);
	printf("You typed: %s\n",text);

	return(0);
}

