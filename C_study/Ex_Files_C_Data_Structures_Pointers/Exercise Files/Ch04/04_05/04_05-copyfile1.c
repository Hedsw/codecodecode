#include <stdio.h>

int main()
{
	const char original[] = "beta.txt";
	const char duplicate[] = "betacopy.txt";
	FILE *org,*dup;
	int c;

	/* open/create the files */
	org = fopen(original,"r");
	dup = fopen(duplicate,"w");
	if( org==NULL || dup==NULL)
	{
		puts("Unable to copy the file");
		return(1);
	}

	/* read/write to copy the file */
	while(1)
	{
		c = fgetc(org);
		if( c == EOF )
			break;
		fputc(c,dup);
	}

	printf("%s copied to %s\n",original,duplicate);

	fclose(org);
	fclose(dup);

	return(0);
}

