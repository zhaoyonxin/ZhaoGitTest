import random
secret = random.randint(1, 10)
print(secret)
print('------------------学习python------------------')
temp = input('猜数字:')
guess = int(temp)
while guess != secret:
    temp = input('请重新猜数字:')
    guess = int(temp)
    if guess == secret:
        print('猜中了')
    else:
        if guess > secret:
            print("猜大了")
        else:
            print("猜小了")
        print('猜错哦')
print('游戏结束')