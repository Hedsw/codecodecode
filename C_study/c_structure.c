#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    struct pixel {
        int horz;
        int vert;
        char color;
    };

    struct pixel center;

    center.color = 'r';
    center.horz = 320;
    center.vert = 100;
    
    printf("Print %d %d", center.horz, center.vert);

    switch(center.color) {
        case 'r':
            puts("red");
            break;
        case 'g':
            puts("green");
            break;
        case 'b':
            puts("Black");
            break; 

    }


    return 0;
}