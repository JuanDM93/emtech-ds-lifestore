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
    
    sales = global_sales()
    sold = least_sold(sales)
    sold = filter_by_categories(sold, cats)[:50]
    print(f'least_sold {get_categories(sold)}:')
    print(count_empty(sold))
    
    searches = global_searches()
    searched = filter_by_categories(most_searched(searches), cats)[:100]
    print(f'most_searched {get_categories(searched)}:')
    print(count_empty(searched))
    
    stocks = global_stocks()
    stocked = filter_by_categories(lowest_stock(stocks), cats)
    print(f'lowest_stock {get_categories(stocked)}:')
    print(stocked)

    reviews = total_reviewes()
    reviewed = filter_by_categories(most_reviewed(reviews), cats)[:20]
    print(f'most_reviewed {get_categories(reviewed)}:')
    print(count_empty(reviewed))
    
    refs = total_refunds()
    refunds = filter_by_categories(most_refund(refs), cats)
    print(f'most_refund {get_categories(refunds)}:')
    print(refunds)

    revenues = total_revenue()
    revenue = filter_by_categories(least_revenue(revenues), cats)
    print(f'least_revenue {get_categories(revenue)}:')
    print(revenue)

    months = filter_by_categories(most_sold(sales), cats)
    monthly = filter_by_month(months, '01')
    print(f'monthly_sales {get_categories(monthly)}:')
    print(clean_empty(monthly))
####


# main program
def main():
    # GLOBALS
    CATEGORIES = get_categories()
    
    login()
    test()


if __name__ == "__main__":
    main()
