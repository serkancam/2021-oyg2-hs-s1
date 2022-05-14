#include <stdio.h>

int main()
{
    int i = 1;

    switch (i)
    {
    case 0:
        printf("0-%d\n", i);
    // break;
    default:
        printf("varsayılan\n");
        break;
    case 1:
        printf("1-%d\n", i);
        break;
    case 2:
        printf("2-%d\n", i);
        break;
    }

    return 0;
}