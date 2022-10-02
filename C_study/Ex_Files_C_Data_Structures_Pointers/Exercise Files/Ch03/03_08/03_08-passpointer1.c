#include <stdio.h>

void doubler(int *alpha)
{
	*alpha += *alpha;
}

int main()
{
	int a = 2;

	printf("Value before: %d\n",a);
	doubler(&a);
	printf("Value after: %d\n",a);

	return(0);
}

