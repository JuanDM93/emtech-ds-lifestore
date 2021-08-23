"""
Backend modules
"""
# Datasets
from utils.frontend import login
from .lifestore_file import lifestore_searches, lifestore_sales, lifestore_products


# Getters
def get_product(id:int) -> list:
    """
    returns: product object from dataset
    """
    return lifestore_products[id - 1]


def get_sale(id:int) -> list:
    """
    returns: sale object from dataset
    """
    return lifestore_sales[id - 1]


def get_categorie(product_id:int) -> str:
    """
    returns: categorie str from product_id
    """
    return lifestore_products[product_id - 1][3]
        

def get_categories(data:list=lifestore_products) -> list:
    """
    data: any list with product_id at [0]
    returns: categories list from input
    """
    categories = []
    for d in data:
        cat = get_categorie(d[0])
        if cat not in categories:
            categories.append(cat)
    return categories


# Filters
def clean_empty(data:list) -> list:
    """
    data: any list with id at [0] and to_clean_list at [1]
    returns: clean list (remove [])
    """
    return [d for d in data if len(d[1]) > 0]


def count_empty(data:list) -> list:
    """
    data: any list with id at [0] and to_count_list at [1]
    returns: count list ([] -> 0, [...] -> len([...]))
    """
    return [[d[0], len(d[1])] for d in data]


def filter_by_categories(data:list, cats:list) -> list:
    """
    data: any list with product_id at [0]
    cats: a custom categories list
    returns: list of products filtered by cats
    """
    return [d for d in data if get_categorie(d[0]) in cats]


def filter_by_month(data:list, month:str) -> list:
    """
    data: any list with product_id at [0] and sales_ids at [1]
    month: str ['01', ..., '12']
    returns: list of product sales filtered by month
    """
    result = []
    for ps in data:
        sales = []
        for s in ps[1]:
            sale = get_sale(s)
            s_date = sale[3].split('/')[1]
            if s_date == month:
                sales.append(s)
        result.append([ps[0], sales])
    return result
        

# Sales
def global_sales() -> list:
    """
    returns: global sales list by product
    """
    total_sales = [[p[0], []] for p in lifestore_products]
    for sale in lifestore_sales:
        total_sales[sale[1] - 1][1].append(sale[0])
    return total_sales


def most_sold(data:list) -> list:
    """
    data: any list with product_id at [0]
    returns: sorted most sold products list
    """
    result = data[:]
    result.sort(key=lambda p: len(p[-1]), reverse=True)
    return result


def least_sold(data:list) -> list:
    """
    data: any list with product_id at [0]
    returns: sorted least sold products list
    """
    result = data[:]
    result.sort(key=lambda p: len(p[1]), reverse=False)
    return result


# Searches
def global_searches() -> list:
    """
    returns: global search list by product
    """ 
    total_searches = [[p[0], []] for p in lifestore_products]
    for search in lifestore_searches:
        total_searches[search[1] - 1][1].append(search[0])
    return total_searches


def most_searched(data:list) -> list:
    """
    data: any list with product_id at [0]
    returns: sorted most searched products list
    """
    result = data[:]
    result.sort(key=lambda p: len(p[-1]), reverse=True)
    return result


def least_searched(data:list) -> list:
    """
    data: any list with product_id at [0]
    returns: sorted least searched products list by category
    """
    result = data[:]
    result.sort(key=lambda p: len(p[-1]), reverse=False)
    return result


# Stocks
def global_stocks() -> list:
    """
    returns: global stocks for products 
    """
    return [[p[0], p[-1]] for p in lifestore_products]


def lowest_stock(data:list) -> list:
    """
    data: any list with product_id at [0]
    returns: sorted low stock products list by category
    """
    result = data[:]
    result.sort(key=lambda p: p[1], reverse=False)
    return result


def most_stock(data:list) -> list:
    """
    data: any list with product_id at [0]
    returns: sorted low stock products list by category
    """
    result = data[:]
    result.sort(key=lambda p: p[1], reverse=True)
    return result


# Reviews
def total_reviewes() -> list:
    """
    returns: reviews per global products list
    """
    result = []
    g_sales = global_sales()
    for i in range(len(g_sales)):
        result.append([g_sales[i][0], []])
        sales = g_sales[i][1]
        for s in sales:
            review = get_sale(s)[2]
            result[i][1].append(review)
    return result


def most_reviewed(data:list) -> list:
    """
    data: any list with product_id at [0]
    returns: product reviews list per categories
    """
    result = data[:]
    result.sort(key=lambda p: len(p[-1]), reverse=True)
    return result


def least_reviewed(data:list) -> list:
    """
    data: any list with product_id at [0]
    returns: product reviews list per categories
    """
    result = data[:]
    result.sort(key=lambda p: len(p[-1]), reverse=False)
    return result


# Refunds
def total_refunds() -> list:
    """
    returns: total refunds per product list
    """
    result = []
    g_sales = global_sales()
    for i in range(len(g_sales)):
        result.append([g_sales[i][0], 0])
        sales = g_sales[i][1]
        for s in sales:
            result[i][1] += get_sale(s)[-1]
    return result


def most_refund(data:list) -> list:
    """
    data: any list with product_id at [0]
    returns: product refunds list per categories
    """
    result = data[:]
    result.sort(key=lambda p: p[-1], reverse=True)
    return result


def least_refund(data:list) -> list:
    """
    data: any list with product_id at [0]
    returns: product refunds list per categories
    """
    result = data[:]
    result.sort(key=lambda p: p[-1], reverse=False)
    return result


# Revenue
def total_revenue() -> list:
    """
    returns: total revenue per product list
    """
    result = []
    for ps in global_sales():
        product = get_product(ps[0])
        ps_total = 0
        for s in ps[1]:
            refund = get_sale(s)[-1]
            if refund == 0:
                ps_total += product[2]
        result.append([ps[0], ps_total])
    return result


def most_revenue(data:list) -> list:
    """
    data: any list with product_id at [0]
    returns: product revenue list per categories
    """
    result = data[:]
    result.sort(key=lambda p: p[-1], reverse=True)
    return result


def least_revenue(data:list) -> list:
    """
    data: any list with product_id at [0]
    returns: product revenue list per categories
    """
    result = data[:]
    result.sort(key=lambda p: p[-1], reverse=False)
    return result
