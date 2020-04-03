#! python3

import matplotlib.pyplot as plt
import numpy as np

#generic X,Y
X = [1, 2, 3]
Y = [1, 2, 3]
costFun = []
tangetVal = np.linspace(-0.5, 2.5, 100)

for i in tangetVal: 
	for j in range(len(X)):
		meanConstant = 1/(2*len(X));
		perTangentValueRes = pow((i*X[j]-Y[j]), 2)
		perTangentValueRes *= meanConstant
	costFun += [perTangentValueRes]


plt.legend()
plt.plot(tangetVal, costFun, '-r')
plt.xlabel("tangetValues")
plt.ylabel("costFunction Values")
plt.show()

# plt.plot(X, Y, '-r')
# plt.title('CostFunction')
# plt.show()
