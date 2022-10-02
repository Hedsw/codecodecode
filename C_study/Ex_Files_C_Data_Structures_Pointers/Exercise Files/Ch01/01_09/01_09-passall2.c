#include <stdio.h>

struct pixel {
	int horz;
	int vert;
	char color;
};

void show_pixel(struct pixel p); // 여기서 Pixel을 파라메터로 쓰고 있기 때문에 pixel
//이 무엇인지를 이거 전에 먼저 Define 해야함. 그래서 pixel structure를 이 함수 선언 전으로 이동

int main()
{
	struct pixel center;

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

