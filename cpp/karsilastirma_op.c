#include <stdio.h>

int main()
{
    /*
    karşılaştırma operatörünün sonucu ya 1 ya da 0 çıkar
    a<b
    a<=b
    a>b
    a>=b
    a!=b
    a==b
    */
    int a = 5, b = 8, c;

    c = 3 < a + b > 9; // 3<a+1-->3<6
    printf("c=%d\n", c);
    /*
    ve --> && eğer şartlardan biri 0 sa sonuç 0 dır
    veya --> ||eğer şartlardan biri 1 ise aonuç 1 dir
    değil --> ! 
   0 ın değili 1
   diğer bütün sayıların değili 0 dır
    */
    int d = 5;
    printf("d nin değili=%d\n", !d);
    printf("%d\n", a < 5 && b > 8);
    printf("%d\n", 1 && 72);
    printf("%d\n", -1 && -72);
    printf("%d\n", -1 && -72);
    printf("%d\n", a < 6 || b > 8);
    c=++a<6 && b++>8; 
    printf("a=%d,b=%d,c=%d,d=%d\n",a,b,c,d);

    

    

    return 0;
}