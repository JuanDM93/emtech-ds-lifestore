"""
PROJECT 1
This is a basic python based data science solution
author: juan_dm93@hotmail.com
"""
# Imports
from utils.frontend import login
from utils.backend import *


#### TESTING
def test():
    cats = ['procesadores', 'audifonos']
    
    searches = clean_list(global_searches())
    cats_searched = filter_categories(searches, cats)
    most_searched = custom_sort(cats_searched)[:10]
    print(f'most_searched {get_categories(most_searched)}:')
    print(most_searched)

    sales = clean_list(global_sales())
    cats_sold = filter_categories(sales, cats)
    least_sold = custom_sort(cats_sold, False)[:10]
    print(f'least_sold {get_categories(least_sold)}:')
    print(least_sold)

    monthly_sold = filter_months(cats_sold, '01')
    most_sold = custom_sort(monthly_sold)[:10]
    print(f'monthly_sales {get_categories(most_sold)}:')
    print(most_sold)
    
    stocks = get_stocks(sales)
    cats_stocked = filter_categories(stocks, cats)
    lowest_stock = custom_sort(cats_stocked, False)
    print(f'lowest_stock {get_categories(lowest_stock)}:')
    print(lowest_stock)

    reviews = get_reviews(sales)
    cats_reviewed = filter_categories(reviews, cats)
    most_reviewed = custom_sort(cats_reviewed)[:10]
    print(f'most_reviewed {get_categories(most_reviewed)}:')
    print(most_reviewed)
    
    refunds = get_refunds(sales)
    cats_refunds = filter_categories(refunds, cats)
    most_refund = custom_sort(cats_refunds)
    print(f'most_refund {get_categories(most_refund)}:')
    print(most_refund)

    revenues = get_revenue(sales)
    cats_revenue = filter_categories(revenues, cats)
    least_revenue = custom_sort(cats_revenue, False)
    print(f'least_revenue {get_categories(least_revenue)}:')
    print(least_revenue)
####


# main program
def main():
    # GLOBALS
    CATEGORIES = get_categories()
    
    login()
    test()


if __name__ == "__main__":
    main()
