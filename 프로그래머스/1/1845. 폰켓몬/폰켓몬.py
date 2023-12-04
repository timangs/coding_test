def solution(nums):
    nums_set = set(nums)
    if len(nums)/2 <= len(nums_set):
        #print(nums)
        answer = int(len(nums)/2)
    else:
        #print(nums_set)
        answer = len(nums_set)
    return answer