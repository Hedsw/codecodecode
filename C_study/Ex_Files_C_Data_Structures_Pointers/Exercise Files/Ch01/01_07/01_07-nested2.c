#include <stdio.h>
#include <string.h>

int main()
{
	struct date {
		int month;
		int day;
		int year;
	};
	struct person {
		struct date birthday;
		struct date died;
		char name[32];
	};
	struct person president;

	president.birthday.month = 2;
	president.birthday.day = 22;
	president.birthday.year = 1732;
	president.died.month = 12;
	president.died.day = 14;
	president.died.year = 1799;
	strcpy(president.name,"George Washington");

	printf("%s was born on %d/%d/%d and died on %d/%d/%d\n",
			president.name,
			president.birthday.month,
			president.birthday.day,
			president.birthday.year,
			president.died.month,
			president.died.day,
			president.died.year
		  );

	return(0);
}

