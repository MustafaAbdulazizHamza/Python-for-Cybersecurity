import os
import time
start = time.perf_counter()
files = [fi for fi in os.listdir() if '.txt' in fi]
for fi in files:
    no = int(fi.split(".")[0])
    if no < 10:
        no = f'00{no}'
    elif no < 100:
        no = f"0{no}"
    os.rename(fi, f"{no}-Lecture.txt")
end = time.perf_counter()
print(end - start)