def func(*data):
    count = {}
    middle_names = []
    

    for name in data:
        words = name.split("：")
        middle_name = name[1] 
        middle_names.append(middle_name)
        count[middle_name] = count.get(middle_name, 0) + 1
    

    for full_name, middle_name in zip(data, middle_names):
        if count[middle_name] == 1:
            print(full_name)
            return

    print("沒有")
    
func("彭大牆", "王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
