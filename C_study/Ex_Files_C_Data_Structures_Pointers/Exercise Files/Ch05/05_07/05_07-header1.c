#include <stdlib.h>
#include <time.h>

#define MAX 100
#define SIZE 3

int main()
{
	struct data {
		int a;
		char b;
	};
	struct data stuff[SIZE];
	int x;
	
	/* seed randomizer */
	srand( (unsigned)time(NULL) );

	for(x=0;x<SIZE;x++)
	{
		stuff[x].a = rand() % MAX + 1;
		stuff[x].b = rand() % 26 + 'A';
	}

	return(0);
}

