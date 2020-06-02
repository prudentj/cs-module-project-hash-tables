# Print out all of the numbers in the following array that are divisible by 3:
# [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# The expected output for the above input is:
# 27
# 81
# 8
# 27
# 99
# 63
# 42
# You may use whatever programming language you wish.
# Verbalize your thought process as much as possible before
# writing any code. Run through the UPER problem solving framework while going through your thought process.
practice_Arr = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# Iterate through the array
for item in practice_Arr:

    # If the element is divisible by 3 print is
    if item % 3 == 0:
        print(item)
