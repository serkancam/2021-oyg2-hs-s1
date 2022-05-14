#include <stdio.h>

int i = 0;
int f(int y)
{
    i++;
    if (y == 0)
        return i;
    return f(y / 2) + f(y - 1);
}
int main()
{
    printf("%d\n", f(4));
}