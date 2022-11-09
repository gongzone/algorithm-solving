def get_compressed_string(count, prev):
    temp = str(count) + prev if count >= 2 else prev
    return temp

def solution(s):
    answer = len(s)
    
    for num in range(1, len(s) // 2 + 1):
        prev = s[0:num]
        count = 1
        compressed_string = ''
        
        for i in range(num, len(s), num):
            now = s[i:i + num]
            
            if prev == now:
                count += 1
            else:
                compressed_string += get_compressed_string(count, prev)
                prev = now
                count = 1
        
        compressed_string += get_compressed_string(count, prev)
        answer = min(len(compressed_string), answer)
        
    return answer