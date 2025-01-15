print(not True)
print(not False)
print(not 7) # False because 7 is True

print(True or False)
print(True and False)
print(2 or 3 or 4) # at which step did you know this is true (2); first true-like value
print(False or 0 or 4 or True)
print(1 and 2 and 3) # for AND it is always last True or first False
print(1 and 0.0 and 4) # first misstep
print(False or 0 or None) # for OR it can still be saved till the last one