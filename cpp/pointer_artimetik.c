#include <stdio.h>

int main()
{
    int d[][3][2]={4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24};
    int i=-1;
    int j;
    j=d[i++][++i][++i];  //2*6+3*2+2

    printf("%d",j);
    return 0;

}