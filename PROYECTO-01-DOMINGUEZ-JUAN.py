"""
PROJECT 1
This is a data science use case solution using basic python
author: juan_dm93@hotmail.com
"""

"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""
from lifestore_file import lifestore_searches, lifestore_sales, lifestore_products


# Login
def login(user:str, password:str):
    """
    user:
    password:

    returns:
    """
    admin = 'JuanDM'
    secret = 'xxxxxx'
    if user==admin and password==secret:
        return True
    return False

# Sells
def sells():
    most_sell = sorted(lifestore_sales)[:50]
    most_searched = sorted(lifestore_searches)[:100]
    
# Reviews
def reviews():
    best_reviewed = lifestore_products.sort()[:20]
    worst_reviewed = lifestore_products.sort()[:20]

# Revenue
def revenue():
    total_revenue = None
    total_sells = None

    average_revenue = None
    average_sells = None
    
    best_months = None
