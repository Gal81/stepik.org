import datetime

def main():
    # date = '2016 4 20'
    date = input()
    # days = 14
    days = int(input())
    yyyy, mm, dd = date.split(' ')
    date = datetime.date(int(yyyy), int(mm), int(dd))
    date_next = date + datetime.timedelta(days=days)

    yyyy, mm, dd = str(date_next).split('-')
    print(f'{int(yyyy)} {int(mm)} {int(dd)}')

if __name__ == '__main__':
    main()