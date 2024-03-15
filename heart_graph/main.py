import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

e = np.e   # Euler
pi = np.pi # pi

# Equation to plot
def equation(x, e, pi, a):
    return x**(2/3) + (e/3 * (pi - x**2)**0.5) * np.sin(a * np.pi * x)

# Update function for animations
def update(a):
    y_vals1 = equation(x_vals, e, pi, a)
    y_vals2 = equation(-x_vals, e, pi, a)
    line1.set_ydata(y_vals1)
    line2.set_ydata(y_vals2)
    ax1.set_title(f'a = {a:.1f}')
    return line1, line2

# Create the figure and axes for the plot
fig, ax1 = plt.subplots()
fig.canvas.manager.set_window_title('Window 1')
ax2 = ax1.twinx()  # Create a secondary y-axis for mirrored values
ax1.set_xlim(-2, 2)
ax1.set_ylim(-1.5, 3)
ax2.set_ylim(-1.5, 3)

x_vals = np.linspace(-10, 10, 5000)
# Main Plot in blue
line1, = ax1.plot(x_vals, equation(x_vals, e, pi, 0), color='blue')
# Mirrowed plot in red
line2, = ax2.plot(x_vals, equation(-x_vals, e, pi, 0), color='red')

# Animate the graph with values of 'a' from 0 to 20 with 0.1 steps
animation = FuncAnimation(fig, update, frames=np.arange(0, 20, 0.1), interval=40)

# Show the plot
plt.show()
