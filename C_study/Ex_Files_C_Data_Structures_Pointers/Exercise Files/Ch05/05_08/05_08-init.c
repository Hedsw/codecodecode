#include "05_08-horserace.h"

/* I generally separate out all parts of the project
   that must be setup and configured into an initialize()
   function */
void initialize(struct pony horse[])
{
	/* this type of string declaration works because only the
	   address is copied into the pony structure */
	char *horsename[] = {
		"Secretariat",
		"Seattle Slew",
		"Affirmed",
		"American Pharoah",
		"Justify"
	};
	int x;

	/* seed the randomizer */
	srand( (unsigned)time(NULL) );
	
	/* build the structures */
	for(x=0;x<RECORDS;x++)
	{
		horse[x].name = horsename[x];
		horse[x].distance[0] = 0;
		horse[x].first[0] = 0;
	}

	/* display title */
	puts("Horse Race Simulation");
	
	/* display table header */
	printf("%-17s %5s","Name","Start");
	for(x=1;x<RACE_LENGTH-1;x++)
		printf(" %4d ",x);
	printf(" Finish\n");
}

