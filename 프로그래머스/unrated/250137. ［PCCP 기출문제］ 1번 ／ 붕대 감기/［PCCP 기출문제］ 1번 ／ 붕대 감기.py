def solution(bandage, health, attacks):
    bandage_count_int = 0
    health_max_int = health
    attacks_timing_list = []
    attacks_damage_list = []
    attacks_count_int = 0
    
    for j in range(len(attacks)):
        attacks_timing_list.append(attacks[j][0])
        attacks_damage_list.append(attacks[j][1])

    for i in range(max(attacks)[0]+1):
        if i == 0:
            continue
        if i in attacks_timing_list:
            bandage_count_int = 0
            health -= attacks_damage_list[attacks_count_int]
            if health <= 0:
                return -1
            attacks_count_int += 1
        else:
            health += bandage[1]
            bandage_count_int += 1
            if bandage_count_int == bandage[0]:
                health += bandage[2]
                bandage_count_int = 0

            if health >= health_max_int:
                health = health_max_int
        #print(f'시간 {i} {health}') 

    return health