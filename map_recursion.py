

# def map_r(function, l):
#     # if i == len(l) - 1:
#     #     print "if statement ran" 
#     #     l[i] == function(l[i])
#     if not l:
#         return []
#     else:
#         return [function(l[0])] + (map_r(function, l[1:]))
#         # map_r(function, l[len(l) - 2])
        

# print map_r(lambda x: x*2, [1,2,3,4])

def filter_r(function, l):
    if not l:
        return []
    else:
        if function(l[0]):
            return [l[0]] + filter_r(function, l[1:])
        else:
            return filter_r(function, l[1:])

print filter_r(lambda x: x%2 == 0, [1, 2, 3, 4, 5, 6])

# def reduce_r(function, l):
#     # if len(l) == 2:
#     #     return function(l[-1], reduce(function, l[-2])
#     # else:
#     if len(l) == 0:
#         return []
#     else:
#         reduce_r(function, l[:len(l)-1])

# print reduce_r(lambda x,y: x*y, [2,3,4])