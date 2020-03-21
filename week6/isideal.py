def isIdeal(num):
    flag = 0
    while num != 1:
        if num%3 == 0:
            num /= 3
        elif num%5 == 0:
            num /= 5
        else:
            flag = 1
            break

    if flag == 1:
        return False
    else:
        return True


if __name__ == "__main__":

    print(1, 75)

    low = 400000
    high = 500000
    temp = 0
    count = 0
    for i in range(low, high+1):
        if temp == 0:
            if isIdeal(i):
                temp = i
                print(temp)
                count += 1
        elif temp != 0:
            print(i)
            if i%temp == 0:
                # print(i)
                count += 1
                temp = i