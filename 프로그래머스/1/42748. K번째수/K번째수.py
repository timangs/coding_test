def slicelist(param_list:list,start_int:int,end_int:int,find_int:int) -> int:
    return sorted(param_list[start_int-1:end_int])[find_int-1]

def solution(array, commands):
    answer = []
    for i,j,k in commands:
        answer.append(slicelist(array,i,j,k))
    return answer