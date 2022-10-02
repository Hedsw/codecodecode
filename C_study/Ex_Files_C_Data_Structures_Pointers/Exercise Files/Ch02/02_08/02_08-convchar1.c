#include <stdio.h>

int main()
{
	int a = 123;

	puts("The %d placeholder, no width specification:");
	printf("%d\n",a);
	puts("8-character width:");
	printf("%8d\n",a);
	printf("%8d\n",a*10);
	printf("%8d\n",a*100);
	puts("Left-justified 8-character width:");
	printf("%-8d\n",a);
	printf("%-8d\n",a*10);
	printf("%-8d\n",a*100);
	puts("8-character width padded with zeros:");
	printf("%08d\n",a);
	printf("%08d\n",a*10);
	printf("%08d\n",a*100);

	return(0);
}

