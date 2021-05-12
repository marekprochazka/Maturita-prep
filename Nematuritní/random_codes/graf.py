from matplotlib.pyplot import *
from numpy import arange
# x = arrange(-5,5,0.2) -> vekror x od -5 do 5 s krokem 0.2

x = arange(-3, 3, 0.01)
y1 = x**2-1
y2 = 2*x+1
fill_between(x, y1, y2, where=(y2 > y1), facecolor="gray")
plot(x, y1, "black")
plot(x, y2, "black")
text(0, 0, 'popisek', fontsize='16', color="blue")

annotate('Vybarvená plocha', xy=(-2, 8),
         xytext=(1, -4), arrowprops=dict(facecolor="g"))

grid(True)
show()
