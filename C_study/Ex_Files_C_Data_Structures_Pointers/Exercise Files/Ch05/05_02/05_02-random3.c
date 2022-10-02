#include <stdio.h>
#include <stdlib.h>

int main()
{
	int x,r;
	unsigned s;

	printf("Enter the seed: ");
	scanf("%u",&s);
	srand(s);

	for(x=0;x<100;x++)
	{
		r = rand() % 100 + 1;
		printf("%4d",r);
	}
	putchar('\n');

	return(0);
}
