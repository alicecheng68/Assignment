def func(*data):
    result = []
    for text in data:
        count = {}
        same = False
        for char in text:
            if char in count:
                same = True
                break
            same[char] = 1
        if not same:
            result.append(text)
    return result
    

func("彭大牆", "王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有

