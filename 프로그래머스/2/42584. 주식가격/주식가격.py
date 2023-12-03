def solution(prices):
    answer = [0 for i in range(len(prices))]

    for i,j in enumerate(prices):
        count_int = 0
        for k in range(i,len(prices)-1):
            if j <= prices[k]:
                count_int += 1
            else:
                break
        answer[i] = count_int
                


    return answer

    return answer