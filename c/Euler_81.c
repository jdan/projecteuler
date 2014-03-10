/**
 * Path sum: Two ways
 * https://projecteuler.net/problem=81
 *
 * Jordan Scales <scalesjordan@gmail.com>
 * for CS370
 * 9 Mar 2014
 */

#include <stdio.h>
#include <stdlib.h>

const int ROW = 80;
const int COL = 80;

int minimumPathSum(int**, int, int);
int min(int, int);

int main() {
  int **matrix, i, j;

  /* Allocate memory for the matrix */
  matrix = (int**)malloc(ROW * sizeof(int*));
  for (i = 0; i < ROW; i++) {
    matrix[i] = (int*)malloc(COL * sizeof(int));
  }

  /* Read in the values */
  for (i = 0; i < ROW; i++) {
    for (j = 0; j < COL; j++) {
      /* Scan for a number followed by a comma */
      scanf("%d,", &(matrix[i][j]));
    }
  }

  printf("Result: %d\n", minimumPathSum(matrix, ROW, COL));

  /* Free the matrix */
  for (i = 0; i < ROW; i++) {
    free(matrix[i]);
  }
  free(matrix);
}

int minimumPathSum(int **matrix, int rows, int cols) {
  int **dp, i, j, result;

  /* Allocate memory for the DP matrix */
  dp = (int**)malloc(rows * sizeof(int*));
  for (i = 0; i < rows; i++) {
    dp[i] = (int*)malloc(cols * sizeof(int));
  }

  /* Set the top corner value */
  dp[0][0] = matrix[0][0];

  /* Calculate preliminary values in the first row and first column */
  for (i = 1; i < cols; i++) {
    dp[0][i] = dp[0][i-1] + matrix[0][i];
  }

  for (i = 1; i < rows; i++) {
    dp[i][0] = dp[i-1][0] + matrix[i][0];
  }

  /**
   * Dynamic Programming Step
   * Each position is defined as its cost in the matrix, plus the minimum
   * of each of the positions it can come from (top or left)
   */
  for (i = 1; i < rows; i++) {
    for (j = 1; j < cols; j++) {
      dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j];
    }
  }

  result = dp[rows-1][cols-1];

  /* free the DP matrix */
  for (i = 0; i < rows; i++) {
    free(dp[i]);
  }
  free(dp);

  return result;
}

/**
 * Computes the min between two numbers
 */
int min(int x, int y) {
  return (x > y) ? y : x;
}

