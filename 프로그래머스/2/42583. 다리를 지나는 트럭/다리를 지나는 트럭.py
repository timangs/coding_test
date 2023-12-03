import collections
def solution(bridge_length, weight, truck_weights):
    time_int = 0
    weight_now_list = collections.deque()
    weight_now_int = 0
    truck_weights.reverse()

    while len(truck_weights) != 0:
        time_int += 1

        if weight_now_list:
            if time_int == weight_now_list[-1][1]:
                weight_now_int -= weight_now_list[-1][0]
                weight_now_list.pop()

        if weight_now_int + truck_weights[-1] <= weight:
            weight_now_int += truck_weights[-1]
            weight_now_list.appendleft([truck_weights[-1],time_int+bridge_length])
            truck_weights.pop()

            
        #print(weight_now_list,truck_weights)


    return weight_now_list[0][1]