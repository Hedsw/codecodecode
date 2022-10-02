#include <stdio.h>

int main(int argc, char **argv)
{
	int x;

	if( argc < 2)
		puts("No extra arguments found");
	else
	{
		for(x=1;x<argc;x++)
			printf("Argument %d is %s\n",x,*(argv+x) );
	}

	return(0);
}
