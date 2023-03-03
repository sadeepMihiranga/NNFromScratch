inputs = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

bias = [2, 3, 0.5]

layers_output = []

for neuron_weights, neuron_bias in zip(weights, bias):
    neuron_output = 0
    for input_n, weight in zip(inputs, neuron_weights):
        neuron_output += input_n * weight # output of the neuron
    layers_output.append(neuron_output + neuron_bias) # output of current layer

print(layers_output)