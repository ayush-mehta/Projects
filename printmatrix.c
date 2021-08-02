//
//  printm.c
//  ADCS_Functions
//
//  Created by Ayush Mehta on 21/03/21.
/*
 The Following function prints a matrix with given rows and columns
 INPUT: - r: Number of rows of the given matrix
        - c: Number of columns of the given matrix
        - mat: Matrix to be printed with 'r' rows and 'c' columns
 OUTPUT: - Prints the given matrix
*/
#include "matrix.h"

void printmatrix(int r, int c, double mat[r][c]) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++){
            printf("%0.2f ", mat[i][j]);
        }
        printf("\n");
    }
}

