#include <stdio.h>

int main()
{
	int text[10];
	int *pt;

	pt = text;
	printf("Address of text = %p\n",text);
	printf("Address of pt = %p\n",pt);

	return(0);
}

