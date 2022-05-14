#include <stdio.h>
union paylas{
    double f;
    int i;
    char kr;
};

int main()
{
    int id1[5];//5 elemanlı dizi değerleri rastgele
    int id2[]={3,5,6};//3 elemanlı
    int id3[5]={55,2};//5 elemanlı ilk 2 indis ten sonrası 0 olacak(varsayılan değer)

    printf("id1 boyut=%d\n",sizeof(id1));//byte cinsinden
    printf("id2 boyut=%d\n",sizeof(id2));//byte cinsinden
    printf("id3 boyut=%d\n",sizeof(id3));//byte cinsinden
    printf("id3 eleman sayısı=%d\n",sizeof(id3)/sizeof(int));
    //byte cinsinden

    //char dizi karakter katarı (dizge)
    char *isim="halil osman";
    char ad[4]="serkan";
    char soyad[]="cam";
    // scanf("%s",soyad);
    // printf("%s %s \n",ad,soyad);
    printf("ad--> %d\n",sizeof(ad)/sizeof(char));
    printf("soyad--> %d\n",sizeof(soyad)/sizeof(char));
    printf("isim--> %s\n",isim);
    isim="111111111111111111111112";
    printf("isim--> %s\n",isim);
    //
    union paylas bir,iki;
    // bir.f=3.14;
    // bir.i=65;
    // bir.kr='A';

    printf("%f %d %c\n",bir.f,bir.i,bir.kr);
    printf("union %d\n",sizeof(bir));
    

    




    return 0;
}