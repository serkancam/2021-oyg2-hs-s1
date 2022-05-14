#include <stdio.h>

int main()
{
    char c1 = 'd';
    printf("c=%c,c=%d\n",c1,c1);
    printf("c=%c\n",c1-32);
    printf("deger=%c\n",78);
    c1++;
    printf("c=%c\n",c1);
    printf("boyut=%d\n",sizeof(1.2F));
    int s=90;
    printf("s=%d,s=%o,s=%0x,s=%c\n",s,s,s,s);
    int o1,h1,b1;
    o1=01257;
    h1=0x12547;
    b1=0b110011011;
    printf("o1=%d,h1=%d,b1=%d\n",o1,h1,b1);

    return 0;
}