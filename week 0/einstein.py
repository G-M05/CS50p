def squared():
    c = int(300000000)
    return c * c


m = int(input("m: "))

E = int(m * squared())

print(f"E: {E:,}")