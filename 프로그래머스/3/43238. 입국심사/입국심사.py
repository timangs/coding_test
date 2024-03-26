def solution(n, times):
    times.sort()
    times_fast: int = times[0]
    time_min,time_max = times_fast,times_fast * n,
    
    def mid(max: int, min: int) -> int:
        return (max+min) // 2 
    
    while True:
        if time_max == time_min +1:
            break
        time_mid: int = mid(time_max,time_min)
        if sum([time_mid // time for time in times]) >= n:
            time_max = time_mid
        else:
            time_min = time_mid
        
    
    return time_max