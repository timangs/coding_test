def solution(name:list, yearning:list, photos:list) -> list:
    name_year_dict: dict = {}
    for i in range(len(yearning)):
        name_year_dict[name[i]] = yearning[i]
    
    answer = []
    for photos_index in range(len(photos)):
        tmp: int = 0
        for names_in_photo in photos[photos_index]:
            try:
                tmp += name_year_dict[names_in_photo]
            except:
                pass
        answer.append(tmp)
    
    
    return answer