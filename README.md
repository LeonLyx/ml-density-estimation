# Naive Probability Density Estimation
The aim of this project is to implement the **Naive Probability Density Estimation** algorithm and the code can be located in `naiveEst.py`. 

## Requirements
- Python 3.6+
- No external dependencies required

## Instructions
To run the program:
```
python naiveEst.py
```

## Overview
A set of data points is provided in `data.txt`:
1. The **first** row contains the metadata of the dataset
2. The metadata includes the **total number of data points** and the **expected dimension** for each data point, and both are separated using a comma (`,`)
3. Subsequent rows will reflect each data point in the dataset
4. Each row corresponds to a data point, where each dimension is separated using a space (`" "`)

A brief overview of the algorithm is as follows:
1. Specify the length of each edge for the hypercube, **h**, which denotes the desired boundary
2. Traverse through each data point in the dataset
3. For each data point, do a comparison on every dimension with the rest of the dataset
4. Count the total number of data points that are within the boundary of each data point
5. Based on the result in step 4, calculate the probability estimation for each data point

Based on the given dataset, the program will run the algorithm and compute the probability estimation for each data point. Once the program terminates, the output can be located in `output.txt`.

Each row contains the probability estimation for each data point in the dataset.