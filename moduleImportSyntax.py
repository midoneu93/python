from statistics import mean as me , median as med

#from statistics import *
#mean = mean(example_list)
#median = median(example_list)


example_list = [3, 5, 4, 6, 4, 87, 9, 7, 6, 3, 10]

mean = me(example_list)
median = med(example_list)

print(mean, "\n", median)