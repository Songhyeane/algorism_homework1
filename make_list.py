import random

def make_random_list(end,start,len):
    list = []
    for i in range(0,len):
        list.append(random.randint(end,start))

    return list
