#include <stdio.h>

void show_pixel(struct pixel p);

int main()
{
	struct pixel {
		int horz;
		int vert;
		char color;
	} center; // 이렇게 선언하면 Local이라서 라인 17에서 Parameter로 보냈을 때 인식X
	// 그래서 01_09-passall2.c 처럼 해야함 

	center.horz = 320;
	center.vert = 240;
	center.color = 'r';

	show_pixel(center);

	return(0);
}

void show_pixel(struct pixel p)
{
	printf("Pixel found at %d,%d, color = ",
			p.horz,
			p.vert
		  );
	switch(p.color)
	{
		case 'r':
			puts("red");
			break;
		case 'g':
			puts("green");
			break;
		case 'b':
			puts("blue");
			break;
		default:
			puts("Invalid");
	}
}

