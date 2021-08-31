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
PROCESSES = ['globals', 'categories', 'datetime']
CATEGORIES = get_categories()
DATES = get_dates()


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
            if response[0] > len(PROCESSES):
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
    if process_id == 0:
        print('- Globals -\n')
        globals()
    elif process_id == 1:
        print('- Categories -\n')
        ask_cats()
    elif process_id == 2:
        print('- Datetime -\n')
    else:
        print('- Unknown -\n')


# Globals
def globals():
    print('This is a global report\n')
    separator = '-------------------\n'
    print(separator)
    revenue()
    print(separator)
    months()
    print(separator)
    most_sold()
    print(separator)
    least_sold()
    print(separator)
    most_searched()
    print(separator)
    least_searched()
    high_stock()
    print(separator)
    low_stock()
    print(separator)
    best_reviewed()
    print(separator)
    worst_reviewed()
    print(separator)
    most_refunds()
    # Return
    input('Input anything to return')
    clear()


# Total revenue
def revenue():
    print('This is a total revenue report\n')


# Monthly revenue
def months():
    print('This is a monthly total revenue report\n')


# Most sold
def most_sold():
    print('Most sold items report\n')


# Least sold
def least_sold():
    print('Least sold items report\n')


# Most searched
def most_searched():
    print('Most searched items report\n')


# Least searched
def least_searched():
    print('Least searched items report\n')


# Most stock
def high_stock():
    print('High stock items report\n')


# Lowest stock
def low_stock():
    print('Low stock items report\n')


# Best reviewed
def best_reviewed():
    print('Best reviewed items report\n')


# Worst reviewed
def worst_reviewed():
    print('Worst reviewed items report\n')


# Most refunds
def most_refunds():
    print('Most refunds items report\n')


# By Category
def ask_cats():
    """
    Validates categories input and prints report per category
    """
    options = CATEGORIES[:]
    response = print_options(options)
    for r in response:
        c = CATEGORIES[r]
        cat_report(c)


def cat_report(cat: str):
    """
    Prints category report (TESTING)
    """
    separator = '-------------------\n'
    print(separator)
    print(f'"{cat} Report" ->\n')
    test(cat)
    print(separator)


# By Date

#################


# TESTING
def test(c: str):
    """
    Prints report (TESTING)
    """
    separator = '----------\n'
    cats = [c]

    # Searches
    print(separator)
    print('searches:\n')
    searches = global_searches()
    cats_searched = filter_categories(searches, cats)

    if len(cats_searched) > 0:
        most_searched = custom_sort(cats_searched)[:10]
        print('* most_searched:')
        print(most_searched)
        print()

        least_searched = custom_sort(cats_searched, False)[:10]
        print('* least_searched:')
        print(least_searched)
        print()

    # Sales
    print(separator)
    print('sales:\n')
    sales = global_sales()
    cats_sold = filter_categories(sales, cats)

    if len(cats_sold) > 0:
        total_most_sold = custom_sort(cats_sold)[:10]
        print('* total_most_sold:')
        print(total_most_sold)
        print()

        total_least_sold = custom_sort(cats_sold, False)[:10]
        print('* total_least_sold:')
        print(total_least_sold)
        print()

        print('* historic:')
        for m in range(1, 13):
            month = f'{m:02d}'
            print(f'- - monthly_sales_{month}:')
            monthly_sold = filter_dates(cats_sold, months=[month])

            if len(monthly_sold) > 0:
                most_sold = custom_sort(monthly_sold)
                print(most_sold)
                print()

    # Reviews
    print(separator)
    print('reviews:\n')
    reviews = get_reviews(sales)
    cats_reviewed = filter_categories(reviews, cats)
    if len(cats_reviewed) > 0:
        most_reviewed = custom_sort(cats_reviewed)
        print('* most_reviewed:')
        print(most_reviewed)
        print()

        least_reviewed = custom_sort(cats_reviewed, False)
        print('* least_reviewed:')
        print(least_reviewed)
        print()

    # Stocks
    print(separator)
    print('stocks:\n')
    stocks = get_stocks(sales)
    cats_stocked = filter_categories(stocks, cats)
    if len(cats_stocked) > 0:
        most_stock = custom_sort(cats_stocked)
        print('* most_stock:')
        print(most_stock)
        print()

        lowest_stock = custom_sort(cats_stocked, False)
        print('* lowest_stock:')
        print(lowest_stock)
        print()

    # Refunds
    print(separator)
    print('refunds:\n')
    refunds = get_refunds(sales)
    cats_refunds = filter_categories(refunds, cats)
    if len(cats_refunds) > 0:
        most_refund = custom_sort(cats_refunds)
        print('* most_refund:')
        print(most_refund)
        print()

        least_refund = custom_sort(cats_refunds, False)
        print('* least_refund:')
        print(least_refund)
        print()

    # Revenue
    print(separator)
    print('revenue:\n')
    revenues = get_revenue(sales)
    cats_revenue = filter_categories(revenues, cats)
    if len(cats_revenue) > 0:
        most_revenue = custom_sort(cats_revenue)
        print('* most_revenue:')
        print(most_revenue)
        print()

        least_revenue = custom_sort(cats_revenue, False)
        print('* least_revenue:')
        print(least_revenue)
        print()
####
