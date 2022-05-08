import math

def solution(progresses, speeds):
    completions = []
    answer = []
    
    for i in range(len(progresses)):
        completion = math.ceil((100 - progresses[i]) / speeds[i])
        completions.append(completion)
    
    temp = completions.pop(0)
    count = 1
    while completions:
        if temp >= completions[0]:
            count += 1
        else:
            answer.append(count)
            temp = completions[0]
            count = 1
    
        completions.pop(0)
    
    answer.append(count)
        
    return answer