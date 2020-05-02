"""
    Parameters
    -----------
    target_index : int
        index of row to be evaluated
    data_dim : int
        number of dimensions for each data row
    hypercube_h : float
        allowable distance between each datapoint, for N dimensions
    data_set : float[][]
        complete set of data
    
    Returns
    -------
    number_of_matches : int
        number of matches for a given row, inclusive of itself
"""
def calcProbabilityDensity(target_index, data_dim, hypercube_h, data_set):
    evaluate_set = [[elem for elem in curr_row] for curr_index, curr_row in enumerate(data_set) if target_index != curr_index]
    for curr_dim in range(data_dim):
        temp_set = []
        for curr_row in evaluate_set:
            u = (data_set[target_index][curr_dim] - curr_row[curr_dim]) / hypercube_h

            if abs(u) < 0.5:
                temp_set.append(curr_row)
        evaluate_set = temp_set
    
    number_of_matches = len(evaluate_set) + 1
    return number_of_matches

# file configurations
data_file = "data.txt"
output_file = "output.txt"
temp_output_file = "tmp.txt"





# parameter configurations
hypercube_h = 2.0

data_list = open(data_file, "r", encoding="utf-8").readlines()
# meta info and dataset
data_size, data_dim = [int(meta) for meta in str(data_list[0]).split(",")]
data_set = [[float(col) for col in str(data_list[line]).split(" ")] for line in range(1, len(data_list))]

output_set = list()
# output probability density
for target_index in range(len(data_set)):
    matches = calcProbabilityDensity(target_index, data_dim, hypercube_h, data_set)
    probability = (1 / (pow(hypercube_h, data_dim) * data_size)) * matches
    output_set.append("{:.2}\n".format(probability))

open(temp_output_file, "w", encoding="utf-8").writelines(output_set)
















