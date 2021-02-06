
from matplotlib import pyplot as plt
from prettytable import PrettyTable

#?############
#* HISTOGRAM #
#?############

# values on the y axis
y = [14, 3, 6, 9]

# plotting histogram
plt.hist(y)

# showing plot
plt.show()

#?##########
#* BOX PLOT#
#?##########

# values on the y axis
y = [14, 3, 6, 9]

# plotting histogram
plt.boxplot(y)

# showing plot
plt.show()

#?###########
#* Bar Plot #
#?###########

# values on the x axis
x = [5, 2, 9, 4, 7]

# values on the y axis
y = [14, 3, 6, 9, 1]

# plotting bar
plt.bar(x, y)

# showing plot
plt.show()

#?############
#* Line Plot #
#?############

# values on the x axis
x = [5, 2, 9, 4, 7]

# values on the y axis
y = [14, 3, 6, 9, 1]

# plotting line
plt.plot(x, y)

# showing plot
plt.show()

#?############
#* Pie Chart #
#?############

# The labels are the names for the parts
label_set = '7', '6', '8+', '5-'

# we give each label a size
sizes = [20, 45, 15, 20]

# we use explode to show a particular slide
explode = (0, 0, 0, 0.1)

# subplots
fig1, ax1 = plt.subplots()

ax1.pie(sizes, explode=explode, labels=label_set,
        autopct='%1.1f%%', shadow=True, startangle=90)

# make sure its a circle
ax1.axis('equal')

# show the plot
plt.show()

#?###############
#* Scatter Plot #
#?################

# values on the x axis
x = [5, 2, 9, 4, 7, 6, 3, 1, 4, 11, 4, 4, 5]

# values on the y axis
y = [14, 3, 6, 9, 1, 3, 1, 2, 7, 8, 3, 4, 11]

# make the actual scatter plot
plt.scatter(x, y)

# show the plot
plt.show()


#?##############
#* prettytable #
#?##############

# specifying column names
mytable = PrettyTable(["Student Name", "Class", "Section", "Percentage"])

# adding rows
mytable.add_row(["Serra", "X", "B", "91.2%"])
mytable.add_row(["Penny", "B", "C", "61.2%"])
mytable.add_row(["Erik", "B", "B", "90.2%"])
mytable.add_row(["Josso", "X", "A+", "100%"])
mytable.add_row(["Luka", "X", "B", "88.1%"])

# output
print(mytable)

#?###################
#* testing comments #
#?###################

# the following section is for testing better comments
# TODO: Implement x and y
# ? This is a query
# * this is hightlighted, way better then the stupid plain default comments
# ! this is very important
