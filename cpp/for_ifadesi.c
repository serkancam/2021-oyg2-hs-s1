#include <stdio.h>

int main()
{

    /*
    for(döngü değişkeni;döngü şartı; değişim)
    */
  
   for( int i=0;i<5;i++)
   {
       printf("i=%d\n",i);
   }
  // printf("dış i=%d\n",i);
  int j=0;
  for(;;)
  {
      printf("j=%d\n",++j);
      if(j>5)
      break;
  }
  /*
  
  for(int j=0;j<=6;j++)
  {
      printf("j=%d\n",j);
    
  }
  */
}