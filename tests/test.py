from .context import cs613_hw4
import numpy as np


def print_node_weights(label, nodes):
    for i in xrange(len(nodes)):
        node = nodes[i]
        print "{0}_{1} Weights: {2}".format(label, i, node.weights)


def print_network_weights(neural_net):
    print "Hidden Weights: {0}".format(neural_net.hidden_weights)

    print_node_weights("Output", neural_net.output_nodes)


def test_multi_inputs(neural_net):
    print "Testing Multiple Inputs"
    inputs = np.array([[1, 2, 2], [2, 2, 2], [1, 3, 3], [2, 2, 2]])
    expected_output = np.array([[1], [0], [1], [0]])

    neural_net.train_binary(inputs, expected_output)

    print "Final Weights"
    print_network_weights(neural_net)

    print "Evaluating Test Data"
    print neural_net.forward_propagate(np.array([[2, 2, 2, 2], [1, 2, 2, 1]]))


def test_single_input(neural_net):
    print "Testing Single Input"
    inputs = np.array([[1, 2, 2, 1]])
    expected_output = np.array([[1]])

    neural_net.train_binary(inputs, expected_output)

    print "Final Weights"
    print_network_weights(neural_net)

    print "Evaluating Test Data"
    print neural_net.forward_propagate(np.array([[2, 2, 2, 2], [1, 2, 2, 1]]))


def setup_network():
    num_inputs = 3
    num_hidden_nodes = 4
    learning_rate = 1.0
    return cs613_hw4.ann.BatchANN(num_inputs, num_hidden_nodes, learning_rate)


if __name__ == "__main__":
    a_neural_net = setup_network()

    #test_single_input(a_neural_net)
    #print ""
    test_multi_inputs(a_neural_net)