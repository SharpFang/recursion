def reverse_string(s):
    if not s:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


input_str = "tiger"
output_str = reverse_string(input_str)
print(output_str)