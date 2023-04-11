'''

Exercise 4, gaussian.py, continued:

'''

import numpy
import matplotlib.pyplot as plot

n = 50000
x = numpy.random.randn(n)

a = 4
b = 0
y = a * x + b

ev = numpy.mean(y)
var = numpy.std(y)

bins = 100
num_points, boundary_values, _ = plot.hist(
    y, bins=bins, density=True, alpha=0.5, label='aX + b')

pdf_x = numpy.linspace(numpy.min(boundary_values),
                       numpy.max(boundary_values), 100)
pdf_y = 1 / (var * numpy.sqrt(2 * numpy.pi)) * \
    numpy.exp(-0.5 * ((pdf_x - ev) / var) ** 2)
plot.plot(pdf_x, pdf_y, color='blue', linewidth=2, label='Transformed PDF')

plot.title(f'Gaussian RV: ({b}, {a}^2)')
plot.xlabel('Value')
plot.ylabel('Density')

plot.legend()
plot.show()
