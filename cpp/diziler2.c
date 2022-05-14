#include <stdio.h>

int main()
{
    int d[5] = {1, 2, 8, 12, 10, 6};
    d[100] = 6;
    printf("%d\n", d[5]);
    printf(" d adresi %p\n", d);
    printf(" d[0] adresi %p\n", &d[0]);
    printf(" d[1] adresi %p\n", &d[1]);
    printf(" (3)[d] değeri %d\n", (3)[d]);
    int *a = d + 2;
    printf("a[0]=%d\n", a[0]);
    printf("sizeof(a)=%d\n", sizeof(a));
    printf("sizeof(*a)=%d\n", sizeof(*a));
    a=a+2;
    printf("a[0]=%d\n", a[0]);

    printf("(3)[d]+(2)[d]=%d\n",++(3)[d]+(2)[d]--);
    printf("d[3]=%d\n",d[3]);

    int dd[3][4]={22,35,365,78,36};

    int i=-1,j;
   // j= i++ + ++i + ++i;
   // printf("j=%d",j);
   // printf("j=%d\n",i++ + ++i + ++i);
    // printf("%d %d %d\n",i++ , ++i , ++i);
    printf("%d %d \n",i++, ++i);



    
   

}