'''
This app ask you a ticket number and shows is it lucky or not
'''
def main():
    number = str(input('Enter ticket number (ex. 000000): '))

    if len(number) != 6:
        main()
    else:
        if sum(list(map(int, number[0:3]))) == sum(list(map(int, number[3:]))):
            print("Счастливый")
        else:
            print("Обычный")

if __name__ == '__main__':
    main()
