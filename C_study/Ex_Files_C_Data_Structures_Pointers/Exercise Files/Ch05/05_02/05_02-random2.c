#include <stdio.h>
#include <stdlib.h>

int main()
{
	int x,r;

	for(x=0;x<100;x++)
	{
		r = rand() % 100;
		printf("%4d",r);
	}
	putchar('\n');

	return(0);
}
