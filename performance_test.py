# from timeit import default_timer as timer
# import matplotlib.pyplot as plt


# def loopAdder(length):
# 	result = 0
# 	for i in range(length):
# 		result = result+i
# 	return result

# sizes = [100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
# XVAL = []
# YVAL = []

# for i in range(len(sizes)):
# 	start = timer()
# 	loopAdder(sizes[i])
# 	end = timer() - start
# 	XVAL = XVAL+[len(str(sizes[i]))-1]
# 	YVAL = YVAL+[end]
# 	print("10^"+str(len(str(sizes[i]))-1)+" sizes input took "+ str(end)+ "s")


# plt.plot(XVAL, YVAL, "ro")
# plt.xlabel('input size on power of 10 or 10^')
# plt.axis([1, 10, -0.1, 100])
# plt.show()

from timeit import default_timer as timer
def calculate(size_in_power):
	a = []
	num = pow(10, int(size_in_power))
	start = timer()
	for i in range(0, num):
		a+=[i]
	stop = timer()-start
	print("elapsed time {:.8f} secodns".format(stop-start))

calculate(8)
