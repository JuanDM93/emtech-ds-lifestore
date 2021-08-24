"""
Frontend modules
"""
from .backend import *


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
        print('Login failed... try again')
        admin, secret = ask()
    print('Login succesful!')


def report(cats):
    separator = '\n-------------------\n'
    for c in cats:
        print(separator)
        print(f'"{c} Report" ->')
        test(c)


#### TESTING
def test(c:str):
    separator = '\n----------\n'
    cats = [c]

    # Search
    print(separator)
    print('searches:')
    searches = global_searches()
    cats_searched = filter_categories(searches, cats)

    if len(cats_searched) > 0:
        most_searched = custom_sort(cats_searched)[:10]
        print('* most_searched:')
        print(most_searched)
        
        least_searched = custom_sort(cats_searched, False)[:10]
        print('* least_searched:')
        print(least_searched)

    # Sale
    print(separator)
    print('sales:')
    sales = global_sales()
    cats_sold = filter_categories(sales, cats)
    
    if len(cats_sold) > 0:
        total_most_sold = custom_sort(cats_sold)[:10]
        print('* total_most_sold:')
        print(total_most_sold)

        total_least_sold = custom_sort(cats_sold, False)[:10]
        print('* total_least_sold:')
        print(total_least_sold)

        print('* historic:')
        for m in range(1, 2):
            month = f'{m:02d}'
            print(f'* - monthly_sales_{month}:')
            monthly_sold = filter_months(cats_sold, month)
            if len(monthly_sold) > 0:
                most_sold = custom_sort(monthly_sold)
                print(most_sold)

    # Review
    print(separator)
    print('reviews:')
    reviews = get_reviews(sales)
    cats_reviewed = filter_categories(reviews, cats)
    if len(cats_reviewed) > 0:
        most_reviewed = custom_sort(cats_reviewed)
        print('* most_reviewed:')
        print(most_reviewed)

        least_reviewed = custom_sort(cats_reviewed, False)
        print('* least_reviewed:')
        print(least_reviewed)

    # Stock
    print(separator)
    print('stocks:')
    stocks = get_stocks(sales)
    cats_stocked = filter_categories(stocks, cats)
    if len(cats_stocked) > 0:
        most_stock = custom_sort(cats_stocked)
        print('* most_stock:')
        print(most_stock)
        
        lowest_stock = custom_sort(cats_stocked, False)
        print('* lowest_stock:')
        print(lowest_stock)

    # Refunds
    print(separator)
    print('refunds:')
    refunds = get_refunds(sales)
    cats_refunds = filter_categories(refunds, cats)
    if len(cats_refunds) > 0:
        most_refund = custom_sort(cats_refunds)
        print('* most_refund:')
        print(most_refund)

        least_refund = custom_sort(cats_refunds, False)
        print('* least_refund:')
        print(least_refund)

    # Revenue
    print(separator)
    print('revenue:')
    revenues = get_revenue(sales)
    cats_revenue = filter_categories(revenues, cats)
    if len(cats_revenue) > 0:
        most_revenue = custom_sort(cats_revenue)
        print('* most_revenue:')
        print(most_revenue)

        least_revenue = custom_sort(cats_revenue, False)
        print('* least_revenue:')
        print(least_revenue)
####
