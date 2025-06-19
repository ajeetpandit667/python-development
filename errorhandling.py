a = int(input("Enter a number: "))
print(f"Multiplication table of {a} is:")
try:
    for i in range(1, 11):
        print(f"{a} x {i} = {a * i}")
except Exception as e:
    print("An error occurred:", e)