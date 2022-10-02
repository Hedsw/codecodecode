#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define COUNT 51
#define BALLS 6

int main()
{
	int lottoball[COUNT];
	int x,draw,b;

	/* seed the randomizer */
	srand( (unsigned)time(NULL) );
	/* initialize the array */
	for(x=0;x<COUNT;x++)
		lottoball[x] = 0;

	/* pull the lotto balls */
	draw = 0;
	while(draw<BALLS)
	{
		/* generate a random number */
		b = rand() % COUNT;
		/* confirm that it hasn't yet been drawn */
		if( lottoball[b] == 0 )
		{
			/* mark the ball as drawn */
			lottoball[b] = 1;
			/* update the winners array */
			draw++;
		}
		/* if the number has been drawn, the loop repeats */
	}

	/* show the winners, which are naturally in ascending order */
	puts("Winning Lotto Numbers:");
	for(x=0;x<COUNT;x++)
	{
		if( lottoball[x] == 1 )
		{
			/* add one to the output to account for element zero */
			printf("%3d",x+1);	
		}
	}
	putchar('\n');

	return(0);
}

