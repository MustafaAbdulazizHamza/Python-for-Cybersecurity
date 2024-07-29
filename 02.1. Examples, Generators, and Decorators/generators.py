# def funtion():
#     # Block of code
#     yield <value>
def readDict(dic):
    with open(dic, 'r') as d:
        for line in d:
            yield line.strip()
# for i in readDict("rockyou.txt"):
#     print(i)
