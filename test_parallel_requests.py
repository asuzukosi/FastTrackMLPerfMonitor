import threading


def say_numbers():
    for i in range(0, 10):
        print(f"number : {i}")
        

threads = []
for i in range(0, 10):
    pass