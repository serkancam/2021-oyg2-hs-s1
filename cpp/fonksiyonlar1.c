#include <stdio.h>

/**
 * 
 *
 <geri dönüş tipi> <fonksiyon adı>([paratmetreler])
 {
     işlemler;


     [return ?;]
 }
 */
void artir1(int sayi)
{
    sayi+=1;

}
void artir2(int *sayi)
{
    *sayi=*sayi+1;
    return 5;
}
void artir3(int sayi[],int uzunluk)
{
    sayi[uzunluk-2]=300;
}
int main()
{
    int s1=10,s2=20;
    int dizi[5]={20,30,45,60,75};
    artir1(s1);
    printf("s1=%d\n",s1);
    artir2(&s2);
    printf("s2=%d---donus=%d\n",s2);
    artir3(dizi,5);
    printf("dizi[3]=%d\n",dizi[3]);

    char *isim="bilsem";

    printf("deger=%d--%c\n",*isim+1,*isim+1);
    printf("deger=%d--%c\n",*(isim+1),*(isim+1));

    printf("adres1=%p,adres2=%p\n",isim,isim+1);
    



    return 0;
}