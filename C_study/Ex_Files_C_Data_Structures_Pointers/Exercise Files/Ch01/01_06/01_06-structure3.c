#include <stdio.h>

int main()
{
	struct pixel {
		int horz;
		int vert;
		char color;
	} top, center, bottom;

	top.horz = 320;
	top.vert = 0;
	top.color = 'r';
	center.horz = 320;
	center.vert = 240;
	center.color = 'g';
	bottom.horz = 320;
	bottom.vert = 480;
	bottom.color = 'b';

	return(0);
}
