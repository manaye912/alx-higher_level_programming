#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
     for raw in range(len(matrix)):
         for col in range(len(matrix[i])):
             print("{:d}".format(matrix[raw][col]), end="")
             if col != (len(matrix[raw]) - 1):
                 print(" ", end="")
                 print("")
