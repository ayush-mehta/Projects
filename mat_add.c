//
//  matadd.c
//  ADCS_Functions
//
//  Created by Ayush Mehta on 14/04/21.
//

//The folowing functions add/multiplies two matrices
//INPUT: - r: Number of rows for the given matrices
//       - c: Number of columns for the given matrices
//       - matrix1: The first matrix
//       - matrix2: The second matrix
//OUTPUT: - Returns a double pointer to their resultant matrix where res = matrix1 + matrix2
//       - If the input is not valid then the function will return 0
//IMPORTANT
//Remember that this function returns a double pointer, after calling this function store the sum in another 2D array and free it in order to avoid any problems caused by pointers.
//Example:
//
//// This is to check that the input is valid or not
//if (res == 0) {
//    return 1;
//}
//
//// Storing the result in another variable
//double ans[r][c];
//for (int i = 0; i < r; i++) {
//    for (int j = 0; j < c ; j++) {
//        ans[i][j] = res[i][j];
//    }
//}
//
//// Freeing up the pointer
//for(int i = 0; i < 2; i++) {
//        free(res[i]);
//    }
//free(res);
//
//If you don't do this then there will be multiple error which will be difficult to debug later on.
//

#include "matrix.h"

double** mat_add(int r1, int c1, double matrix1[r1][c1], int r2, int c2 ,double matrix2[r2][c2]) {
    
//    Verifies the input, if there is an error in the input data or the operation cannot be carried out then it will return 0
    if (r1 != r2 || c1 != c2) {
        return 0;
    }
    
    int i, j;
    
//    Dynamically allocating memory to the varaible
    double **res;
    res = malloc(sizeof(double*) * r1);
     
    for(i = 0; i < r1; i++) {
        res[i] = malloc(sizeof(double*) * c2);
    }
    
//    Carrying out the desired operation
    for(i = 0; i < r1; i++) {
        for(j = 0; j < c2; j++) {
                res[i][j] = matrix1[i][j] + matrix2[i][j];
        }
    }
    return res;
}
