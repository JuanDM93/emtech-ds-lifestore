"""
Frontend module
"""
import os
from time import sleep
from .backend import                                    \
    clean_list, custom_sort, filter_categories,         \
    get_yearly, global_searches, sum_reviews,           \
    get_reviews, get_stocks, get_total_revenue,         \
    get_monthly, get_product, get_refunds, get_revenue, \
    SALES, DATES, CATEGORIES


# LOCALS
SLEEPING = 0.5
PRINT_SIZE = 10
SECRETS = ['admin', 'pass']

PROCESSES = ['globals', 'cats', 'date']
EXIT_CMDS = ['return', 'logout', 'exit']


def clear():
    """
    Clears screen
    """
    os.system('clear')


# Login
def login(limit: int = 3) -> bool:
    """
    auth starter function
    """
    def ask() -> tuple:
        """
        returns: user inputs (admin, secret)
        """
        admin = input('Input admin user: ')
        secret = input('Password: ')
        return (admin, secret)

    while True:
        (admin, secret) = ask()
        if admin != SECRETS[0] or secret != SECRETS[1]:
            limit -= 1
            print(f'Login failed... : {limit}\n')
        else:
            print('Login succesful!\n')
            sleep(SLEEPING)
            clear()
            # Start interface service
            interface()

        # Failed logout
        if limit == 0:
            print('... bye')
            return False


# Main Interface
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
    except ValueError:
        print(f'\nERROR: Input unavailable "{answer}"\n')
        answer = -1

    print(separator)
    sleep(SLEEPING)
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
#   Reports     #
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


# Date
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
            m = d[-1][1]
            if m not in months:
                months.append(m)
        months.sort()
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
    if len(date) == 2:
        result = get_monthly(SALES, date)
    elif len(date) == 4:
        result = get_yearly(SALES, date)
    else:
        result = []

    if len(result) > 0:
        print_sales(result)
        print_reviews(result)
        print_refunds(result)
        print_revenue(result)
        print_total_revenue(result)


# Globals
def ask_globals():
    """
    Prints global related data
    """
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
        print_sales(SALES)
    elif response == 1:
        print_searches()
    elif response == 2:
        print_reviews(SALES)
    elif response == 3:
        print_stocks()
    elif response == 4:
        print_refunds(SALES)
    elif response == 5:
        print_revenue(SALES)
        print_total_revenue(SALES)


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
    print_cat_searches(CATEGORIES[cat])
    print(separator)
    print_cat_reviews(CATEGORIES[cat])
    print(separator)
    print_cat_stocks(CATEGORIES[cat])


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
        print(f'Sales: {len(s[1])} - {product[3]} - {product[1]}')

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
        print(f'Sales: {len(s[1])} - {product[1]}')

    c_sale = filter_categories(sales, [categorie])

    print_total_revenue(c_sale)
    print_revenue(c_sale)

    print(f'\nMost sold {categorie}\n')
    c_most_sale = clean_list(custom_sort(c_sale))
    for s in c_most_sale:
        print_cat_sale(s)

    print(f'\nLeast sold {categorie}\n')
    c_least_sale = custom_sort(c_sale, False)
    for s in c_least_sale:
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
        print(f'Searches: {len(s[1])} - {product[3]} - {product[1]}')

    searches = global_searches()

    print(f'\n{PRINT_SIZE} most searched items\n')
    most = clean_list(custom_sort(searches))[:PRINT_SIZE]
    for s in most:
        print_search(s)

    print(f'\n{PRINT_SIZE} least searched items\n')
    least = custom_sort(searches, False)[:PRINT_SIZE]
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
        print(f'Searches: {len(s[1])} - {product[1]}')

    searches = global_searches()
    c_search = filter_categories(searches, [categorie])

    print(f'\nMost searched {categorie}\n')
    c_most_search = clean_list(custom_sort(c_search))
    for s in c_most_search:
        print_cat_search(s)

    print(f'\nLeast searched {categorie}\n')
    c_least_search = custom_sort(c_search, False)
    for s in c_least_search:
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
        print(f'Review: {r[1]:.2f} - {product[3]} - {product[1]}')

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


def print_cat_reviews(categorie):
    """
    Prints reviews data by categorie
    """
    def print_cat_review(r):
        """
        Review item print
        """
        product = get_product(r[0])
        print(f'Review: {r[1]:.2f} - {product[1]}')

    reviews = get_reviews(SALES)
    result = sum_reviews(reviews)

    c_review = filter_categories(result, [categorie])

    print(f'\nBest reviewed {categorie}\n')
    c_best_review = clean_list(custom_sort(c_review))
    for r in c_best_review:
        print_cat_review(r)

    print(f'\nWorst reviewed {categorie}\n')
    c_worst_review = clean_list(custom_sort(c_review, False))
    for r in c_worst_review:
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
        print(f'Stock: {s[1]} - {product[3]} - {product[1]}')

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
        print(f'Stock: {s[1]} - {product[1]}')

    stocks = get_stocks(SALES)
    c_stock = filter_categories(stocks, [categorie])

    print(f'\nHigh stock {categorie}\n')
    c_high_stock = clean_list(custom_sort(c_stock))
    for s in c_high_stock:
        print_cat_stock(s)

    print(f'\nLow stock {categorie}\n')
    c_low_stock = custom_sort(c_stock, False)
    for s in c_low_stock:
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
        print(f'Revenue: ${r[1]:10.2f} - {product[3]} - {product[1]}')


def print_total_revenue(data: list):
    """
    Prints total revenue for data list
    """
    revenue = get_total_revenue(data)
    print(f'\nTotal revenue: ${revenue:10.2f}\n')


# Refunds
def print_refunds(data: list):
    """
    Prints refund items data
    """
    print(f'\n{PRINT_SIZE} most refund items\n')
    refunds = get_refunds(data)
    refunds = clean_list(custom_sort(refunds))[:PRINT_SIZE]
    for r in refunds:
        product = get_product(r[0])
        print(f'Refunds: {r[1]} - {product[3]} - {product[1]}')
