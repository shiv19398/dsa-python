# Brute force solution
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    answer = []
    n = len(temperatures)

    for i in range(n):
        j = i + 1

        while j < n:
            if temperatures[j] > temperatures[i]:
                answer.append(j - i)
                break
            j += 1
        else:
            answer.append(0)

    return answer


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

# Optimized solution using stack
def dailyTemperaturesOptimized(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    
    answer = [0]* n

    stack = []

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            index = stack.pop()
            answer[index] = i - index
        stack.append(i)

    return answer

print(dailyTemperaturesOptimized([73, 74, 75, 71, 69, 72, 76, 73]))