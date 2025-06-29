ap, ad = map(int, input().split())
bp, bd = map(int, input().split())

while True:
    if ad <= 0 and bd <= 0:
        print("DRAW")
        break
    elif ad <= 0:
        print("PLAYER B")
        break
    elif bd <= 0:
        print("PLAYER A")
        break
    else:
        ad -= bp
        bd -= ap