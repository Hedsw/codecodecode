#include "05_07-header2.h"

int main()
{
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

