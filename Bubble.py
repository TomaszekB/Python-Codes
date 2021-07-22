def sort(list):
    x = len(list)

    while x > 1:
        change = False
        for i in range(0, x - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                change = True

        x -= 1
        print(list)
        if not change: break

    return list


sort([-18, 9, 3, 0, 4, -12])
