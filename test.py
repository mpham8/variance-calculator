import calculator as calc
import pandas as pd
import numpy as np

#created an example of a dataframe
# i = [0.0575, -0.0971, -0.0559, -0.0814, 0.1187]
# j = [0.0297, -0.1795, -0.003, -0.0422, -0.0133]
# k = [0.0532, 0.0322, 0.1261, -0.1079, 0.0507]
# l = [0.1018, 0.0273, -0.1592, -0.0548, 0.0859]

i = [0.0575, -0.0971, -0.0559, -0.0814, 0.1187]
j = [0.0297, -0.1795, -0.003, -0.0422, -0.0133]
k = [0.0532, 0.0322, 0.1261, -0.1079, 0.0507]
l = [0.1018, 0.0273, 0.08, -0.0548, 0.0859]

i_series = pd.Series(i, name = 'i')
j_series = pd.Series(j, name = 'j')
k_series = pd.Series(k, name = 'k')
l_series = pd.Series(l, name = 'l')

data_frame = pd.concat([i_series, j_series, k_series, l_series], axis=1)


#created an example of a list of weights
weights = [0.00, 0.3, 0.4, 0.3] #aapl, #google, #exon, #walmart



#EDIT THIS!
covariance, variance, semivariance = calc.main(data_frame, weights, reference_return = 0)

print(covariance)
print(variance)
print(semivariance)
