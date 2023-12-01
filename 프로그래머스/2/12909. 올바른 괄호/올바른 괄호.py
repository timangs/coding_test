def solution(s):
    answer = True
    open_count_int = 0
    close_count_int = 0

    
    for i in list(s):
        if close_count_int > open_count_int:
            answer = False
        if i == "(":
            open_count_int += 1
        if i == ")":
            close_count_int += 1
    
    if open_count_int == close_count_int:
        if list(s)[0] == ")":
            answer = False
    else:
        answer = False
    return answer
