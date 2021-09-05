"""
Frontend module
"""
import os
from time import sleep
from .backend import *


# LOCALS
SLEEPING = 1
PRINT_SIZE = 10
SECRETS = ['admin', 'pass']

PROCESSES = ['globals', 'cats', 'date']
EXIT_CMDS = ['return', 'logout', 'exit']
CATEGORIES = get_categories()
DATES = get_dates()

SALES = global_sales()


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


# Main Interfece
def interface():
    """
    Prints report options
    """
    while True:
        separator = '++++++++++\n'
        print(separator)
        print('Hey, what would you like to do?\n')

        response = ask_option(PROCESSES)
        # Process case selector
        print(separator)
        if len(response) > 0:
            response = response[0]
            if response > len(PROCESSES):
                print(
                    f'ERROR: Sorry, process [{response}] - "{PROCESSES[response]}" - not yet available\n')
                sleep(SLEEPING)
            else:
                print(f'INFO: Running "{PROCESSES[response]}" process\n')
                sleep(SLEEPING)
                report(response)
        else:
            print(f'WARNING: No valid option selected\n')
            sleep(SLEEPING)
        print(separator)
        clear()


def exit_status(answer: list) -> bool:
    """
    Checks exit command behaviour
    """
    answer = answer[0]
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


def ask_option(options: list) -> list:
    """
    Asks unique option value
    """
    response = print_options(options)
    while len(response) > 1:
        sleep(SLEEPING)
        clear()
        response = [options[r] for r in response]
        response = print_options(response)
    return response


def print_options(options: list) -> list:
    """
    options: ids list
    returns: response ids list
    """
    separator = '**********\n'
    print(separator)
    print('Select option by indices:\n')

    size = len(options)
    options = [(i, options[i]) for i in range(size)]
    for o in options:
        print(f'{o[0]}: {o[-1]}')
    for e in EXIT_CMDS:
        print(f'"{e}"": {e}')

    answer = input('answer: ')

    valids = []
    errors = [[], []]
    answer = answer.split(',')
    if len(answer) == 1:
        if exit_status(answer):
            return answer
    for a in answer:
        try:
            a = int(a)
            if a < 0 or a > size - 1:
                errors[0].append(a)
                continue
        except ValueError:
            if a not in EXIT_CMDS:
                errors[1].append(a)
            continue
        valids.append(a)

        print(separator)
        for e in errors[1]:
            print(f'ERROR: Wrong input "{e}"\n')

        for w in errors[0]:
            print(f'WARNING: "{w}"" is not a valid option\n')
        sleep(SLEEPING)

    print(separator)
    result = []
    for v in valids:
        if v not in result:
            result.append(v)
    return result


#################
#   Reports     #
#################


def report(process_id: int = 0):
    """
    reports logic
    """
    def wait_input():
        # Return
        input('\nInput anything to return\n')
        clear()
    if process_id == 0:
        print('- Globals -\n')
        ask_globals()
        wait_input()
    elif process_id == 1:
        print('- Categories -\n')
        ask_cats()
        wait_input()
    elif process_id == 2:
        print('- Dates -\n')
        # ask_date()
        wait_input()
    else:
        print('- Unknown -\n')
        wait_input()


# Globals
def ask_globals():
    """
    Prints global related data
    """
    print('This is a global report\n')
    separator = '-------------------\n'
    options = [
        'sales', 'searches', 'reviews',
        'stock', 'refunds', 'revenue',
    ]

    response = print_options(options)[0]
    print(separator)
    if response == 0:
        print_sales()
    elif response == 1:
        print_searches()
    elif response == 2:
        print_reviews()
    elif response == 3:
        print_stocks()
    elif response == 3:
        print_refunds()
    elif response == 4:
        print_revenue()


# Cats
def ask_cats():
    """
    Prints categorie filtered data
    """
    print('This is a categorie report\n')
    separator = '-------------------\n'
    cat = print_options(CATEGORIES)[0]

    # Cat report
    print(separator)
    print_cat_sales(CATEGORIES[cat])
    print(separator)
    print_cat_searches(CATEGORIES[cat])
    print(separator)
    print_cat_reviews(CATEGORIES[cat])
    print(separator)
    print_cat_stocks(CATEGORIES[cat])


