#include <stdio.h>

int main()
{
	union storage {
		char a;
		int b;
	} reg;

	reg.a = 'A';
	printf("reg.a stores %c\n",reg.a);

	reg.b = 1346;

	printf("reg.b stores %d\n",reg.b);
	reg.b = 1349;

	printf("reg.a stores %c\n",reg.a);

	// 이거 값이 자꾸 바뀌는데.. 그 이유는 Union은 Variable의 Storage를 공유하고 있고,
	// 그 공유된 Storage의 값이 B가 바뀔 때 마다 A도 영향을 받아서 바뀌는 것

	return(0);
}

