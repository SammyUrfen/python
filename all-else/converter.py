def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def decimal_to_binary(decimal_num):
    # Convert to binary and pad with leading zeros for 32 bits
    return format(decimal_num if decimal_num >= 0 else (1 << 32) + decimal_num, '032b')

def twos_complement(binary_str):
    # Invert the bits
    inverted_bits = ''.join('1' if bit == '0' else '0' for bit in binary_str)
    # Convert to decimal, add 1, then convert back to binary
    decimal_value = int(inverted_bits, 2) + 1
    return format(decimal_value, '032b')

def main():
    number = input("Enter a number (binary or decimal): ")

    # Check if the number is binary (contains only '0' and '1')
    if all(char in '01' for char in number):
        # Binary input
        print("You entered a binary number.")
        choice = input("Choose an option:\n1. Convert to decimal\n2. Find 2's complement\nEnter 1 or 2: ")

        if choice == '1':
            decimal_value = binary_to_decimal(number)
            print(f"The decimal equivalent is: {decimal_value}")
        elif choice == '2':
            complement = twos_complement(number)
            print(f"The 2's complement is: {complement}")
        else:
            print("Invalid choice.")
    else:
        # Decimal input
        try:
            decimal_num = int(number)
            print("You entered a decimal number.")
            binary_value = decimal_to_binary(decimal_num)
            print(f"The binary equivalent (32-bit) is: {binary_value}")
        except ValueError:
            print("Invalid number format.")

if __name__ == "__main__":
    main()

