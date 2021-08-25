"""
Frontend module
"""
from .backend import *


PROCESSES = ['cats', 'monthly', 'other']
CATEGORIES = get_categories()


# Login
def login():
    """
    admin:  admin
    secret: pass
    """
    def ask() -> tuple:
        """
        returns: user inputs (admin, secret)
        """
        admin = input('Input admin user: ')
        secret = input('Password: ')
        return admin, secret

    admin, secret = ask()
    while 'admin' != admin or 'pass' != secret:
        print('Login failed... try again\n')
        admin, secret = ask()
    print('Login succesful!\n')


# Option printer
def print_options(options: list) -> list:
    """
    Prints options list
    """
    separator = '**********\n'
    print(separator)
    print('Select option by indices : 1,5,6,...\n')

    size = len(options)
    options = [(i, options[i]) for i in range(size)]
    for o in options:
        print(f'{o[0]}: {o[-1]}')
    answer = input('answer: ')

    valids = []
    errors = [[], []]
    answer = answer.split(',')
    for a in answer:
        try:
            a = int(a)
            if a < 0 or a > size - 1:
                errors[0].append(a)
                continue
        except ValueError:
            errors[1].append(a)
            continue
        valids.append(a)

    for e in errors[1]:
        print(separator)
        print(f'ERROR: Wrong input "{e}"\n')
        
    for w in errors[0]:
        print(separator)
        print(f'WARNING: "{w}"" is not a valid option\n')
            
    for v in valids:
        print(separator)
        print(f'INFO: validated input "{a}"\n')
    
    return valids


# Manual report
def manual():
    """
    Prints manual report
    """
    separator = '**********\n'
    print(separator)
    print('Hi, what would you like to do?\n')
    response = print_options(PROCESSES)
    for r in response:
        if r == 0:
            print(f'INFO: Running "{PROCESSES[r]}" process\n')
            ask_cats()
            print(separator)
        else:
            print(f'ERROR: Process "{PROCESSES[r]}" not yet available\n')
            print(separator)


def ask_cats():
    """
    Validates categories input and prints report per category
    """
    response = print_options(CATEGORIES)
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
            monthly_sold = filter_months(cats_sold, month)
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
