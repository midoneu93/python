import statistics

example_list = [3, 5, 4, 6, 4, 87, 9, 7, 6, 3, 10]

mean = statistics.mean(example_list)
print(mean)

median = statistics.median(example_list)
print(median)

stdev = statistics.stdev(example_list)
print(stdev)

variance = statistics.variance(example_list)
print(variance)