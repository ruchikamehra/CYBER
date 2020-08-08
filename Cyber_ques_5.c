#include<stdio.h>
#include<string.h>
int main()
{
char a[10];
int i,n,m;
printf("enter the string");
gets(a);
for(i=0;a[i]!='\0';i++)
{
    if(a[i]>=65&&a[i]<=90)
    {
    n=a[i]-64 ;
}
else if(a[i]>=97&&a[i]<=122)
{
    n=a[i]-96;
}
if((i+1)%2==0)
{
  while(n!=0)
  {
  printf("$");
  n--;
  }
}
  else if((i+1)%2!=0)
  {
  while(n!=0)
  {
  printf("#");
  n--;
  }
  }
}
return 0;
}

