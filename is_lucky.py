def main():
    '''
    This app ask you a ticket number and shows is it lucky or not
    '''
    # get a ticket number
    number = str(input('Enter ticket number (ex. 000000): '))

    # checking recived variable length (it could only contain 6 numbers)
    if len(number) != 6:
        main()
    else:

        # compare sum of first 3 numbers and sum of last 3 numbers
        if sum(list(map(int, number[0:3]))) == sum(list(map(int, number[3:]))):
            print("Счастливый")
        else:
            print("Обычный")

if __name__ == '__main__':
    main()
