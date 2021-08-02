//
//  adj.c
//  ADCS_Functions
//
//  Created by Ayush Mehta on 14/04/21.
//

#include "matrix.h"

double** adj(int n, double matrix[n][n]) {
    
//    Dynamically allocating memory to the varaible
    double **res;
    res = malloc(sizeof(double*) * n);
     
    for(int i = 0; i < n; i++) {
        res[i] = malloc(sizeof(double*) * n);
    }
    
    double a[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            double temp[n - 1][n - 1];
            for (int x = 0; x < n; x++) {
                if (x == i)
                    continue;
                for (int y = 0; y < n; y++) {
                    if (y == j)
                        continue;
                    if (x < i && y < j)
                        temp[x][y] = matrix[x][y];
                    if (x < i && y > j)
                        temp[x][y - 1] = matrix[x][y];
                    if (x > i && y < j)
                        temp[x - 1][y] = matrix[x][y];
                    if (x > i && y > j)
                        temp[x - 1][y - 1] = matrix[x][y];
                }
            }
            a[i][j] = pow(-1, i + j) * det(n - 1, temp);
        }
    }
    res = trn(n, a);
    
    return res;
}
