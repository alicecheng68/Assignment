def calculate_sum_of_bonus(data):
    exchange_rate = 30
    employees = data["employees"]
    total_bonus = 8000
    total_base = 0
    
    for person in employees:
        name = person["name"]
        salary = person["salary"]
        performance = person["performance"]
        role = person["role"]
        
        if "USD" in salary:
            salary = float(salary.strip("USD")) * exchange_rate
        else:
            salary = float(salary.replace(",", ""))
        
        if salary >=100000:
            salary_base = 0.16
        else:
            salary_base = 0.12
    
        if performance == "above average":
            performance_base = 0.12
        elif performance == "average":
            performance_base = 0.09
        else:
            performance_base = 0.09
         
        if role == "CEO":
            role_base = 0.08
        else:
            role_base = 0.11
        
        base = salary_base + performance_base + role_base
        total_base += base
        base_per = total_base / base
        bonus = total_bonus * base_per
        
        print(f"{name}: {bonus}")
    
    print(f"Total Bonus: {total_bonus}")
        

calculate_sum_of_bonus({ 
    "employees": [
        {
            "name": "John",
            "salary": "1000USD", 
            "performance": "above average", 
            "role": "Engineer"
        },
        {
            "name": "Bob", 
            "salary": "60000", 
            "performance": "average", 
            "role": "CEO"
        },
        {
            "name": "Jenny", 
            "salary": "50,000", 
            "performance": "below average", 
            "role": "Sales"
        } 
    ]
})
