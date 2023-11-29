import matplotlib.pyplot as plt

def visualize_firing_rate(i, f_rate):
    # Assuming you want to visualize the firing rate based on 'i'
    x_values = np.linspace(0, 120, 100)  # Adjust the range as needed
    y_values = [firing_rate(x) for x in x_values]

    plt.plot(x_values, y_values)
    plt.scatter(i, f_rate, color='red', label='Current Firing Rate')
    plt.xlabel('Input Current (pA)')
    plt.ylabel('Firing Rate (Hz)')
    plt.title('Firing Rate vs. Input Current')
    plt.legend()
    plt.grid(True)
    plt.show()
