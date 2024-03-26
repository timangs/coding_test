def solution(answers):
    result = []
    case_1 = [(i % 5) + 1 for i in range(len(answers))]
    case_2 = [2 if i % 2 == 0 else [1, 3, 4, 5][(i // 2) % 4] for i in range(len(answers))]
    case_3 = [(lambda i: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][i % 10])(i) for i in range(len(answers))]

    case_1_score,case_2_score,case_3_score = 0,0,0

    for i,v in enumerate(answers):
        if v == case_1[i]:
            case_1_score += 1
        if v == case_2[i]:
            case_2_score += 1
        if v == case_3[i]:
            case_3_score += 1

    score = [case_1_score,case_2_score,case_3_score]
    print(score)

    if score[0] == max(score):
        result.append(1)
    if score[1] == max(score):
        result.append(2)
    if score[2] == max(score):
        result.append(3)
    return result