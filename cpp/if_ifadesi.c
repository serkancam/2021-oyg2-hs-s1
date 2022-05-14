#include <stdio.h>

int main()
{
    int yas;
    printf("yaşınızı giriniz:");
    scanf("%d",&yas);

    if(yas>=18)
    {
       printf("ehliyet alabilir.\n");
    }
    else
    {
       printf("Ehliyet alamaz.\n");
    }
    //bir blok tek satırdan oluşuyorsa küme parantezi kullanılmayabilir. Bu bütün blok yapsısında olan ifadeler için geçerlidir. for/while/

    if(yas>=18)    
    printf("ehliyet alabilir.\n"); 
    // printf("hata")   ;
    else    
    printf("Ehliyet alamaz.\n");
    printf("hata 2 %d %c\n",yas,yas);
    //else if
    if(yas>0 && yas<=10)
    printf("çocuk\n");
    else if(yas>10  && yas<=16)
    printf("ergen\n");
    else if(yas>16 && yas<=25)
    printf("Genç\n");
    else if(yas>25)
    printf("Yaşlı");
    else
    printf("negatif sayı girilemez\n");

    



    return 0;
}