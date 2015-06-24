import random
def foo(s1, s2):
    inner = []
    outer = []
    for x in s1+s2:
        if x in s1 and x in s2:
            inner.append(x)
            outer.append(x)
        elif x in s1:
            outer.append(x)
    
    print "inner :", ''.join(inner)
    print "outer :", ''.join(outer) 


def bar(diff):
    nums = [random.randint(1,25) for i in range(10)]
    print nums
    result = []
    for i, x in enumerate(nums):
        for y in nums[i:]:
            if x-y == diff:
                result.append((x,y))
    
    print result