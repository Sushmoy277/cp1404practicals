try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1. If we  input any inappropriate value for example-any words,alphabets etc.
# 2. If we input 0 in the denominator.
# 3. Yes, we can .If we make the code to check if it's a 0 and after detecting if its ,it will print an error message.
