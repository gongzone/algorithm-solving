def extend_lock(lock, extent, new_scale):
    extended_lock = [[0] * new_scale for _ in range(new_scale)]
    
    for i in range(extent, new_scale - extent):
        for j in range(extent, new_scale - extent):
            extended_lock[i][j] = lock[i - extent][j - extent]
    
    return extended_lock

def rotate_key(key, key_length):
    rotated_key = [[0] * key_length for _ in range(key_length)]
    
    for i in range(key_length):
        rotated_key[i] = [key[j][i] for j in reversed(range(key_length))]
        
    return rotated_key

def check_lock(extended_lock, extent, new_scale):
    for i in range(extent, new_scale - extent):
        for j in range(extent, new_scale - extent):
            if extended_lock[i][j] != 1:
                return False
    
    return True

def solution(key, lock):
    lock_length = len(lock)
    key_length = len(key)

    extent = key_length - 1
    new_scale = lock_length + extent * 2
    extended_lock = extend_lock(lock, extent, new_scale)

    for i in range(new_scale - extent):
        for j in range(new_scale - extent):
            for _ in range(4):
                key = rotate_key(key, key_length)
                for x in range(key_length):
                    if i + x < extent or i + x > new_scale - extent:
                        continue
                    for y in range(key_length):
                        extended_lock[i + x][j + y] += key[x][y]

                if check_lock(extended_lock, extent, new_scale):
                    return True
                else:
                    for x in range(key_length):
                        for y in range(key_length):
                            extended_lock[i + x][j + y] -= key[x][y]

    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))
