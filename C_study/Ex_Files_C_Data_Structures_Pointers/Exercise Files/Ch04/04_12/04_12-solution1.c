#include <stdio.h>
#include <unistd.h>
#include <dirent.h>

#define SIZE 512

int main()
{
	DIR *directory;
	FILE *output;
	struct dirent *entry;
	char path[SIZE];
	const char filename[] = "filelist.txt";
	int x,r;

	/* open the output file  - must do this first! */
	/* By doing this step first, you create the output file
	   in the same directory as the program */
	output = fopen(filename,"w");
	if( output == NULL )
	{
		printf("Unable to create file %s\n",filename);
		return(1);
	}

/* fetch path for the directory to read */
	printf("Enter the directory to examine: ");
	fgets(path,SIZE,stdin);
	/* remove the newline */
	for(x=0;x<SIZE;x++)
	{
		if( path[x] == '\n' )
		{
			path[x] = '\0';
			break;
		}
	}

/* change to the directory supplied by the user */
	r = chdir(path);
	/* if this function fails, it's most likely that the
	   user typed an invalid pathname */
	if( r != 0 )
	{
		printf("Unable to change to '%s'\n",path);
		fclose(output);		/* don't forget this part! */
		return(1);
	}

	/* open the directory */
	directory = opendir(path);
	if( directory == NULL )
	{
		printf("Unable to open directory %s\n",path);
		fclose(output);		/* don't forget this part! */
		return(1);
	}

/* read the directory and save the filenames */
	while( (entry=readdir(directory)) != NULL )
	{
		fprintf(output,"%s\n",entry->d_name);
	}
	printf("%s created listing files in %s\n",filename,path);

	/* tidy-up */
	fclose(output);
	closedir(directory);

	return(0);
}

