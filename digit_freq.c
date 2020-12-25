//https://www.hackerrank.com/challenges/frequency-of-digits-1/problem

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int l,i;
    int num[10];
    for(i=0;i<=9;i++){
        num[i] = 0;
    }
    char s[1001];
    scanf("%s",s);
    l = strlen(s);
    for(i=0;i<l;i++){
        if(s[i]>=48 && s[i]<58){
            num[s[i]-48] += 1; 
        }
    }
    printf("%d",num[0]);
    for(i=1;i<=9;i++){
       printf(" %d",num[i]); 
    }  
    return 0;
}
