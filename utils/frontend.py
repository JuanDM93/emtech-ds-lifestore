"""
Frontend module
"""
import os
from time import sleep
from .backend import                                    \
    clean_list, custom_sort, filter_categories,         \
    get_yearly, sum_reviews, get_reviews, get_stocks,   \
    get_total_revenue, get_monthly, get_product,        \
    get_refunds, get_revenue,                           \
    SALES, SEARCHES, DATES, CATEGORIES


# LOCALS
SLEEPING = 0.5
PRINT_SIZE = 10
ADMINS = [['admin', 'pass'], ]

PROCESSES = ['globals', 'cats', 'date']
EXIT_CMDS = ['return', 'logout', 'exit']

MONTHS = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC',
]


#################
#   Interface   #
#################


def clear():
    """
    Clears screen
    """
    os.system('clear')


# Login
def login(limit: int = 3):
    """
    auth starter function
    """
    def ask() -> tuple:
        """
        returns: user inputs (user, password)
        """
        user = input('Input username: ')
        password = input('Password: ')
        return (user, password)

    def print_login(limit=-1):
        """
        prints login result
        """
        if limit >= 0:
            print(f'Login failed... : {limit}\n')
        else:
            print('Login succesful!\n')
        sleep(SLEEPING)
        clear()

    while limit > 0:
        (user, password) = ask()
        for admin in ADMINS:
            if admin[0] == user and admin[-1] == password:
                print_login()
                # Start interface service
                interface()
        limit -= 1
        print_login(limit)

    # Failed logout
    print('... bye')


# Main
def interface():
    """
    Prints report options
    """
    while True:
        separator = '++++++++++'
        print(separator)
        print('\nHey, what would you like to do?\n')
        response = print_options(PROCESSES)

        # Process
        if response >= 0:
            print(separator)
            print(f'\nINFO: Running "{PROCESSES[response]}" process\n')
            sleep(SLEEPING)
            report(response)
            clear()


def print_options(options: list) -> int:
    """
    options: ids list
    returns: response id
    """
    separator = '**********'
    print(separator)
    print('\nSelect option:\n')

    size = len(options)
    options = [(i, options[i]) for i in range(size)]
    for o in options:
        print(f'{o[0]}: {o[-1]}')
    print()
    for e in EXIT_CMDS:
        print(f'"{e}"')

    answer = input('\nanswer: ')
    if exit_status(answer):
        return len(options) + 1
    print(separator)
    try:
        answer = int(answer)
        if answer < 0 or answer > size - 1:
            print(f'\nWARNING: "{answer}" is not a valid option\n')
            answer = -1
    except ValueError:
        print(f'\nERROR: Input unavailable "{answer}"\n')
        answer = -1

    print(separator)
    sleep(SLEEPING)
    clear()
    return answer


def exit_status(answer: str) -> bool:
    """
    Checks exit command behaviour
    """
    if answer == EXIT_CMDS[-1]:
        exit()
    else:
        if answer == EXIT_CMDS[1]:
            clear()
            login()
            return True
        if answer == EXIT_CMDS[0]:
            clear()
            interface()
        return False


#################
#    Reports    #
#################


def report(process_id: int = 0):
    """
    reports logic
    """
    def wait_input():
        """
        Return
        """
        input('\nInput anything to return\n')
        clear()

    if process_id == 0:
        print('\n- Globals -\n')
        ask_globals()
        wait_input()
    elif process_id == 1:
        print('\n- Categories -\n')
        ask_cats()
        wait_input()
    elif process_id == 2:
        print('\n- Dates -\n')
        ask_dates()
        wait_input()
    else:
        print('\n- Unknown -\n')
        wait_input()


