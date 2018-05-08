Input = input("Input: ")
find = input("find: ")
i = 0
for kata in Input.split():
    if (kata == find):
        i += 1
print(i)

