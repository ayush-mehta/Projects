//
//  det.c
//  ADCS_Functions
//
//  Created by Ayush Mehta on 23/03/21.
//
/*
 The following function computes the determinant of the given n x n matrix
 INPUT: - Size of the matrix
        - The given matrix
 OUTPUT: - The determinant value
 */


#include "matrix.h"

double det(int size, double matrix[size][size]) {
    if(size==1){
        return matrix[0][0];
    }
    else if(size==2){
        int ret = ((matrix[0][0]) * (matrix[1][1]) - (matrix[0][1]) * (matrix[1][0]));
        return ret;
    }
    else {
        int sum = 0;
        for (int i = 0; i<size; i++){
            double return_matrix[size - 1][size - 1];
            int skip_value = 0;
            for(int j=0; j<size-1;j++){
                if(j==i){
                    skip_value++;
                }
                for(int k = 0; k < size - 1; k++) {
                    return_matrix[j][k] = matrix[j+skip_value][k];
                }
            }
            int determinant = det(size - 1, return_matrix);
            sum+= (matrix[i][size-1]) * (pow(-1, i)) * (determinant);
        }
        if(size%2) {
            return sum;
        }
        else {
            return -sum;
        }
    }

}
