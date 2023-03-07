def solution(number):
    num = 0
    if number >= 0:
        for i in range(number):
            if i % 3 == 0 or i % 5 == 0:
                num += i
        return num
    else:
        return 0


print(solution(10))
