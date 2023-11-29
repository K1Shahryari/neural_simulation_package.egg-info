def collect_u_w_values():
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

    return u, w