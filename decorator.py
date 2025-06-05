def decorator(func):
    def wrapper(x):
        ans = func(x)
        return ans*2
    return wrapper

@decorator

def suare(num):
    return num*num


ans = suare(2 )

print(ans)

     
