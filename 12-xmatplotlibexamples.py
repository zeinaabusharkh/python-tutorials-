###############################################################################
##
##  PYTHON MATPLOTLIB DEMO -- Copyright Michel Pasquier, 2013-2018
##


## This demo using MatplotLib is part of section 12 (Python Graphics and GUI).
## While the code and examples in all the other sections only require Python,
## this file needs the numpy and matplotlib modules to be installed.
## If not available, all resulting plots can be found (for convenience) in
## the PDF file: 12-xMatplotlibExamples-figs.pdf
##
## These examples are borrowed or adapted from the MatplotLib online tutorial
## latest version is always @ https://matplotlib.org/tutorials/index.html


import numpy as np
import matplotlib.pyplot as plt


# Plot Y axis values given as a single list/array, with the X axis values
# automatically generated (starting at 0 i.e., [0,1,2,3])
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()                          # 12-xMatplotlibExamples-figs: 01


# Plot X versus Y, given as 2 lists
plt.plot([1,2,3,4], [1,4,9,16])
plt.show()

# Plot specifying an (optional) format string (using Matlab notation).
# Default is "b-" i.e., a solid blue line; "ro" means red circles.
# axis() specifies the viewport of the axes: [xmin, xmax, ymin, ymax] 
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()                          # 12-xMatplotlibExamples-figs: 02


# Use numpy arrays e.g., evenly sampled time at 200ms intervals.
# Plot using red dashes, blue squares, and green triangles.
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()                          # 12-xMatplotlibExamples-figs: 03


# Working with multiple figures and axes: script to create two subplots
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()                          # 12-xMatplotlibExamples-figs: 04


# Working with text: plot title, axis labels, arbitrary text
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
# Histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

plt.title('Histogram of IQ', fontsize=14, color='red')
plt.xlabel('Smarts')
plt.ylabel('Probability')
# Using mathematical expressions in text, as TeX equations (e.g., sigma)
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()                          # 12-xMatplotlibExamples-figs: 05


# Annotating text
ax = plt.subplot(111)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)
# Specify label, location being annotated, location of the label (both
# are x,y tuples), and pointing arrow.
plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),)
plt.ylim(-2,2)
plt.show()                          # 12-xMatplotlibExamples-figs: 06


###
###  More Matplotlib examples
###  @ http://matplotlib.org/1.3.1/gallery.html
###


# Horizontal bar chart demo
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, people)
plt.xlabel('Performance')
plt.title('How fast do you want to go today?')
plt.show()                          # 12-xMatplotlibExamples-figs: 07


# Scatter plot demo
N = 50
x, y = np.random.rand(N), np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses
plt.scatter(x, y, s=area, alpha=0.5)
plt.show()                          # 12-xMatplotlibExamples-figs: 08


# Demo of the "streamplot" function -- A streamplot, or streamline plot,
# is used to display 2D vector fields. This example shows a few features
# of the stream plot function i.e., varying the color along a streamline,
# the density of streamlines, and the line width along a stream line.
Y, X = np.mgrid[-3:3:100j, -3:3:100j]
U, V = -1 - X**2 + Y, 1 + X - Y**2
speed = np.sqrt(U*U + V*V)
plt.streamplot(X, Y, U, V, color=U, linewidth=2, cmap=plt.cm.autumn)
plt.colorbar()
#f, (ax1, ax2) = plt.subplots(ncols=2)
#ax1.streamplot(X, Y, U, V, density=[0.5, 1])
#lw = 5*speed/speed.max()
#ax2.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)
plt.show()                          # 12-xMatplotlibExamples-figs: 09


# Demo of a basic pie chart, plus a few additional features:
# slice labels, auto-labeling percentage, offsetting a slice with "explode",
# drop-shadow, and custom start angle. 
#  Note about the custom start angle: The default "startangle" is 0, which
# would start the "Frogs" slice on the positive x-axis. This example sets
# "startangle = 90" such that everything is rotated counter-clockwise by 90
# degrees, and the frog slice starts on the positive y-axis.

# slices will be ordered and plotted counter-clockwise.
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0) # only "explode" the 2nd slice ('Hogs')
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.show()                          # 12-xMatplotlibExamples-figs: 10


# Demo of bar plot on a polar axis
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
ax = plt.subplot(111, polar=True)
bars = ax.bar(theta, radii, width=width, bottom=0.0)
for r, bar in zip(radii, bars): # use custom colors and opacity
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)
plt.show()                          # 12-xMatplotlibExamples-figs: 11


# Shaded relief plots demo (like Mathematica)
# cf. http://reference.wolfram.com/mathematica/ref/ReliefPlot.html
from matplotlib.colors import LightSource
X,Y = np.mgrid[-5:5:0.05,-5:5:0.05]
Z = np.sqrt(X**2+Y**2)+np.sin(X**2+Y**2)
ls = LightSource(azdeg=0,altdeg=65) # create light source object
rgb = ls.shade(Z,plt.cm.copper)     # shade data creating an RGB array
plt.figure(figsize=(12,5))          # plot un-shaded and shaded images
plt.subplot(121)
plt.imshow(Z,cmap=plt.cm.copper)
plt.title('imshow')
plt.xticks([]); plt.yticks([])
plt.subplot(122)
plt.imshow(rgb)
plt.title('imshow with shading')
plt.xticks([]); plt.yticks([])
plt.show()                          # 12-xMatplotlibExamples-figs: 12


# Pylab example: fill spiral
from pylab import *
theta = arange(0,8*pi,0.1)
a, b = 1, 0.2
for dt in arange(0,2*pi,pi/2.0):
    x = a*cos( theta+dt )*exp(b*theta)
    y = a*sin( theta+dt )*exp(b*theta)
    dt = dt+pi/4.0
    x2 = a*cos( theta+dt )*exp(b*theta)
    y2 = a*sin( theta+dt )*exp(b*theta)
    xf = concatenate( (x,x2[::-1]) )
    yf = concatenate( (y,y2[::-1]) )
    p1=fill(xf,yf)
show()                              # 12-xMatplotlibExamples-figs: 13


# 3D surface demo
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()                          # 12-xMatplotlibExamples-figs: 14


# 3D contour with 2D projections demo
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)
ax.set_xlabel('X')
ax.set_xlim(-40, 40)
ax.set_ylabel('Y')
ax.set_ylim(-40, 40)
ax.set_zlabel('Z')
ax.set_zlim(-100, 100)
plt.show()                          # 12-xMatplotlibExamples-figs: 15


##
##  END
##
