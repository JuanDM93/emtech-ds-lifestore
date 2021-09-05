"""
Frontend module
"""
import os
from time import sleep
from .backend import *


# LOCALS
SLEEPING = 1
SECRETS = ['admin', 'pass']
EXIT_CMDS = ['return', 'logout', 'exit']
PROCESSES = ['globals',]
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


# Report interfece
def interface():
    """
    Prints report options
    """
    while True:
        separator = '++++++++++\n'
        print(separator)
        print('Hey, what would you like to do?\n')
        response = print_options(PROCESSES)

        # Ask main option
        while len(response) > 1:
            sleep(SLEEPING)
            clear()
            response = [PROCESSES[r] for r in response]
            response = print_options(response)

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
        sleep(SLEEPING)

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
        input('Input anything to return\n')
        clear()
    if process_id == 0:
        print('- Globals -\n')
        ask_globals()
        wait_input()
    else:
        print('- Unknown -\n')
        wait_input()


# Globals
def ask_globals():
    print('This is a global report\n')
    separator = '-------------------\n'
    print(separator)
    print_sales()
    print(separator)
    print_searches()
    print(separator)
    print_reviews()
    print(separator)
    print_stocks()
    print(separator)
    print_refunds()
    print(separator)
    print_revenue()


# Sales
def print_sales():    
    print('Total most sold items\n')
    most = custom_sort(SALES)[:10]
    for s in most:
        product = get_product(s[0])
        print(f'Sales: {len(s[1])} - {product[3]} - {product[1]}')
    
    print('\nLeast sold items per cat')
    for c in CATEGORIES:
        c_sale = filter_categories(SALES, [c])
        c_sale = custom_sort(c_sale, False)[:10]
        print(f'\n- Cat: {c}\n')
        for s in c_sale:
            product = get_product(s[0])
            print(f'Sales: {len(s[1])} - {product[1]}')


# Searches
def print_searches():
    searches = global_searches()
    
    print('Most searched items\n')
    most = custom_sort(searches)[:10]
    for s in most:
        product = get_product(s[0])
        print(f'Searches: {len(s[1])} - {product[3]} - {product[1]}')

    print('\nLeast searched items per cat')
    for c in CATEGORIES:
        c_search = filter_categories(searches, [c])
        c_search = custom_sort(c_search, False)[:10]
        print(f'\n- Cat: {c}\n')
        for s in c_search:
            product = get_product(s[0])
            print(f'Searches: {len(s[1])} - {product[1]}')


# Reviews
def print_reviews():
    reviews = get_reviews(SALES)
    
    result = []
    for r in reviews:
        if len(r[1]) > 0:
            review = sum(r[1]) / len(r[1])
            result.append([r[0], review])
    
    print('Best reviewed items\n')
    best = custom_sort(result)[:10]
    for r in best:
        product = get_product(r[0])
        print(f'Review: {r[1]:.2f} - {product[3]} - {product[1]}')

    print('\nWorst reviewed items\n')
    worst = custom_sort(result, False)[:10]
    for r in worst:
        product = get_product(r[0])
        print(f'Review: {r[1]:.2f} - {product[3]} - {product[1]}')


# Stocks
def print_stocks():
    stocks = get_stocks(SALES)

    print('High stock items\n')
    h_stocks = custom_sort(stocks)[:10]
    for s in h_stocks:
        product = get_product(s[0])
        print(f'Stock: {s[1]} - {product[3]} - {product[1]}')

    print('\nLow stock items\n')
    l_stocks = custom_sort(stocks, False)[:10]
    for s in l_stocks:
        product = get_product(s[0])
        print(f'Stock: {s[1]} - {product[3]} - {product[1]}')


# Refunds
def print_refunds():
    print('Most refunds items\n')
    refunds = get_refunds(SALES)

    refunds = custom_sort(refunds)[:10]
    for r in refunds:
        product = get_product(r[0])
        print(f'Refunds: {r[1]} - {product[3]} - {product[1]}')


# Revenue
def print_revenue():
    print('Most revenue per item\n')
    revenue = get_revenue(SALES)
    revenue = custom_sort(revenue)[:10]
    for r in revenue:
        product = get_product(r[0])
        print(f'Revenue: ${r[1]:10.2f} - {product[3]} - {product[1]}')
