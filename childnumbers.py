#!/usr/bin/env python

from multiprocessing import Process, Pool
import timeit

multiple_dict = {}

def generate_substrings(string):
    j = 1
    a = set()
    while True:
        for i in range(len(string) - j + 1):
            a.add(string[i:i+j])
        if j == len(string):
            break
        j += 1
    return a

def is_child_number(number):
    num_digits = len(str(number))
    num_multiples = 0
    if len(str(number)) in multiple_dict:
        multiples = multiple_dict[num_digits]
    else:
        multiples = [i for i in xrange(0, 9 * num_digits, num_digits)]
        multiple_dict[num_digits] = multiples
        
    child = False
    for multiple in multiples:
        num = str(number).count(str(multiple))
        if num == 0:
            pass
        elif num == 1:
            if not child:
                child = True
            else:
                return False
        else:
            return False
    return child

def calculate_range(low, high):
    num_children = 0
    for i in xrange(low, high):
        if is_child_number(i):
            num_children += 1
    print "between %d and %d\t: %d" % (low, high, num_children)
    
def do_job():
    processes = set()
    for i, x in enumerate(xrange(0, 10 ** 7, 10 ** 6)):
        low = i * 10 ** 7
        p = Process(target = calculate_range, args = (low, low + 999999))
        processes.add(p)
        p.start()
    
    for p in processes:
        p.join()
        
        
if __name__ == '__main__':
    print timeit.timeit(do_job, number = 1)
