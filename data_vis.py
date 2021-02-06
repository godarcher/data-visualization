
from matplotlib import pyplot as plt

###########
#HISTOGRAM#
###########

#values on the y axis
y = [14,3,6,9]

#plotting histogram
plt.hist(y)

#showing plot
plt.show()

##########
#BAR PLOT#
##########

#values on the x axis
x = [5, 2, 9, 4, 7]

#values on the y axis
y = [14,3,6,9,1]

#plotting bar
plt.bar(x,y)

#showing plot
plt.show()

###########
#LINE PLOT#
###########

#values on the x axis
x = [5, 2, 9, 4, 7]

#values on the y axis
y = [14,3,6,9,1]

#plotting line 
plt.plot(x,y)

#showing plot
plt.show()