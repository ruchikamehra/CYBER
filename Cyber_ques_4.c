#include<stdio.h>
#include<string.h>
int main()
{
    int i,j,ch,x=0;
    char s[50];
    printf("enter the string ");
    gets(s);
    printf("enter the choice : 1-Encrypt, 2-Decrypt");
    scanf("%d",&ch);
    if(ch==1)
    {
        for(i=0;s[i]!='\0';i++)
        {
            if(s[i]>85&&s[i]<=90)
            {
                x=0;
               for(j=90;j>=85;j--)
               {
                   if(s[i]==j)
                   {
                       s[i]=s[i]-25+x+x+4;
                       break;
                   }
                   x++;
               }
            }
            else if(s[i]>=118&&s[i]<=122)
            {

                x=0;
               for(j=122;j>=118;j--)
               {
                   if(s[i]==j)
                   {
                       s[i]=s[i]-25+x+x+4;
                       break;
                   }
                   x++;
               }
            }
           else if((s[i]>=65&&s[i]<=90)||(s[i]>=97&&s[i]<=117))
           {
                 s[i]=s[i]+5;
           }
        }

        printf("the encrypted string: ");
    }
    else if(ch==2)
    {
       for(i=0;s[i]!='\0';i++)
        {
            if(s[i]>=97&&s[i]<=101)
            {
                x=0;
               for(j=97;j<=101;j++)
               {
                   if(s[i]==j)
                   {
                       s[i]=s[i]+25-4;
                       break;
                   }
                   x++;
               }
            }
            else if(s[i]>=65&&s[i]<=69)
             {
                x=0;
               for(j=65;j<=69;j++)
               {
                   if(s[i]==j)
                   {
                       s[i]=s[i]+25-4;
                       break;
                   }
                   x++;
               }
             }
            else if((s[i]>101&&s[i]<=122)||(s[i]>=69&&s[i]<=122))
              {
                 s[i]=s[i]-5;
              }
        }
        printf("the decrypted string : ");
    }

    puts(s);
    return 0;
}
