hilt_class = ["Jennifer", "Sally", "Sam", "Mary"]

for name in hilt_class:
    if name == "Sally":
            print(name)

states = {"MI": "Michigan", "ME": "Maine"}

for code, state in states.items():
    print(code + " is the code for " + state)

for i in range(10):
    print("I am at number " + str(i))

for i in range(5, 10):
    print("I'm at number " + str(i))

for i in range(0, 10, 12):
    print("I'm at number " + str(i))

fruits = ['sand', 'cardboard', 'mice', 'apple']

if fruits[0] == "apple":
    print("Yum!")
elif fruits[0] == "cardboard" or fruits[0] == "sand":
    print("Yuck!")

else:
    print("Not bad.")
