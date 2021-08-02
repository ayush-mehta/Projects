//
//  inv.c
//  ADCS_Functions
//
//  Created by Ayush Mehta on 14/04/21.
//

#include "matrix.h"

double** inv(int n, double matrix[n][n]) {
    
//    Dynamically allocating memory to the varaible
    double **res;
    res = malloc(sizeof(double*) * n);
     
    for(int i = 0; i < n; i++) {
        res[i] = malloc(sizeof(double*) * n);
    }
    

    if (det(n, matrix) == 0)
        return 0;
    res = adj(n, matrix);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            res[i][j] = res[i][j] / det(n, matrix);
        }
    }
    return res;
}
