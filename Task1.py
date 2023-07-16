
def find_and_print(messages):
    adult=[]
    for a, b in messages.items():
      if "18 years old" in b or "legal age" in b or "vote" in b:
          adult.append(a)

    for name in adult: 
        print(name)


find_and_print({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
})


