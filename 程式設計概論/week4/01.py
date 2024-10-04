for i in range(1, 10):
    ll = ""
    for j in range(1, 10):
        ll += str(i) + "x" + str(j) + "=" + (str(i*j) if len(str(i*j)) == 2 else " "+str(i*j)) + " "
    print(ll)