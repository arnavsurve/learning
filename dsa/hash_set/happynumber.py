n = int(input("Enter a number: "))

past_nums = set()

status = True

while n != 1 and status == True:
    num = list(map(int, str(n)))
    n = 0
    
    for i in num:
        n += i **2

    if n not in past_nums:
        past_nums.add(n)
    else:
        status = False

print("n is a happy number: " + str(status))
