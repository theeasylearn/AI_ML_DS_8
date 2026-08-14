def getMean(list):
    total = 0
    for item in list:
        # print(item)
        total = total + item 
    average = total / len(list)
    # print(total,average)
    return average
def getVariance(list,average):
    deviation = [] #empty list 
    for item in list:
        difference = item - average
        deviation.append(difference)
    # print(deviation)
    square = []
    total = 0
    for item in deviation:
        temp = item * item 
        total = total + temp
        square.append(temp)
    population_variance = total / len(list)
    population_variance = round(population_variance,2)
    sample_variable = total / (len(list) - 1)
    sample_variable = round(sample_variable,2)
    # print(square,total,population_variance,sample_variable)
    return population_variance,sample_variable

def getCovariance(list1, list2):
    mean1 = getMean(list1)
    mean2 = getMean(list2)
    total = 0

    for i in range(len(list1)):
        deviation1 = list1[i] - mean1
        deviation2 = list2[i] - mean2
        total = total + (deviation1 * deviation2)

    population_covariance = total / len(list1)
    sample_covariance = total / (len(list1) - 1)

    return round(population_covariance, 2), round(sample_covariance, 2)