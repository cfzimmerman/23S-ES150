''' 

PS7 Q4 part 3 

'''

import numpy
import matplotlib.pyplot as plot
from scipy.special import erfinv

n = 50000
x = numpy.random.rand(n)

quant = numpy.sqrt(2) * erfinv(2 * x - 1)
# Compute the quantile function

xrange = numpy.linspace(-5, 5, 100)
pdf = 1 / numpy.sqrt(2 * numpy.pi) * numpy.exp(-xrange ** 2 / 2)

plot.hist(quant, bins=50, density=True, alpha=0.5, label='Standard normal')
plot.plot(xrange, pdf, label='PMF')

plot.xlabel('Value')
plot.ylabel('Density')
plot.title('Standard normal from Uniform using PIT')

plot.legend()
plot.show()
