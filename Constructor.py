class new:
    def __init__(self,x):
        print(id(x))
        print("Constructor Called")

obj = new(10)

# n number of constructor bana sakte hai pr last bala call hota hai automatiacally
