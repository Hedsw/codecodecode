#include <stdio.h>
#include <string.h>

int main()
{
	char first[16] = "George";
	char last[16] = "Washington";
	char full[32];

	strcpy(full,first);
	/* Append a string with a single space */
	strcat(full," ");	/* must be a string, not a single char */
	strcat(full,last);

	printf("Pleased to meet you, %s\n",full);

	return(0);
}
