#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	struct person {
		char *name;
		int age;
	} *you;
	char buffer[32];

	/* allocate storage for the structure */
	you = (struct person *)malloc( sizeof(struct person) * 1 );
	if( you== NULL)
	{
		puts("Unable to allocate storage");
		exit(1);
	}

	printf("Enter your name: ");
	fgets(buffer,32,stdin);
	/* allocate storage */
	you->name = (char *)malloc( sizeof(buffer) );
	if( you->name == NULL)
	{
		puts("Unable to allocate storage");
		exit(1);
	}
	/* copy the buffer */
	strcpy(you->name,buffer);
	/* get your age */
	printf("Enter your age: ");
	scanf("%d",&you->age);

	printf("You are %s",you->name);
	printf("You are %d years old\n",you->age);

	return(0);
}

