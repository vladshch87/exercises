white_rook_letter = str(input())
white_rook_number = int(input())
black_rook_letter = str(input())
black_rook_number = int(input())

if white_rook_letter not in 'ABCDEFGH' or black_rook_letter not in 'ABCDEFGH':
    print('Недопустимая буква')
elif str(white_rook_number) not in '12345678' or str(black_rook_number) not in '12345678':
    print('Недопустимое число')
else:
    if white_rook_letter == black_rook_letter and white_rook_number == black_rook_number:
        print('Координаты не должны быть одинаковыми!')
    elif white_rook_letter == black_rook_letter or white_rook_number == black_rook_number:
        print('Yes')
    else:
        print('No')

