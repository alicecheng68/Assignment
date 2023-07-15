def get_number(index):

        n=[0]
        for i in range(1,index):
            if i % 2 == 1:

                n.append(n[i-1] + 4)  # 遞增4
            else:
                n.append(n[i-1] - 1)  # 遞減1
        return n
print(get_number(index[-1]))



get_number(1)   # 輸出: 4
get_number(5)   # 輸出: 10
get_number(10)  # 輸出: 15

