def solution(N, number):
    # dp[k] : N을 k번 사용해서 만들 수 있는 숫자들의 집합
    dp = [set() for _ in range(9)]
    for k in range(1, 9):
        concatenated_num = int(str(N) * k)
        dp[k].add(concatenated_num)
        
        for i in range(1, k):
            j = k - i
            # dp[i]의 모든 수와 dp[j]의 모든 수를 조합
            for num1 in dp[i]:
                for num2 in dp[j]:
                    dp[k].add(num1 + num2)
                    dp[k].add(num1 - num2)
                    dp[k].add(num1 * num2)
                    if num2 != 0:
                        dp[k].add(num1 // num2)

        if number in dp[k]:
            return k
    return -1