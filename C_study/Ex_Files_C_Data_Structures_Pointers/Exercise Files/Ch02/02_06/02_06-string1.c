#include <stdio.h>

int main()
{
	char string[] = "I'm such a handsome program!\n";
	int a;

	a = 0;
	while( string[a] != '\0' )
	{
		putchar( string[a] );
		a++;
	}

	return(0);
}

