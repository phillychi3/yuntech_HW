def input_lol():
    top = float(input("TTT"))
    bottom = float(input("BBB"))
    height = float(input("HHH"))

    if top < 0 or bottom < 0 or height < 0:
        print("lol")
        input_lol()
    else:
        print("梯形的面積為", (top + bottom) * height / 2)


input_lol()
