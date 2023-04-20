num=float (input ("Enter a number: ") )
if num>0:
    print (f"The input number {num} is positive")
else:
    print (f"The input number {num} is negative")
ref_number = float (input ("Enter a reference number: "))
if num>ref_number:
    print (f" {num} is on the right-hand side of the number {ref_number}")
else:
    print (f" {num} is on the left-hand side of the number {ref_number}")
