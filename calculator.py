#Covariance Matrix, Variance, Semi-Variance Calculator using only vanilla python
#Michael Pham, July 2022

import pandas as pd
import numpy as np


def calculate_b_matrix(df, reference_return):

  #t is an integer that represents time periods
  t = len(df)
  print(f't = {t}')

  #calculate t x 1 vector (greek letter i) that fits needs of equation
  filler_vector = []
  for h in range(t):
    filler_vector.append([1])
  filler_vector = np.array(filler_vector)
  print(f'vector i =\n {filler_vector}')

  #calculate t x n Matrix R where there are n variables
  r_matrix = df
  print(f'Matrix R  =\n{r_matrix}')

  #calculate 1 x t vector e
  # if calculating semivariance e is [reference return,..., reference return]
  # if calculating variance e is [mean of i, mean of j,..., mean of z]
  if reference_return == 'no reference return':
    #get e = [u1, u2,..., u4]
    e = [-0.01164, -0.04166, 0.03086, 0.0002]
  else:
    e = []
    for h in range(len(df.columns)):
      e.append(reference_return) 
  e_vector = np.array([e,])
  print(f'vector e = \n{e_vector}')

  #calculate t x n Matrix B
  b_matrix = ( 1/np.sqrt(t) ) * (r_matrix - np.matmul(filler_vector, e_vector))
  print(f'Matrix B = \n{b_matrix}')

  return b_matrix


def calculate_semivariance(b_matrix, weights):

  #create n x 1 weights vector
  weights_vector = np.array(weights)

  #CHANGE MODIFIED TO CORRECTED VOCAB FOR NEGATION
  #create matrix A which is (x^t B^t)^-
  a = np.transpose(weights_vector)@np.transpose(b_matrix)
  a_modified = a._get_numeric_data() #ERROR
  a_modified[a_modified > 0] = 0
  print(f'modified Matrix A = \n{a_modified}')

  #create matrix B which is (Bx)^-
  b = b_matrix@weights_vector
  b_modified = b._get_numeric_data() #ERROR
  b_modified[b_modified > 0] = 0
  print(f'modified Matrix B = \n{b_modified}')

  #calculate semivariance
  semivariance = a_modified@b_modified

  print('-'*20)
  print(f'SEMIVARIANCE = {semivariance}')
  print('-'*20)


  return semivariance


def calculate_variance(b_matrix, weights):
  #calculate Covariance Matrix
  print('-'*20)

  #calculate n x n covariance matrix
  covariance_matrix = np.transpose(b_matrix)@b_matrix
  print(f'COVARIANCE MATRIX = \n{covariance_matrix}')

  #calculate variance
  variance = np.transpose(weights)@covariance_matrix@weights
  print(f'VARIANCE = {variance}')
  print('-'*20)

  return covariance_matrix, variance


def semivariance(df, weights, reference_return):
  b_matrix = calculate_b_matrix(df, reference_return)
  semi_variance = calculate_semivariance(b_matrix, weights)
  return semi_variance


def variance(df, weights):
  b_matrix = calculate_b_matrix(df, 'no reference return')
  covariance_matrix, variance = calculate_variance(b_matrix, weights)
  return covariance_matrix, variance


def main(data_frame, weights, reference_return):
  #input dataframe with 2+ variables
  semivar = semivariance(data_frame, weights, reference_return)
  covar, var = variance(data_frame, weights)

  return covar, semivar, var







