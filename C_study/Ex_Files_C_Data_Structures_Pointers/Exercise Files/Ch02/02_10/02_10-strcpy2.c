#include <stdio.h>
#include <string.h>

int main()
{
	char original[] = "Am I the original?";
	char duplicate[] = "This is the duplicate";

	printf("Here is the original string: %s\n",original);
	printf("Here is the duplicate: %s\n",duplicate);
	strcpy(duplicate,original);
	printf("And now this is the duplicate: %s\n",duplicate);

	return(0);
}
