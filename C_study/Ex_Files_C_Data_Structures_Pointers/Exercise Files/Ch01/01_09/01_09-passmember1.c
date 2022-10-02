#include <stdio.h>

char *show_color(char c);

int main()
{
	struct pixel {
		int horz;
		int vert;
		char color;
	} center;

	center.horz = 320;
	center.vert = 240;
	center.color = 'r';

	printf("The pixel at %d,%d is colored %s\n",
			center.horz,
			center.vert,
			show_color(center.color)
		  );

	return(0);
}

char *show_color(char c)
{
	switch(c)
	{
		case 'r':
			return("red");
		case 'g':
			return("green");
		case 'b':
			return("blue");
		default:
			return("Invalid");
	}
}

