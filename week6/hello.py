from cs50 import get_string

num: str = 12
answer: int = get_string("What's your name? ")
print("hello, " + answer)
print(f"hello, {answer}")
print(f"num = {num}")