#include <stdio.h>

int main(int argc, char **argv) {
    long long int n;
    int i;
    
    n = 1;
    
    for (i = 2; i <= 100000; i++) {
        n *= i;
        
        while (!(n % 10))
            n /= 10;
        
        n %= 100000;
    }
    
    printf("%lld\n", n);
}