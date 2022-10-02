#include <stdio.h>
#include <string.h>

struct tookoffice {
    int month;
    int day;
    int year;
};

struct person {
    char name[32];
    struct tookoffice tookoffices;
};

void show(struct person p[]) {
    int x;

    puts("Presidents:");
    for(x = 0; x < 4; x++) {
        printf("President %s took office on %d / %d / %d \n",
            p[x].name,
            p[x].tookoffices.month,
            p[x].tookoffices.day,
            p[x].tookoffices.year);
    }
}
int main() {
    struct person presidents[5] = {
		{ "George Washington", { 4, 30, 1789 } },
		{ "Thomas Jefferson", { 3, 4, 1801 } },
		{ "Abraham Lincoln", { 3, 4, 1861 } },
		{ "Theodore Roosevelt", { 9, 14, 1901 } }
	};

    struct person temp; // Swap할 때 요렇게 선언해주고 Swap 하면 됨 
    show(presidents);

    printf("Swapping");
    temp = presidents[1];
    presidents[1] = presidents[2];
    presidents[2] = temp;

    show(presidents);

    return 0;
}