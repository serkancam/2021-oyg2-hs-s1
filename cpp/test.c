#include <stdio.h>
#include <math.h>


int main()
{
    /*
    int short --> %d
    float  -->%f
    double -->%lf
    char -->%c


    */
    //short,int,long,long int,char
    // long long unsigned int a=1e19;
//     //int a=6;
//     {
//         //int a=12;
//         printf("a=%ld\n",a);

//     }
//    // printf("%f",sin(M_PI/2));
//     printf("%llu\n",a);
    char a='s';
    char isim[]="çam";
    // printf("%c\n%d\n",a-32,a-32);
    // printf("%s\n",isim);
    // printf("%c\n",135);
    printf("%d\n",sizeof(isim));
    printf("%c\n",isim[4]);

    return 0;
}