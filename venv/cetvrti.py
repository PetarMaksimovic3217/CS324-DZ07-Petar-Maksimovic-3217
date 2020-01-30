arr1 = [1, 2, 3, 4]
arr2 = [1, 2, 3]

try:
    if len(arr1) == len(arr2):
        print ("OK")
    else:
        raise RuntimeError()
        print ("nije OK")

except RuntimeError:
        print ("Liste su razlicitih duzina!")