# Sales
def print_sales():
    """
    Prints sales data
    """
    def print_sale(s):
        """
        Sale item print
        """
        product = get_product(s[0])
        print(f'Sales: {len(s[1])} - {product[3]} - {product[1]}')

    print(f'{PRINT_SIZE} most sold items\n')
    most = custom_sort(SALES)[:PRINT_SIZE]
    for s in most:
        print_sale(s)

    print(f'\n{PRINT_SIZE} least sold items\n')
    least = custom_sort(SALES, False)[:PRINT_SIZE]
    for s in least:
        print_sale(s)


def print_cat_sales(categorie):
    """
    Prints sales data by categorie
    """
    def print_cat_sale(s):
        """
        Cat sale item print
        """
        product = get_product(s[0])
        print(f'Sales: {len(s[1])} - {product[1]}')

    c_sale = filter_categories(SALES, [categorie])

    print(f'Most sold {categorie}\n')
    c_most_sale = custom_sort(c_sale)
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
    
    print(f'{PRINT_SIZE} most searched items\n')
    most = custom_sort(searches)[:PRINT_SIZE]
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

    print(f'Most searched {categorie}\n')
    c_most_search = custom_sort(c_search)
    for s in c_most_search:
        print_cat_search(s)

    print(f'\nLeast searched {categorie}\n')
    c_least_search = custom_sort(c_search, False)
    for s in c_least_search:
        print_cat_search(s)


# Reviews
def print_reviews():
    """
    Prints reviews data
    """
    def print_review(r):
        """
        Review item print
        """
        product = get_product(r[0])
        print(f'Review: {r[1]:.2f} - {product[3]} - {product[1]}')

    reviews = get_reviews(SALES)

    result = []
    for r in reviews:
        if len(r[1]) > 0:
            review = sum(r[1]) / len(r[1])
            result.append([r[0], review])

    print(f'Best {PRINT_SIZE} reviewed items\n')
    best = custom_sort(result)[:PRINT_SIZE]
    for r in best:
        print_review(r)

    print(f'\nWorst {PRINT_SIZE} reviewed items\n')
    worst = custom_sort(result, False)[:PRINT_SIZE]
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

    result = []
    for r in reviews:
        if len(r[1]) > 0:
            review = sum(r[1]) / len(r[1])
            result.append([r[0], review])

    c_review = filter_categories(result, [categorie])

    print(f'Best reviewed {categorie}\n')
    c_best_review = custom_sort(c_review)
    for r in c_best_review:
        print_cat_review(r)

    print(f'\nWorst reviewed {categorie}\n')
    c_worst_review = custom_sort(c_review, False)
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

    print(f'{PRINT_SIZE} high stock items\n')
    h_stocks = custom_sort(stocks)[:PRINT_SIZE]
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

    print(f'High stock {categorie}\n')
    c_high_stock = custom_sort(c_stock)
    for s in c_high_stock:
        print_cat_stock(s)

    print(f'\nLow stock {categorie}\n')
    c_low_stock = custom_sort(c_stock, False)
    for s in c_low_stock:
        print_cat_stock(s)


# Revenue
def print_revenue():
    """
    Prints revenue per item data
    """
    print(f'{PRINT_SIZE} most revenue per item\n')
    revenue = get_revenue(SALES)
    revenue = custom_sort(revenue)[:PRINT_SIZE]
    for r in revenue:
        product = get_product(r[0])
        print(f'Revenue: ${r[1]:10.2f} - {product[3]} - {product[1]}')


# Refunds
def print_refunds():
    """
    Prints refund items data
    """
    print(f'{PRINT_SIZE} most refund items\n')
    refunds = get_refunds(SALES)
    refunds = custom_sort(refunds)[:PRINT_SIZE]
    for r in refunds:
        product = get_product(r[0])
        print(f'Refunds: {r[1]} - {product[3]} - {product[1]}')
