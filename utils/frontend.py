"""
Frontend modules
"""
from .backend import *


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


# Category selector
def cats_options():
    """
    Prints categories options
    """
    print('Select categories indices: 1,5,6,...')
    options = [(i, CATEGORIES[i]) for i in range(len(CATEGORIES))]
    for o in options:
        print(f'{o[0]}: {o[-1]}')


def ask_cats():
    """
    Validates categories input and prints report per category
    """
    separator = '\n**********\n'
    response = []
    flag = True
    while flag:
        cats_options()
        responses = input('cats: ')
        responses = responses.split(',')
        for r in responses:
            try:
                r = int(r)
                if r < 0 or r > 7:
                    print(separator)
                    print(f'WARNING: "{r}"" is not a valid option')
                    print()
                    continue
                response = CATEGORIES[r]
                cat_report(response)
            except ValueError:
                print(separator)
                print(f'ERROR: Wrong input "{r}"')
                print()
                continue
        flag = False


def cat_report(cat: str):
    """
    Prints category report (TESTING)
    """
    separator = '\n-------------------\n'
    print(separator)
    print(f'"{cat} Report" ->')
    test(cat)
    print(separator)


# TESTING
def test(c: str):
    """
    Prints report (TESTING)
    """
    separator = '\n----------\n'
    cats = [c]

    # Searches
    print(separator)
    print('searches:')
    print()
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
    print('sales:')
    print()
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
        print()
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
    print('reviews:')
    print()
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
    print('stocks:')
    print()
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
    print('refunds:')
    print()
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
    print('revenue:')
    print()
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
####
