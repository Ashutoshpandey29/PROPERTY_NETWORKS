import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Define some data
labels = ['Apples', 'Bananas', 'Oranges', 'Peaches']
sizes = [20, 30, 25, 15]

# Create a figure and axis object
fig, ax = plt.subplots()

# Create the initial pie chart
pie_chart = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)


# Define the update function for the animation
def update(frame):
    # Generate new data
    new_sizes = [random.randint(0, 50) for i in range(4)]

    # Update the sizes of the pie slices
    for i, slice in enumerate(pie_chart[0]):
        slice.set_sizes([new_sizes[i]])

    # Return the updated artists
    return pie_chart


# Create the animation object
animation = FuncAnimation(fig, update, frames=10, interval=1000)

# Show the plot
plt.show()
