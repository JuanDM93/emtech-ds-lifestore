"""
Backend modules
"""
# Datasets
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
def filter_by_categories(data:list, cats:list) -> list:
    """
    data: any list with product_id at [0]
    cats: a custom categories list
    returns: list of products filtered by cats
    """
    return [d for d in data if get_categorie(d[0]) in cats]


def filter_by_month(data:list, month:str='01') -> list:
    """
    data: any list with product_id at [0] and sales_ids at [1]
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
    returns: sales list by product
    """
    total_sales = [[p[0], []] for p in lifestore_products]
    for sale in lifestore_sales:
        total_sales[sale[1] - 1][1].append(sale[0])
    return total_sales


def monthly_sales(data:list, month:str) -> list:
    """
    data: any list with product_id at [0] and sales_ids at [1]
    returns: monthly filtered sales
    """
    return filter_by_month(data, month)


def most_sold(data:list, categories:list) -> list:
    """
    data: any list with product_id at [0]
    returns: sorted most sold products list by category
    """
    result = data[:]
    result.sort(key=lambda p: len(p[-1]), reverse=True)
    return filter_by_categories(result, categories)


def least_sold(data:list, categories:list) -> list:
    """
    data: any list with product_id at [0]
    returns: sorted least sold products list by category
    """
    result = data[:]
    result.sort(key=lambda p: len(p[-1]), reverse=False)
    return filter_by_categories(result, categories)


# Searches
def global_searches() -> list:
    """
    returns: search list by product
    """ 
    total_searches = [[p[0], []] for p in lifestore_products]
    for search in lifestore_searches:
        total_searches[search[1] - 1][1].append(search[0])
    return total_searches


def most_searched(data:list, categories:list=['procesadores']) -> list:
    """
    data: any list with product_id at [0]
    returns: sorted most searched products list
    """
    result = data[:]
    result.sort(key=lambda p: len(p[-1]), reverse=True)
    return filter_by_categories(result, categories)


def least_searched(data:list, categories:list=['procesadores']) -> list:
    """
    data: any list with product_id at [0]
    returns: sorted least searched products list by category
    """
    result = data[:]
    result.sort(key=lambda p: len(p[-1]), reverse=False)
    return filter_by_categories(result, categories)


# Stocks
def global_stocks() -> list:
    """
    returns: products in stock 
    """
    return [[p[0], p[-1]] for p in lifestore_products]


def lowest_stock(data:list, categories:list=['procesadores']) -> list:
    """
    data: any list with product_id at [0]
    returns: sorted low stock products list by category
    """
    result = data[:]
    result.sort(key=lambda p: p[1], reverse=False)
    return filter_by_categories(result, categories)


def most_stock(data:list, categories:list=['procesadores']) -> list:
    """
    data: any list with product_id at [0]
    returns: sorted low stock products list by category
    """
    result = data[:]
    result.sort(key=lambda p: p[1], reverse=True)
    return filter_by_categories(result, categories)


# Reviews
def total_reviewes() -> list:
    """
    returns: reviews per product list
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


def most_reviewed(data:list, categories:list=['procesadores']) -> list:
    """
    data: any list with product_id at [0]
    returns: product reviews list per categories
    """
    result = data[:]
    result.sort(key=lambda p: len(p[-1]), reverse=True)
    return filter_by_categories(result, categories)


def least_reviewed(data:list, categories:list=['procesadores']) -> list:
    """
    data: any list with product_id at [0]
    returns: product reviews list per categories
    """
    result = data[:]
    result.sort(key=lambda p: len(p[-1]), reverse=False)
    return filter_by_categories(result, categories)


# Refunds
def total_refunds() -> list:
    """
    returns: refunds per product list
    """
    result = []
    g_sales = global_sales()
    for i in range(len(g_sales)):
        result.append([g_sales[i][0], 0])
        sales = g_sales[i][1]
        for s in sales:
            result[i][1] += get_sale(s)[-1]
    return result


def most_refund(data:list, categories:list=['procesadores']) -> list:
    """
    data: any list with product_id at [0]
    returns: product refunds list per categories
    """
    result = data[:]
    result.sort(key=lambda p: p[-1], reverse=True)
    return filter_by_categories(result, categories)


def least_refund(data:list, categories:list=['procesadores']) -> list:
    """
    data: any list with product_id at [0]
    returns: product refunds list per categories
    """
    result = data[:]
    result.sort(key=lambda p: p[-1], reverse=False)
    return filter_by_categories(result, categories)


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


def most_revenue(data:list, categories:list=['procesadores']) -> list:
    """
    data: any list with product_id at [0]
    returns: product revenue list per categories
    """
    result = data[:]
    result.sort(key=lambda p: p[-1], reverse=True)
    return filter_by_categories(result, categories)


def least_revenue(data:list, categories:list=['procesadores']) -> list:
    """
    data: any list with product_id at [0]
    returns: product revenue list per categories
    """
    result = data[:]
    result.sort(key=lambda p: p[-1], reverse=False)
    return filter_by_categories(result, categories)
