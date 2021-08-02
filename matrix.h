//
//  adcs.h
//  ADCS_Functions
//
//  Created by Ayush Mehta on 20/03/21.
//

#ifndef matrix_h
#define matrix_h

// Header Files included
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

// Supporting Functions
void printmatrix(int r, int c, double mat[r][c]);
double** mat_add(int r1, int c1, double matrix1[r1][c1], int r2, int c2 ,double matrix2[r2][c2]);
double** mat_mul(int r1, int c1, double matrix1[r1][c1], int r2, int c2 ,double matrix2[r2][c2]);
double det(int size, double matrix[size][size]);
double** trn(int n, double matrix[n][n]);
double** adj(int n, double matrix[n][n]);
double** inv(int n, double matrix[n][n]);
