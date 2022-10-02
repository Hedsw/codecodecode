#include <stdio.h>

int main()
{
	int original[5] = { 45, 50, 88, 100, 213 };
	int duplicate[5];
	int x;

	for(x=0;x<5;x++)
		duplicate[x] = original[x];

	puts("Array values:");
	for(x=0;x<5;x++)
		printf("Element#%d %3d == %3d\n",
				x,
				original[x],
				duplicate[x]
			  );

	return(0);
}
