def createHashTable(completion):
    hash_dict = {}
    for x in completion:
        if hash(x) in hash_dict:
            hash_dict[hash(x)] += 1
        else:
            hash_dict[hash(x)] = 1
    return hash_dict
        

def solution(participant, completion):
    hash_table = createHashTable(completion)
    answer = ''
    
    for x in participant:
        if hash(x) in hash_table:
            hash_table[hash(x)] -= 1
            if hash_table[hash(x)] < 0:
                answer = x
                break
            continue
        else:
            answer = x
            break
    
    return answer