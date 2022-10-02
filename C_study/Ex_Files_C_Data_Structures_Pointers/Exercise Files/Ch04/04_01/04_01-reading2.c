#include <stdio.h>

int main()
{
	const char filename[] = "sonnet18.txt";
	FILE *fh;
	int ch;

	/* open the file */
	fh = fopen(filename,"r");
	if( fh == NULL )
	{
		printf("Unable to read from file %s\n",filename);
		return(1);
	}
	
	/* read the file one character at a time */
	while(1)
	{
		ch = fgetc(fh);
		if( ch == EOF )
			break;
		putchar(ch);
	}

	/* close when you're done */
	fclose(fh);

	return(0);
}
