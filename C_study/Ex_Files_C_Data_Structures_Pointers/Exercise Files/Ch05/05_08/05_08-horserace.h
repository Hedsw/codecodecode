#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define RECORDS 5
#define NAME_SIZE 20
#define RACE_LENGTH 9

struct pony {
	char *name;
	int distance[RACE_LENGTH];
	int first[RACE_LENGTH];
};

/* must include prototypes from other modules */
void initialize(struct pony horse[]);
void run_race(struct pony horse[]);
int show_results(struct pony horse[]);

