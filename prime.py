num = int(input())
if num > 1:
    for i in range(2, int(num / 2)):
        if num % i == 0:
            print("Not Prime")
            break

    else:
        print("Prime")
else:
    print(num, "Not a prime Number")

