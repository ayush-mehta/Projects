//
//  trn.c
//  ADCS_Functions
//
//  Created by Ayush Mehta on 14/04/21.
//

#include "matrix.h"

double** trn(int n, double matrix[n][n]) {
    
//    Dynamically allocating memory to the varaible
    double **res;
    res = malloc(sizeof(double*) * n);
     
    for(int i = 0; i < n; i++) {
        res[i] = malloc(sizeof(double*) * n);
    }
    
//    Carrying out the transpose operation
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
                res[i][j] = matrix[j][i];
        }
    }
    
    return res;
}
    
