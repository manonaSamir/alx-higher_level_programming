#!/usr/bin/python3
def weight_average(my_list=[]):
    summtion = sum((x[0] * x[1]) for x in my_list)
    weights_sum = sum(x[1] for x in my_list)
    return summtion / weights_sum
