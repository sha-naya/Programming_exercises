list_x = [0,1,2,3,4,5,6,7,8,9,10]

def find_max(list):
    max_num = list[0]

    for i in list:
        if i >= max_num:
            max_num = i
    return max_num
max = find_max(list_x)
print(max)

def find_min(list):
    min_num = list[0]

    for i in list:
        if i <= min_num:
            min_num = i
    return min_num
min = find_min(list_x)
print(min)
