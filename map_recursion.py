

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

# def filter_r(function, l):
#     if not l:
#         return []
#     else:
#         if function(l[0]):
#             return [l[0]] + filter_r(function, l[1:])
#         else:
#             return filter_r(function, l[1:])

# print filter_r(lambda x: x%2 == 0, [1, 2, 3, 4, 5, 6])

# def reduce_r(function, l):
#     if len(l) == 1:
#         return l[0]
#     else:
#         return function(reduce_r(function, l[:-1]),l[-1])


def custom_bubble_sort(alist):
    sort_made = True
    while sort_made == True:
        sort_made = False
        for i in range(1, len(alist)):
            if alist[i] < alist[i - 1]:
                print alist
                temp = alist[i]
                alist[i] = alist[i - 1]
                alist[i - 1] = temp
                sort_made = True
                print alist, "\n"

    return alist

print custom_bubble_sort([10, 2, 3, 5, 7, 15, 1])

print custom_bubble_sort(['cat', 'llama', 'albatross', 'elephant', 'emu'])