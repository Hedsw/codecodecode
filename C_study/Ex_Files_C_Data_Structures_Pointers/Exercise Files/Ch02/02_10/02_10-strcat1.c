#include <stdio.h>
#include <string.h>

int main()
{
	char first[16] = "George";
	char last[16] = "Washington";
	char full[32];

	strcpy(full,first);
	strcat(full,last);

	printf("Pleased to meet you, %s\n",full);

	return(0);
}
