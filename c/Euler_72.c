#include <stdio.h>

// distinct prime factorization
int *dpf(int);
int totient(int);

int main(int argc, char **argv) {
    int i;
    long total = 0;
    
    for (i = 2; i < 1000001; i++)
        total += totient(i);
        
    printf("Total: %ld\n", total);
}

int totient(int n) {
    int num = 1;
    int denom = 1;
    int d = n;
    
    int curr = 2;
    while (d > 1) {
       if (!(d % curr)) {
           while (!(d % curr))
               d /= curr;

           denom *= curr;
           num *= (curr - 1);
       } 
       
       curr++;
    }
    
    return n * num / denom;
}