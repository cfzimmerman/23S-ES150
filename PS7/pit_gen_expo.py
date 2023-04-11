''' 

PS7 Q4 part 3.2

'''

import numpy
import matplotlib.pyplot as plot

n = 50000
x = numpy.random.rand(n)

quant = -numpy.log(1 - x)
# Compute the quantile function

xrange = numpy.linspace(0, 10, 100)
pdf = numpy.exp(-xrange)

plot.hist(quant, bins=50, density=True,
          alpha=0.5, label='Standard exponential')
plot.plot(xrange, pdf, label='PDF')

plot.xlabel('Value')
plot.ylabel('Density')
plot.title('Standard exponential from Uniform using PIT')

plot.legend()
plot.show()
