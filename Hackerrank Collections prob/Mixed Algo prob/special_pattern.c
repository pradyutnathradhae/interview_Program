//https://www.hackerrank.com/challenges/printing-pattern-2/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n,i,j,k,a,cnt = 0;
    scanf("%d", &n);
  	// Complete the code to print the pattern.
    for(a = 1;a<=(2*n)-1;a++){
        for(i=1;i<=cnt;i++)
            printf("%d ",(n-i+1));
        for(j=1;j<=(2*(n-cnt))-1;j++)
            printf("%d ",(n-cnt));
        for(k=cnt;k>=1;k--)
            printf("%d ",(n-k+1));
        if(a>=n)
            cnt = cnt - 1;
        else {
            cnt = cnt +1;
        }
        printf("\n");
    }
    return 0;
}