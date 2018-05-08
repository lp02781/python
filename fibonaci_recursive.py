def fib1(angka):
    kump_fibo=[0,1]
    if angka<=1:
        return kump_fibo[angka]
    else:
        for index in range (angka):
            kump_fibo.append(kump_fibo[index-1]+kump_fibo[index-2])
    return kump_fibo[angka]

print(fib1(2))
