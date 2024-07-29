import os
for i in range(0, 1000):
    with open(f"{i}.file.txt", "w") as f:
        f.write("data " * i)
    