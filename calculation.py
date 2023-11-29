import numpy as np

def calculate_firing_rate():
    num_neurons = int(input("Enter the number of presynaptic neurons: "))
    u = []
    w = []

    for i in range(num_neurons):
        while True:
            u_i = float(input(f"Enter the subthreshold synaptic input (u) for neuron {i + 1} (in pA): "))
            if 0 <= u_i <= 120:
                break
            else:
                print("Invalid input! Subthreshold synaptic input must be between 0 and 120 pA.")
        u.append(u_i)

        while True:
            w_i = float(input(f"Enter the neuron weight (w) for neuron {i + 1} (must be between 0 and 1): "))
            if 0 <= w_i <= 1:
                break
            else:
                print("Invalid input! Weight must be between 0 and 1.")
        w.append(w_i)

    i = sum([u_i * w_i for u_i, w_i in zip(u, w)])
    i = min(i, 120)

    def firing_rate(i):
        if i < 40:
            return 0
        elif 40 <= i < 45:
            return 20 * (i - 40) / 5
        elif 45 <= i <= 120:
            return 20 + 10 * (i - 45) / 75
        else:
            return 30

    f_rate = firing_rate(i)

    print(f"The total subthreshold synaptic input (Tu) is: {i:.2f} pA")
    print(f"The firing rate F(I) is: {f_rate:.2f} Hz")

    if i >= 40:
        print("\033[32mPostsynaptic firing rate detected.\033[0m")
    else:
        print("\033[31mNo postsynaptic firing rate detected.\033[0m")

    return i, f_rate