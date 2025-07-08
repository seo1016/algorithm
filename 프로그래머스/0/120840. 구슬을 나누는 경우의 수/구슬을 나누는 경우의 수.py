def solution(balls, share):
    def factorial(n):
        lst = list(range(1, n + 1))
        result = 1
        while lst:
            result *= lst.pop(0)
        return result
    return factorial(balls) // (factorial(share) * factorial(balls - share))
