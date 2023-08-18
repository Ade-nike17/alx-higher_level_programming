#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_value = set()
    result = 0

    for num in my_list:
        if num not in uniq_value:
            result += num
            uniq_value.add(num)

    return result
