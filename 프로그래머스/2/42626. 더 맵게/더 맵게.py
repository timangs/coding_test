import heapq

def solution(scoville, K):
    heap_scoville = []
    tried_count = 0
    for i in scoville:
        heapq.heappush(heap_scoville,i)

    def mixed_foods(heap_scoville,tried_count):
        tried_count += 1
        mixed_food = heapq.heappop(heap_scoville) + (heapq.heappop(heap_scoville) * 2)
        return mixed_food, tried_count

    while heap_scoville[0] < K:
        if len(heap_scoville) == 1:
            tried_count = -1
            break
        mixed_food, tried_count = mixed_foods(heap_scoville,tried_count)
        heapq.heappush(heap_scoville,mixed_food)

    return tried_count