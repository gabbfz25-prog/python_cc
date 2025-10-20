# 2-7. Stripping Names:
# Use a variable to represent a person's name, and include some whitespace characters at the beginning and 
# end of the name. Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed. 
# Then print the name using each of the three stripping functions, Istrip(), rstrip(), and strip().

person_name = "   \n  Gabriel    "
print(f"Primer print: {person_name}")
person_name = "\t-\t-Gabriel-\t-"
print(f"Segundo print: {person_name}")
person_name = "\n\tGabriel\tFernadez"
print(f"Tercer print: {person_name}")

print(f"left strip:{person_name.lstrip()}")
print(f"right strip:{person_name.rstrip()}")
print(f"strip:{person_name.strip()}")

name = "\tGabriel Fernandez\n"

print("Unmodified:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())