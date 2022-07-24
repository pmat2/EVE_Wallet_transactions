import locale as lc
import time as t
from matplotlib import pyplot as plt

#local vars
filename = 'logs.txt'

types = ['Bounty Prizes',
'Bounty Prize Corporation Tax',
'ESS Escrow Payment',
'Market Escrow',
'Market Transaction',
'Transaction Tax', 
'Jumpgate Fee']

#currency setting
lc.setlocale(lc.LC_ALL, 'en_US.UTF-8')

def print_header():
    print("""
    /*************************\\
        Wallet logs fetcher

        Author: Zonnie
        Ver: 0.1
    \\*************************/""")
    pass

def print_options():
    print('''
    Avaliable wallet transaction types:
        1. %s
        2. %s
        3. %s
        4. %s
        5. %s
        6. %s
        7. %s
        8. Overall wallet graph
    ''' % (types[0], types[1], types[2], types[3], types[4], types[5], types[6]))
    pass

def format_date(current):
    c = current.split(' ')
    date = c[0].replace('-', '.')
    date = c[0].replace('/', '.')
    return date

def format_input_date(input):
    return input.replace('-', '.').replace('/', '.')

def parse_ISK(isk):
    return int(isk.replace(',', '').replace(' ISK', ''))

def print_supported_formats():
    print("""
        Supported formats:
        YYYY.MM.DD
        YYYY-MM-DD
        YYYY/MM/DD

        press <return> twice for no time bounds
    """)
    pass

def input_to_bool(input):
    return input.lower() == 'y'

def show_graph(list, header):
    plt.title(header) 
    plt.xlabel("Time") 
    plt.ylabel("ISK")
    plt.ticklabel_format(style='plain', useLocale=True)
    plt.plot(list)
    plt.show()
    pass

def show_all_transactions_graph(filename, header):
    vals = []
    with open(filename, 'r') as file:
        for r in file:
            fr = r.split('\t')
            vals.append(parse_ISK(fr[3]))
    vals = vals[::-1]
    show_graph(vals, header)
    pass

def print_all_logs(filename, input_type):
    sum = 0
    graph = input("Would you like to see that in graph?(y/n) ")
    graphb = input_to_bool(graph)
    vals = []
    print('No date set, fetching from entire file\n%s\n' % (input_type))
    with open(filename, 'r') as file:
        for r in file:
            fr = r.split('\t')
            date, type, isk = fr[0], fr[1], fr[2]
            if(type == input_type):
                print('Date: %s\tType: %s\tAmount: %s\t' % (date, type, isk))
                sum = sum + parse_ISK(isk)
                if(graphb):
                    vals.append(abs(parse_ISK(isk)))
    num = lc.currency(sum, grouping=True).replace('$', ' ISK')
    print('\nSum: ', num)
    if(graphb):
        vals = vals[::-1]
        show_graph(vals, input_type)
    pass

def print_logs(filename, input_type, dfrom, dto):
    sum = 0
    graph = input("Would you like to see that in graph?(y/n) ")
    graphb = input_to_bool(graph)
    vals = []
    print('%s from %s to %s\n' % (input_type, dfrom, dto))
    with open(filename, 'r') as file:
        for r in file:
            fr = r.split('\t')
            date, type, isk = fr[0], fr[1], fr[2]
            fd = format_date(date)
            if(fd >= dfrom and fd <= dto and type == input_type):
                print('Date: %s\tType: %s\tAmount: %s\t' % (date, type, isk))
                sum = sum + parse_ISK(isk)
                if(graphb):
                    vals.append(abs(parse_ISK(isk)))
    num = lc.currency(sum, grouping=True).replace('$', ' ISK')
    print('\nSum: ', num)
    if(graphb):
        vals = vals[::-1]
        show_graph(vals, input_type)
    pass

#context menu
def fetcher():
    #headers
    print_header()
    print_options()

    #option
    choice = input('Chose a transaction: ')
    try:
        int(choice)
    except:
        print('Wrong input type')
        return

    if(choice == '' or int(choice) < 0 or int(choice) > len(types)+1):
        print('No transaction type given, quitting program')
        return

    if(choice == '8'):
        show_all_transactions_graph(filename, "Wallet status")
        return

    chosen_type = types[int(choice)-1]
    print("Chosen type: ", chosen_type)

    #date
    print_supported_formats()
    date_bounds = [input('Date from: '), input('Date to: ')]
    if(date_bounds[0] > date_bounds[1]):
        print('Messed up dates? No problem!')
        date_bounds[0], date_bounds[1] = date_bounds[1], date_bounds[0]
    dfrom, dto = format_input_date(date_bounds[0]), format_input_date(date_bounds[1])

    #dated/undated
    if(dfrom == '' or dto == ''):
        print_all_logs(filename, chosen_type)
        return
    else:
        print_logs(filename, chosen_type, dfrom, dto)
        return

#magic
fetcher()
while(True):
    rerun = input('Re-run program?(y/n) ')
    if(rerun.lower() != 'y' and rerun.lower() == 'n'):
        break
    elif(rerun.lower() == 'y' and rerun.lower() != 'n'):
        fetcher()
    else:
        print('Invalid command')

print('\nWindow will close in 2 minutes')
t.sleep(120)