# Problem: Decimal to binary number using recursion - https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

# Decimal to binary conversion
# using recursion
def dec_to_bin(d):
    if d == 0:
        return 0
    else:
        return (d % 2 + 10 * dec_to_bin(d // 2))

# Driver code 
d = 10
print(dec_to_bin(d))