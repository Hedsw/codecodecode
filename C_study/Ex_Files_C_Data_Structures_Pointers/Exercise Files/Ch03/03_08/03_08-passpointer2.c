#include <stdio.h>

void doubler(int *alpha)
{
	*alpha += *alpha;
}

int main()
{
	int *a,b;

	b = 25;
	a = &b;
	printf("Value before: %d\n",*a);
	doubler(a);
	printf("Value after: %d\n",*a);

	return(0);
}

