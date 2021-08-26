def main():
    '''
    This app is coding string from "aaaabbb" to "a4b3"
    '''

    code, result, count = str(input()) + ' ', '', 1

    for i in range(len(code) - 1):
        # counting the same letters
        if code[i] == code[i + 1]:
            count += 1
        else:
            # write the result to variable
            result += '{}{}'.format(code[i], count)
            count = 1

    print(result)

if __name__ == '__main__':
    main()
