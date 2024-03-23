import random
answer = random.randint(0,100)
ans = -1
tries = 0

while ans != answer:
    ans = input("Enter your guess:")
    ans = int(ans)
    if ans < answer:
        print("Answer is higher")
    elif ans > answer:
        print("Answer is lower")
    tries += 1
else:
    print("You win, the answer is:", answer,)
    print("You found it in",tries,"tries")