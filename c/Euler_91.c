// Euler 91 Solution
// Jordan Scales (http://jordanscales.com)
// 19 Aug 2013

#include <stdio.h>

int dot(a1, a2, b1, b2) {
  return a1 * b1 + a2 * b2;
}

long rightTriangles(int m) {
  long total = 0;
  int x1, y1, x2, y2;
  for (x1 = 0; x1 <= m; x1++) {
    for (y1 = 0; y1 <= m; y1++) {
      for (x2 = 0; x2 <= m; x2++) {
        for (y2 = 0; y2 <= m; y2++) {
          if ((x1 == 0 && y1 == 0) || (x2 == 0 && y2 == 0)) continue;
          if ((x1 == x2) && (y1 == y2)) continue;

          if ((dot(x1, y1, x2, y2) == 0) ||
              (dot(x1, y1, x2 - x1, y2 - y1) == 0) ||
              (dot(x2, y2, x2 - x1, y2 - y1) == 0)) {
            total++;
          }
        }
      }
    }
  }

  return total / 2;
}

int main(int argc, char **argv) {
  if (argc < 2) return 1;
  printf("Result: %ld\n", rightTriangles(atoi(argv[1])));
  return 0;
}
