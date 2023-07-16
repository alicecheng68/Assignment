def calculate_sum_of_bonus(data):
    exchange_rate = 30
    employees = data["employees"]

    total_base = 0
    total_bonus = 0
    sum_total_bonus = 0

    for person in employees:
        name = person["name"]
        salary = person["salary"]
        performance = person["performance"]
        role = person["role"]

        if "USD" in salary:
            salary = float(salary.strip("USD")) * exchange_rate
        else:
            salary = float(salary.replace(",", ""))

        if salary >= 100000:
            salary_base = 0.13
        else:
            salary_base = 0.12

        if performance == "above average":
            performance_base = 0.12
        elif performance == "average":
            performance_base = 0.09
        else:
            performance_base = 0.09

        if role == "CEO":
            role_base = 0.05
        else:
            role_base = 0.11

        base = salary_base + performance_base + role_base
        total_base += base
        
    for person in employees:
        name = person["name"]
        salary = person["salary"]
        performance = person["performance"]
        role = person["role"]

        if "USD" in salary:
            salary = float(salary.strip("USD")) * exchange_rate
        else:
            salary = float(salary.replace(",", ""))

        if salary >= 100000:
            salary_base = 0.13
        else:
            salary_base = 0.12

        if performance == "above average":
            performance_base = 0.12
        elif performance == "average":
            performance_base = 0.09
        else:
            performance_base = 0.09

        if role == "CEO":
            role_base = 0.05
        else:
            role_base = 0.11

        base = salary_base + performance_base + role_base
        bonus = (8000 * base) / total_base
        total_bonus += bonus
        sum_total_bonus += bonus

        print(f"{name}: {int(bonus)}")

    print(f"Total Bonus: {int(sum_total_bonus)}")


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
