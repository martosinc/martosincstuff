from numpy import exp, array, dot, random

training_set_inputs = array([[0,0,1],[1,1,0],[1,1,1],[0,0,0]])
training_set_outputs = array([[1,1,1,1]]).T

class NT():
    def __init__(self):
        random.seed(1)

        self.synaptic_weights = random.random((3,1)) 

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def __sigmoid_derivative(self, x):
        return x * (1-x)
    
    def train(self, training_set_inputs, training_set_outputs, num_of_training_iter):
        for iter in range(num_of_training_iter):
            output = self.think(training_set_inputs)

            error = training_set_outputs - output

            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))
            self.synaptic_weights += adjustment

    def think(self, inputs):
        return self.__sigmoid(dot(inputs, self.synaptic_weights))
q = NT()
print(q.synaptic_weights)
q.train(training_set_inputs,training_set_outputs, 100000)
print(q.synaptic_weights)
print(q.think(array([0,0,0])))