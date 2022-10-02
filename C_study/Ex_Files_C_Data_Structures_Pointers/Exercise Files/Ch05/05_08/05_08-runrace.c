#include "05_08-horserace.h"

/* This module calculates a random distance for all the horses. This
   value is multiplied by a small amount for each horse. The results
   is saved in each horse's structure to determine how far they've
   advanced through the race.
   The lead horse is tracked by the laps[] array. */
void run_race(struct pony horse[])
{
	int x,furlong,length,max;
	float speed;

	/* this loop repeats for each furlong in the race */
		/* Start the race length calculations at furlong 1;
		   furlong 0 is the start of the race, where each horse
		   has 0, as preset when the horse structure is initialized */
	furlong = 1;
	while(furlong<RACE_LENGTH)
	{
		/* calculate the minimum length the horses run */
		length = rand() % 660 + 500;
		/* set the distance for each horse */
		for(x=0;x<RECORDS;x++)
		{
			/* randomize each horse's performance */
			speed = (float)(rand() % 30 + 60)/100.0;
			/* calculate how far the horse ran */
			horse[x].distance[furlong] = speed*length + horse[x].distance[furlong-1];
			/* flag the horse in first */
				/* This calculation is a "max" puzzle: Store the first
				   distance value, then if any subsequent value is higher,
				   replace the value */
			if( x == 0 )
			{
				max = horse[x].distance[furlong];	/* store the first value */
			}
			else
			{
				if( horse[x].distance[furlong] > max )	/* when a value is higher, replace it */
				{
					max = horse[x].distance[furlong];
				}
			}
		}
		/* determine which horse is the leader */
		for(x=0;x<RECORDS;x++)
			if( horse[x].distance[furlong] == max )
				horse[x].first[furlong] = 1;
			else
				horse[x].first[furlong] = 0;
		/* Next lap! */
		furlong++;
	}

}

