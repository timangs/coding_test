import collections

def solution(participant, completion):
    counter = collections.Counter(participant) - collections.Counter(completion)
    for k in counter.keys():
        return k