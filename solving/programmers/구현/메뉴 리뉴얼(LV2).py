from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    menu_comb = []
    
    for course_num in course:
        for order in orders:
            print(list(combinations(order, course_num)))

    return answer