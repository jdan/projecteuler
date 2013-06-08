int frac_cmp(int n1, int d1, int n2, int d2) {
  int L, R;

  L = n1 * d2;
  R = n2 * d1;

  if (L == R) {
    return 0;
  } else if (L > R) {
    return 1;
  } else {
    return -1;
  }
}

int gcd(int a, int b) {
  while(1) {
    if (a == 0) {
      return b;
    } else if (b == 0) {
      return a;
    } else if (a == 1 || b == 1) {
      return 1;
    } else if (a > b) {
      a -= b;
    } else {
      b -= a;
    }
  }
}

int reduced(int n, int d) {
  return gcd(n, d) == 1;
}

int main(int argc, char **argv) {
  int total, lower_bound, upper_bound, n, d;

  for (d = 4; d <= atoi(argv[1]); d++) {
    lower_bound = d / 3;
    upper_bound = d / 2;

    for (n = lower_bound; n <= upper_bound; n++) {
      if (reduced(n, d) && frac_cmp(n, d, 1, 3) == 1 && frac_cmp(n, d, 1, 2) == -1) {
        total++;
      }
    }
  }

  printf("Total: %d\n", total);
}
