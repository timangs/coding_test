import re

def solution(phone_book):
    answer = True
    phone_book.sort() # String Sort의 특성을 생각해야한다.
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]: # String sort를 했으므로 다음꺼만 확인한다.
            return False
    return answer
# 혼자 못풀었다. https://kid-do-developer.tistory.com/80 참고하였음.