def checkMagazine(magazine, note):
    mag = {}
    for token in magazine:
        if mag.get(token) == None:
            mag[token] = 1
        else:
            current = mag[token]
            current += 1
            mag[token] = current

    flag = True
    for token in note:
        if mag.get(token) == None or mag.get(token) <= 0:
            flag = False
            break
        else:
            current = mag.get(token)
            current -= 1
            mag[token] = current

    if flag:
        print("Yes")
    else:
        print("No")
