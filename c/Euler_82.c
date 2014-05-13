/**
 * Path sum: Three ways
 * https://projecteuler.net/problem=82
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
int min(int, int, int);

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

  /* Calculate preliminary values in the first row, first column, and bottom row */
  for (i = 1; i < cols; i++) {
    dp[0][i] = dp[0][i-1] + matrix[0][i];
  }

  for (i = 1; i < rows; i++) {
    dp[i][0] = dp[i-1][0] + matrix[i][0];
  }

  for (i = 1; i < cols; i++) {
    dp[rows-1][i] = dp[rows-1][i-1] + matrix[rows-1][i];
  }

  /**
   * Dynamic Programming Step
   * Each position is defined as its cost in the matrix, plus the minimum
   * of each of the positions it can come from (top, left, or bottom)
   */

  /* First iterate up from the bottom */
  for (i = rows-2; i >= 0; i--) {
    for (j = 1; j < cols; j++) {
      dp[i][j] = min(dp[i+1][j], dp[i][j-1], -1) + matrix[i][j];
    }
  }

  for (i = 1; i < rows-2; i++) {
    for (j = 1; j < cols; j++) {
      dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i+1][j]) + matrix[i][j];
    }
  }

  /**
   * The result is the minimum value in the last column
   */
  result = dp[0][cols-1];
  for (i = 1; i < rows; i++) {
    if (dp[i][cols-1] < result) {
      result = dp[i][cols-1];
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
 * Computes the min between three numbers
 * Or three if you pass -1 in for z
 */
int min(int x, int y, int z) {
  if (z < 0) {
    return (x < y) ? x : y;
  }

  if (x < y) {
    return (x < z) ? x : z;
  } else {
    return (y < z) ? y : z;
  }
}

