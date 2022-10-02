#include "05_08-horserace.h"

int main()
{
	struct pony racehorse[RECORDS];
	int winner;

	initialize(racehorse);
	run_race(racehorse);
	winner = show_results(racehorse);

	printf("The winner is %s!\n",racehorse[winner].name);

	return(0);
}
