#include <stdio.h>

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
	} president = {
		{ 2, 22, 1732 },
		{ 12, 14, 1799 },
		"George Washington"
	};

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

