PyramidHeight = int(input("Pyramid Height : "))
StarNumber = 1
for i in range(PyramidHeight):
    print(" " * (PyramidHeight - i) + "*" * StarNumber)
    StarNumber += 2
