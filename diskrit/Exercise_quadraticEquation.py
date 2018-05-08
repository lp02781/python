print ("Perhitungan akar-akar kuadrat persamaan Ax^2+Bx+C")
a = int (input ("masukkan nilai A:"))
b = int (input ("masukkan nilai B:"))
c = int (input ("masukkan nilai C:"))

if a == 0:
    kuad1 = (-c)/b
    print (kuad1)
else:
    kuad1 = (-b + (b**2 - 4*a*c)**(0.5))/2*a
    kuad2 = (-b - (b**2 - 4*a*c)**(0.5))/2*a
    print (kuad1, kuad2)
