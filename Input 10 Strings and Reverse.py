lst = []
def stringGrab():
    for x in range (10):
        ele = input("Input string")
        lst.append(ele)
    res = [x[::-1] for x in lst]
    print('OG List:', lst)
    print('Reversed list:', res)

stringGrab()
