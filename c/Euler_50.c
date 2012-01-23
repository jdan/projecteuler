#include <stdio.h>
#include <math.h>

char is_prime(int);
int next_prime(int);

int main(int argc, char **argv) {
    int top, j, k, length_max, prime_max;
    
    if (argc > 1)
        top = atoi(argv[1]);
    else
        top = 1e6;
        
    for (j = 2; j < top; j = next_prime(j)) {
        int length_temp = 0;
        int prime_temp = 0;
        
        for (k = j; prime_temp < top; k = next_prime(k)) {
            prime_temp += k;
            length_temp++;
            
            if ((prime_temp < top) && (length_temp > length_max) && is_prime(prime_temp)) {
                length_max = length_temp;
                prime_max = prime_temp;
            }
        }
    }
    
    printf("Max: %d (%d primes)\n", prime_max, length_max);
    
    exit(1);
}

char is_prime(int n) {
    int i;
    
    if (!(n % 2))
        return 0;
    
    for (i = 3; i <= sqrt(n); i += 2)
        if (!(n % i))
            return 0;
    
    return 1;
}

int next_prime(int n) {
    n++;
    
    while (!is_prime(n)) 
        n++;
        
    return n;
}