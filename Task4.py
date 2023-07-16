def get_number(index):
    n = [0]
    for i in range(1, index+1):
        if i % 2 == 1:
            n.append(n[i-1] + 4)  # 递增4
        else:
            n.append(n[i-1] - 1)  # 递减1
    result = n[-1]
    print(result)
    return result

get_number(1)   # 输出：4
get_number(5)   # 输出：10
get_number(10)  # 输出：15
