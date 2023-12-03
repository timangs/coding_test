def solution(priorities, location):
    round = 0
    count = 1
    while True:
        if round > len(priorities)-1:
            round = 0
        #print(priorities[round] , max(priorities))
        if priorities[round] == max(priorities):
            if round == location:
                break
            else:
                priorities[round] = 0
                count += 1
                #print(round,'pop')
        round += 1
    return count