import collections

def solution(clothes):
    clothes_counter_dict = collections.Counter(clothes[x][1] for x in range(len(clothes)))
    clothes_counter_list = []
    for i in clothes_counter_dict.values():
        clothes_counter_list.append(i+1)
    result = 1
    for i in range(len(clothes_counter_list)-1,-1,-1):
        result *= clothes_counter_list[i]
    return result -1