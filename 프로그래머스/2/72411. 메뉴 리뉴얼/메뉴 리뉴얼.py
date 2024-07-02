from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        course_menu = dict()
        max_c = []
        for order in orders:
            menu = combinations(list(order), c)
            for m in menu:
                temp = "".join(sorted(m))
                if course_menu.get(temp):
                    course_menu[temp] += 1
                else: 
                    course_menu[temp] = 1
        for k, v in course_menu.items():
            if v == max(course_menu.values()) and v >= 2:
                max_c.append(k)
        answer.extend(max_c)
    return sorted(answer)