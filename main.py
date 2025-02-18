"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra + rb
    

def longest_run(mylist, key):
    curr = 0
    max = 0

    for i in mylist:
        if i == key:
            curr += 1
            if curr > max:
                max = curr
        else:
            curr = 0
    return max


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    return longest_run_recursive_code(mylist, key)[2]

def longest_run_recursive_code(mylist, key):
    if len(mylist) == 0:
        return (0, 0, 0)
    elif len(mylist) == 1:
        if mylist[0] == key:
            return (1, 1, 1)
        else:
            return (0, 0, 0)

    mid_val = len(mylist) // 2
    l_list = mylist[:mid_val]
    r_list = mylist[mid_val:]
    left = longest_run_recursive_code(l_list, key)
    right = longest_run_recursive_code(r_list, key)

    if left[0] != mid_val:
        left_run = left[0]
    else:
        left_run = left[0] + right[0]

    if right[1] != len(mylist) - mid_val:
        right_run = right[1]
    else:
        right_run = right[1] + left[1]


    mid_longest_run = left[1] + right[0] if (mylist[mid_val - 1] == key and mylist[mid_val] == key) else 0

    longest_run = max(left[2], right[2], mid_longest_run)

    return (left_run, right_run, longest_run)



