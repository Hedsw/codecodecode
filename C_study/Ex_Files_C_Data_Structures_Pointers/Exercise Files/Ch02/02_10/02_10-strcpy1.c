#include <stdio.h>
#include <string.h>

int main()
{
	char original[] = "Am I the original?";
	char duplicate[32];

	printf("Here is the original string: %s\n",original);
	strcpy(duplicate,original);
	printf("Here is the duplicate: %s\n",duplicate);

	return(0);
}
