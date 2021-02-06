
from matplotlib import pyplot as plt
from prettytable import PrettyTable

# * Seaborn dependencies
import pandas as pd
import numpy as np
import seaborn as sns

# * Settings
show_matplotlib = False
show_seaborn = True

if (show_matplotlib == True):

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

    # showing plot
    plt.show()

    #?###############
    #* Scatter Plot #
    #?###############

    # values on the x axis
    x = [5, 2, 9, 4, 7, 6, 3, 1, 4, 11, 4, 4, 5]

    # values on the y axis
    y = [14, 3, 6, 9, 1, 3, 1, 2, 7, 8, 3, 4, 11]

    # make the actual scatter plot
    plt.scatter(x, y)

    # showing plot
    plt.show()

    #?###################
    #* Plot Customizing #
    #?###################

    # values on the x axis
    x = [5, 2, 9, 4, 7, 6, 3, 1, 4, 11, 4, 4, 5]

    # values on the y axis
    y = [14, 3, 6, 9, 1, 3, 1, 2, 7, 8, 3, 4, 11]

    # values on the x axis of second set
    x2 = [14, 3, 6, 9, 1, 3, 1, 2, 7, 8, 3, 4, 11]

    # values on the y axis of second set
    y2 = [5, 2, 9, 4, 7, 6, 3, 1, 4, 11, 4, 4, 5]

    # adjust the size of the plot
    plt.figure(figsize=(12, 8))

    # make the actual scatter plot
    plt.scatter(x, y, label="first set")

    # we do the scattering again to plot 2 different sets inside the same plot
    # Note that we used alpha to chagne the opacity of the plot
    plt.scatter(x2, y2, alpha=0.5, label="second set")

    # adjust the x and y label (side text)
    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')

    # adjust the plot title
    plt.title("2D map of x and y coordinates")

    # add a legend #?(depends on label in .scatter)
    plt.legend()

    # showing plot
    plt.show()

    #?####################
    #* Creating Subplots #
    #?####################

    # values on the x axis
    x = [5, 2, 9, 4, 7, 6, 3, 1, 4, 11, 4, 4, 5]

    # values on the y axis
    y = [14, 3, 6, 9, 1, 3, 1, 2, 7, 8, 3, 4, 11]

    # values on the x axis of second set
    x2 = [14, 3, 6, 9, 1, 3, 1, 2, 7, 8, 3, 4, 11]

    # values on the y axis of second set
    y2 = [5, 2, 9, 4, 7, 6, 3, 1, 4, 11, 4, 4, 5]

    # alternative way to chance the size of the plot
    fig = plt.figure(figsize=(12, 8))

    # we create a sublpot
    ax1 = plt.subplot2grid((2, 2), (0, 0))
    # make the actual scatter plot
    ax1 = plt.scatter(x, y, label="first set")
    # adjust the x and y label (side text)
    ax1 = plt.xlabel('X coordinate')
    ax1 = plt.ylabel('Y coordinate')
    # adjust the plot title
    ax1 = plt.title("2D map of x and y coordinates")

    # we create a sublpot
    ax2 = plt.subplot2grid((2, 2), (0, 1))
    # make the actual scatter plot
    ax2 = plt.scatter(x2, y2, label="second set")
    # adjust the x and y label (side text)
    ax2 = plt.xlabel('X coordinate')
    ax2 = plt.ylabel('Y coordinate')
    # adjust the plot title
    ax2 = plt.title("2D map of x and y coordinates")

    # make histogram for ax2
    ax2 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
    ax2 = plt.hist(y2)

    # showcase result
    fig.tight_layout()

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

if (show_seaborn == True):

    #?###################
    #* Seaborn data Vis #
    #?###################

    # set the style of sns
    sns.set_style('darkgrid')

    """
        * This are possible options to use for sns.set_style()
        ? darkgrid
        ? whitegrid
        ? dark
        ? white
        ? ticks
    """

    # load the student database we use for this examples
    df = pd.read_csv('data.csv')
    df.head()

    #?###############
    #* Scatter plot #
    #?###############

    # do scatter with as input x and y coordinates
    sns.scatterplot(x=df['math score'], y=df['reading score'])

    # show the actual plot
    plt.show()

    """
        * We can implement this using multiple ways:
        ? plt.figure(figsize = (9,6))
        ? sns.scatterplot(x = 'math score', y = 'reading score',data = df)
    """

    #?#######################
    #* Scatter plot extended#
    #?#######################

    # set the plot figure size
    plt.figure(figsize=(9, 6))

    # plot data labels x and y, data df, differentiate in gender and use alpha for opacity.
    sns.scatterplot(x='math score',
                    y='reading score',
                    hue='gender',
                    data=df,
                    alpha=0.8
                    )

    # show the actual plot
    plt.show()

    #?############
    #* Count Plot#
    #?############

    # set the plot figure size
    plt.figure(figsize=(9, 6))

    # plot countplot with x label and data df
    sns.countplot(x='race/ethnicity',
                  data=df
                  )

    # show the actual plot
    plt.show()

    #?###############
    #* Distance Plot#
    #?###############

    # set the plot figure size
    plt.figure(figsize=(9, 6))

    # plot distance plot with x data df, and kde false (don't show kde of the distribution)
    sns.distplot(x=df['math score'], kde=False)

    # show the actual plot
    plt.show()

    #?##############
    #* KDE plotting#
    #?##############

    # * KDE stands for Kernal Density Estimate, more information about it is available here:
    # ? https://mathisonian.github.io/kde/

    # set the plot figure size
    plt.figure(figsize=(9, 6))

    # Do a kernal density plot with data math score
    sns.kdeplot(x=df['math score'])

    # show the actual plot
    plt.show()

    #?#########################
    #* Regression scatter plot#
    #?#########################

    # set the plot figure size
    plt.figure(figsize=(9, 6))

    # this creates a scatter plot with a regression line. the regression line tells about the relationship between two points
    # x data = df(math score), y data = df(reading score), the scatter is set to pink, the line to red, we use somehow similar colours
    sns.regplot(x=df['math score'],
                y=df['reading score'],
                scatter_kws={'color': 'pink'},
                line_kws={'color': 'red'}
                )

    # show the actual plot
    plt.show()

    #?################################
    #* Subset regresiion scatter plot#
    #?################################

    # do a plot with x data, y data, making a gender based differentiaton
    # this method automaticly makes a regression line for every subset in the plot
    sns.lmplot(x='math score',
               y='reading score',
               hue='gender',
               data=df
               )

    # show the actual plot
    plt.show()

    #?#################
    #* Paired plotting#
    #?#################

    # * This kind of plot is somewhat harder --> what does it do?
    # ? It pairwise plots distrutions of a dataset with different methods
    # ? It does this in numeric columns
    # ? The input is the subsets of the data with columns you want to plot distributions in between

    # We do a pairplot with 3 different inputs (should result in 9 outputs)
    sns.pairplot(df[['math score',
                     'reading score',
                     'writing score']]
                 )

    # show the actual plot
    plt.show()
