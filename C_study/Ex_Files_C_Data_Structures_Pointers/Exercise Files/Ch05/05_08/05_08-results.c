#include "05_08-horserace.h"


/* This code outputs the table of results, listing each horse's
   distance value. The lead horse for each furlong is flagged */
int show_results(struct pony horse[])
{
	int x,furlong,lead;

	for(x=0;x<RECORDS;x++)
	{
		printf("%-18s",horse[x].name);
		for(furlong=0;furlong<RACE_LENGTH;furlong++)
		{
			printf(" %4d",horse[x].distance[furlong]);
			/* flag the winning horse for each furlong after start */
			if( furlong > 0 )
			{
				if( horse[x].first[furlong] )
				{
					if( furlong == RACE_LENGTH-1 )
					{
						lead = x;
					}
					putchar('*');
				}
				else
				{
					putchar(' ');
				}
			}
		}
		putchar('\n');
	}

	return(lead);
}
