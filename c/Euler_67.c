/**
 * Maximum path sum II
 * https://projecteuler.net/problem=67
 *
 * Jordan Scales <scalesjordan@gmail.com>
 * for CS370
 * 9 Mar 2014
 */

#include <stdio.h>
#include <stdlib.h>

const int ROW = 100;

int maximumPathSum(int**, int, int);
int max(int, int);

int main() {
  int **matrix, i, j;

  /* Allocate memory for the matrix */
  matrix = (int**)malloc(ROW * sizeof(int*));
  for (i = 0; i < ROW; i++) {
    matrix[i] = (int*)malloc(ROW * sizeof(int));
  }

  /* Read in the values - this time as a TRIANGLE! */
  for (i = 0; i < ROW; i++) {
    for (j = 0; j <= i; j++) {
      /* Scan for a number followed by a comma */
      scanf("%d", &(matrix[i][j]));
    }
  }

  printf("Result: %d\n", maximumPathSum(matrix, ROW, ROW));

  /* Free the matrix */
  for (i = 0; i < ROW; i++) {
    free(matrix[i]);
  }
  free(matrix);
}

int maximumPathSum(int **matrix, int rows, int cols) {
  int **dp, i, j, result;

  /* Allocate memory for the DP matrix */
  dp = (int**)malloc(rows * sizeof(int*));
  for (i = 0; i < rows; i++) {
    dp[i] = (int*)malloc(cols * sizeof(int));
  }

  /* Set the top corner value */
  dp[0][0] = matrix[0][0];

  /* Calculate preliminary values in the first column */
  for (i = 1; i < rows; i++) {
    dp[i][0] = dp[i-1][0] + matrix[i][0];
  }

  /**
   * Dynamic Programming Step
   * Each position is defined as its cost in the matrix, plus the minimum
   * of each of the positions it can come from (top or left)
   */
  for (i = 1; i < rows; i++) {
    for (j = 1; j <= i; j++) {
      if (i == j) {
        dp[i][j] = dp[i-1][j-1] + matrix[i][j];
      } else {
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + matrix[i][j];
      }
    }
  }

  /* find the maximum value in the bottom row */
  result = dp[rows-1][0];
  for (i = 0; i < rows; i++) {
    if (dp[rows-1][i] > result) {
      result = dp[rows-1][i];
    }
  }

  /* free the DP matrix */
  for (i = 0; i < rows; i++) {
    free(dp[i]);
  }
  free(dp);

  return result;
}

/**
 * Computes the max between two numbers
 */
int max(int x, int y) {
  return (x > y) ? x : y;
}

