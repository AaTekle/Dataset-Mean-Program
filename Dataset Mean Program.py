#stat modules
import statistics

#2 of the datasets
dataSet1 = [1, 3, 6, 9, 12, 15, 18, 21]
dataSet2 = [1, 4, 8, 12, 16, 20, 24, 28]

#Mean Calculations, with Variable names
M = statistics.mean(dataSet1)
N = statistics.mean(dataSet2)

#Messages printed to the terminal
print("The mean of dataSet1:", M)
print("The mean of dataSet2:", N)