#74 - Basic neural network - simulate individual neurons and their connections.

#First Output
weight1_1 = None
weight2_1 = None

#Second Output
weight1_2 = None
weight2_2 = None

def Classify(input_1,input_2):
    output_1 = input_1 * weight1_1 + input_2 * weight2_1
    output_2 = input_1 * weight1_2 + input_2 * weight2_2
    if output_1 > output_2:
        return 0
    else:
        return 1

