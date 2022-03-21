number = input().split('-')
is_correct_length = 3 <= len(number) <= 4
is_all_digit = True * min([i.isdigit() for i in number])
is_correct_number = True if is_all_digit and ((number[0] == '7' and len(number[1]) == 3 and len(number[2]) == 3 and len(number[3]) == 4) or (len(number[0]) == 3 and len(number[1]) == 3 and len(number[2]) == 4)) else False
print('YES' if is_correct_length and is_correct_number else 'NO')
