#include<stdio.h>
#include<string.h>
int main()
{
char a[10];
int i,j,l,c=0;
printf("enter string");
gets(a);
l=strlen(a);
j=l;
for(i=0;i<l/2;i++)
{
if(a[i]==a[j-1])
{
c++;
j--;
}
}
if(c==l/2)
{
printf("string is palindrome");
}
else
{
printf("string is not palindrome");
}
return 0;
}