# Globals
def ask_globals():
    """
    Prints global related data
    """
    def print_cat_global(data: list, process: str):
        """
        Prints ordered categories summary
        """
        print('\nThis is a categories summary\n')
        for d in custom_sort(data):
            if process == 'reviews':
                print(f'--- {d[-1]:.2f} {d[0]} avg {process}---\n')
            elif process == 'revenue':
                print(f'--- $ {d[-1]:10.2f} {d[0]} {process}---\n')
            else:
                print(f'--- {d[-1]} {d[0]} {process} ---\n')

    separator = '-------------------'
    options = [
        'sales', 'searches', 'reviews',
        'stock', 'refunds', 'revenue',
    ]
    response = print_options(options)
    while response < 0 or response > len(options):
        clear()
        response = print_options(options)

    print('\nThis is a global report\n')
    print(separator)
    if response == 0:
        print_total_revenue(SALES)
        print_sales(SALES)

        results = []
        for c in CATEGORIES:
            c_sales = filter_categories(SALES, c)
            result = [len(s[-1]) for s in c_sales]
            results.append([c, sum(result)])
        print_cat_global(results, options[response])

    elif response == 1:
        print_searches()

        results = []
        for c in CATEGORIES:
            c_search = filter_categories(SEARCHES, c)
            result = [len(s[-1]) for s in c_search]
            results.append([c, sum(result)])
        print_cat_global(results, options[response])

    elif response == 2:
        print_reviews(SALES)

        results = []
        for c in CATEGORIES:
            c_reviews = filter_categories(SALES, c)
            result = sum_reviews(get_reviews(c_reviews))
            avg = [r[-1] for r in result if r[-1] > 0]
            results.append([c, (sum(avg) / len(avg))])
        print_cat_global(results, options[response])

    elif response == 3:
        print_stocks()

        results = []
        for c in CATEGORIES:
            c_stocks = filter_categories(SALES, c)
            result = [r[-1] for r in get_stocks(c_stocks)]
            results.append([c, sum(result)])
        print_cat_global(results, options[response])

    elif response == 4:
        print_refunds(SALES)

    elif response == 5:
        print_total_revenue(SALES)
        print_revenue(SALES)

        results = []
        for c in CATEGORIES:
            c_revenue = filter_categories(SALES, c)
            result = [r[-1] for r in get_revenue(c_revenue)]
            results.append([c, sum(result)])
        print_cat_global(results, options[response])


# Cats
def ask_cats():
    """
    Prints categorie filtered data
    """
    separator = '-------------------'

    cat = print_options(CATEGORIES)
    while cat < 0 or cat > len(CATEGORIES):
        clear()
        cat = print_options(CATEGORIES)

    # Cat report
    print(f'\nThis is a categorie report: {CATEGORIES[cat]}\n')
    print(separator)
    print_cat_sales(SALES, CATEGORIES[cat])
    print(separator)
    print_cat_reviews(SALES, CATEGORIES[cat])
    print(separator)
    print_cat_searches(CATEGORIES[cat])
    print(separator)
    print_cat_stocks(CATEGORIES[cat])
    print(separator)
    print_refunds(filter_categories(SALES, CATEGORIES[cat]))


# Dates
def ask_dates():
    """
    Prints date related data
    """
    def print_date(dates):
        """
        Single report printer
        """
        separator = '-------------------'
        response = print_options(dates)
        while response < 0 or response > len(dates):
            clear()
            response = print_options(dates)
        print(f'\nThis is a {dates[response]} date report\n')
        print(separator)
        print_dates(dates[response])

    options = ['month', 'year']
    response = print_options(options)
    while response < 0 or response > len(options):
        clear()
        response = print_options(options)

    if response == 0:
        months = []
        for d in DATES:
            m = int(d[-1][1]) - 1
            if m not in months:
                months.append(m)
        months.sort()
        months = [MONTHS[m] for m in months]
        print_date(months)
    elif response == 1:
        years = []
        for d in DATES:
            y = d[-1][-1]
            if y not in years:
                years.append(y)
        years.sort(reverse=True)
        print_date(years)


def print_dates(date: str):
    """
    Prints data by month
    """
    if len(date) == 4:
        result = get_yearly(SALES, date)
        if len(result) > 0:
            print_total_revenue(result)
            print_date_cat(result)
            results = []
            for i in range(len(MONTHS)):
                m = MONTHS[i]
                monthly = get_monthly(result, m)
                results.append([m, [r[-1] for r in get_revenue(monthly)]])
            print(' * Monthly revenue * \n')
            for r in custom_sort(results):
                print(f'--- {r[0]}: $ {sum(r[-1]):}---\n')
    else:
        result = get_monthly(SALES, date)
        if len(result) > 0:
            print_total_revenue(result)
            print_date_cat(result)


def print_date_cat(data: list):
    """
    Prints date report per categorie
    """
    print('\n ** Categories revenue ** \n')
    results = []
    for c in CATEGORIES:
        c_sales = filter_categories(data, c)
        results.append([c, [s[-1] for s in get_revenue(c_sales)]])
    for r in custom_sort(results):
        print(f'--- $ {sum(r[-1]):10.2f}: {r[0]}---\n')


# Sales
def print_sales(sales: list):
    """
    Prints sales data
    """
    def print_sale(s):
        """
        Sale item print
        """
        product = get_product(s[0])
        print(f'{len(s[1])} - {product[3]} - {product[1]}')

    print(f'\n{PRINT_SIZE} most sold items\n')
    most = clean_list(custom_sort(sales))[:PRINT_SIZE]
    for s in most:
        print_sale(s)

    print(f'\n{PRINT_SIZE} least sold items\n')
    least = custom_sort(sales, False)[:PRINT_SIZE]
    for s in least:
        print_sale(s)


