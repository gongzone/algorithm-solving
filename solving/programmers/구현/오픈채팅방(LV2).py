def solution(record):
    answer = []
    logs = []
    hash_map = {}
    
    for x in record:
        msg = x.split(' ')
        action = msg[0]
        user_id = msg[1]
        user_name = msg[2] if len(msg) >= 3 else ''
        
        if action == 'Enter':
            hash_map[user_id] = user_name
            logs.append((user_id, '들어왔습니다.'))
            
        if action == 'Leave':
            logs.append((user_id, '나갔습니다.'))
        
        if action == 'Change':
            hash_map[user_id] = user_name
            
    for user_id, action in logs:
        new_msg = f'{hash_map[user_id]}님이 {action}'
        answer.append(new_msg)
        
    return answer