"""
피보나치 수열
- 동적계획법 Memorization
"""

input_num = 200
fibo_memory = {
    1: 1,
    2: 1,
}


# 리펙토링 전
def fibo_dynamic_programming(n):
    if n == 1 or n == 2:
        return 1
    if n not in fibo_memory.keys():
        if n - 1 in fibo_memory and n - 2 in fibo_memory:
            fibo_memory[n] = fibo_memory[n - 1] + fibo_memory[n - 2]
    else:
        return fibo_memory[n]
    return fibo_dynamic_programming(n - 1) + fibo_dynamic_programming(n - 2)


print(fibo_dynamic_programming(input_num))


fibo_memory_2 = {
    1: 1,
    2: 1,
}


# 리펙토링 후
def fibo_dynamic_programming_adv(n):
    if n in fibo_memory_2:
        return fibo_memory_2[n]
    nth_fibo = fibo_dynamic_programming_adv(n - 1) + fibo_dynamic_programming_adv(n - 2)
    fibo_memory_2[n] = nth_fibo
    return nth_fibo


print(fibo_dynamic_programming_adv(input_num))
