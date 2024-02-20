# section of initialization
nums:list = [{2:[3,1,2,3]},{3:[3,3,3,2,2,4]},{2:[3,3,3,2,2,2]}]
    
def solution(nums:list)->int:
    # only even numbers are vaild by restriction number 2.
    maximum_len_of_args: int = len(nums)/2
    
    # construct a dictionary with list nums.
    dict_nums:dict = {}
    for index,value in enumerate(nums):
        dict_nums[index] = value
    
    # execting that part will run the code.
    selected_ponketmon: list = []
    for value in dict_nums.values():
        if value not in selected_ponketmon:
            selected_ponketmon.append(value)
    
    # section verifies that value stays within maximum length
    if len(selected_ponketmon) > maximum_len_of_args:
        answer:int = int(maximum_len_of_args)
    else:
        answer:int = len(selected_ponketmon)
        
    return answer
    

# section of execution
for element in nums:
    for key,value in element.items():
        result: int = solution(value)
        if result != key:
            print(f'{result} is not goal, {key}')
        else:
            print(f'{result} is goal')