def print_cat_sales(sales, categorie):
    """
    Prints sales data by categorie
    """
    def print_cat_sale(s):
        """
        Cat sale item print
        """
        product = get_product(s[0])
        print(f'{len(s[1])} - {product[1]}')

    c_sale = filter_categories(sales, categorie)

    print_total_revenue(c_sale)
    print_revenue(c_sale)

    print(f'\nMost sold {categorie}\n')
    c_most_sale = clean_list(custom_sort(c_sale))
    for s in c_most_sale:
        print_cat_sale(s)


# Searches
def print_searches():
    """
    Prints searches data
    """
    def print_search(s):
        """
        Search item print
        """
        product = get_product(s[0])
        print(f'{len(s[1])} - {product[3]} - {product[1]}')

    print(f'\n{PRINT_SIZE} most searched items\n')
    most = clean_list(custom_sort(SEARCHES))[:PRINT_SIZE]
    for s in most:
        print_search(s)

    print(f'\n{PRINT_SIZE} least searched items\n')
    least = custom_sort(SEARCHES, False)[:PRINT_SIZE]
    for s in least:
        print_search(s)


def print_cat_searches(categorie):
    """
    Prints searches data by categorie
    """
    def print_cat_search(s):
        """
        Cat search item print
        """
        product = get_product(s[0])
        print(f'{len(s[1])} - {product[1]}')

    c_search = filter_categories(SEARCHES, categorie)

    print(f'\nMost searched {categorie}\n')
    c_most_search = clean_list(custom_sort(c_search))
    for s in c_most_search:
        print_cat_search(s)


# Reviews
def print_reviews(data: list):
    """
    Prints reviews data
    """
    def print_review(r):
        """
        Review item print
        """
        product = get_product(r[0])
        print(f'{r[1]:.2f} - {product[3]} - {product[1]}')

    reviews = get_reviews(data)
    result = sum_reviews(reviews)

    print(f'\nBest {PRINT_SIZE} reviewed items\n')
    best = clean_list(custom_sort(result))[:PRINT_SIZE]
    for r in best:
        print_review(r)

    print(f'\nWorst {PRINT_SIZE} reviewed items\n')
    worst = clean_list(custom_sort(result, False))[:PRINT_SIZE]
    for r in worst:
        print_review(r)


def print_cat_reviews(data: list, categorie: str):
    """
    Prints reviews data by categorie
    """
    def print_cat_review(r):
        """
        Review item print
        """
        product = get_product(r[0])
        print(f'{r[1]:.2f} - {product[1]}')

    reviews = get_reviews(data)
    result = sum_reviews(reviews)

    c_review = filter_categories(result, categorie)

    print(f'\nBest reviewed {categorie}\n')
    c_best_review = clean_list(custom_sort(c_review))
    for r in c_best_review:
        print_cat_review(r)


# Stocks
def print_stocks():
    """
    Prints stocks data
    """
    def print_stock(s):
        """
        Stock print
        """
        product = get_product(s[0])
        print(f'{s[1]} - {product[3]} - {product[1]}')

    stocks = get_stocks(SALES)

    print(f'\n{PRINT_SIZE} high stock items\n')
    h_stocks = clean_list(custom_sort(stocks))[:PRINT_SIZE]
    for s in h_stocks:
        print_stock(s)

    print(f'\n{PRINT_SIZE} low stock items\n')
    l_stocks = custom_sort(stocks, False)[:PRINT_SIZE]
    for s in l_stocks:
        print_stock(s)


def print_cat_stocks(categorie):
    """
    Prints stock data by categorie
    """
    def print_cat_stock(s):
        """
        Stock print
        """
        product = get_product(s[0])
        print(f'{s[1]} - {product[1]}')

    stocks = get_stocks(SALES)
    c_stock = filter_categories(stocks, categorie)

    print(f'\nHigh stock {categorie}\n')
    c_high_stock = clean_list(custom_sort(c_stock))
    for s in c_high_stock:
        print_cat_stock(s)


# Revenue
def print_revenue(data: list):
    """
    Prints revenue per item in data list
    """
    print(f'\n{PRINT_SIZE} most revenue per item\n')
    revenue = get_revenue(data)
    revenue = clean_list(custom_sort(revenue))[:PRINT_SIZE]
    for r in revenue:
        product = get_product(r[0])
        print(f'${r[1]:10.2f} - {product[3]} - {product[1]}')


def print_total_revenue(data: list):
    """
    Prints total revenue for data list
    """
    revenue = get_total_revenue(data)
    print(f'\nTotal revenue: ${revenue:10.2f}')


# Refunds
def print_refunds(data: list):
    """
    Prints refund items data
    """
    print('\nMost refund items\n')
    refunds = get_refunds(data)
    refunds = clean_list(custom_sort(refunds))
    for r in refunds:
        product = get_product(r[0])
        print(f'{r[1]} - {product[3]} - {product[1]}')
