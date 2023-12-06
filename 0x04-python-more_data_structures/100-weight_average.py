#!/usr/bin/python3
def weight_average(my_list=[]):
    summtion = sum((x[0] * x[1]) for x in my_list)
    weights_sum = sum(x[1] for x in my_list)
    if weights_sum > 0:
        return summtion / weights_sum
    else:
        return 0
