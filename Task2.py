def calculate_sum_of_bonus(data):
    exchangerate=30
    employees= data["employees"]
    total_bonus = 0
    
    
    for people in employees:
        a=people["name"]
        b=people["salary"]
        c=people["performance"]
        d=people["role"]

        if "USD" in b:
            b=float(b.strip("USD"))*exchangerate
        else:
            b=float(b.replace(",",""))

        if c=="above average":
            c_base=1.0
        elif c=="average":
            c_base=0.8
        else:
            c_base=0.5

        if d=="CEO":
            d_base=0.7
        else:
            d_base=0.5

        bonus=b * 0.1 * c_base * d_base
        total_bonus += bonus
        print(f"{a}:{bonus}")
 print(f"Total Bonus: {total_bonus}")        

# write down your bonus rules in comments
# your code here, based on your own rules

calculate_sum_of_bonus({ 
    "employees":[
        {
        "name":"John",
        "salary":"1000USD", 
        "performance":"above average", 
        "role":"Engineer"
        }, 
        {
            "name":"Bob", 
            "salary":60000, 
            "performance":"average", 
            "role":"CEO"
        }, 
        {
            "name":"Jenny", 
            "salary":"50,000", 
            "performance":"below average", 
            "role":"Sales"
        } 
    ]
}) 