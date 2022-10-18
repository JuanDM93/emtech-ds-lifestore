# Datasets
from utils.lifestore_file import lifestore_searches, lifestore_sales, lifestore_products


def get_total_searches() -> list:
    """
    returns: totals list by product -> [p_id, [type, ...]]
    """
    total_searches = [[p[0], []] for p in lifestore_products]
    for search in lifestore_searches:
        total_searches[search[1] - 1][1].append(search[0])
    return total_searches


SEARCHES = get_total_searches()


def get_total_sales() -> list:
    """
    returns: total sales list by product -> [p_id, total_sales]
    """
    total_sales = [[p[0], []] for p in lifestore_products]
    for sale in lifestore_sales:
        total_sales[sale[1] - 1][1].append(sale[0])
    return total_sales


SALES = get_total_sales()


# Single Getters

def get_product(id: int) -> list:
    """
    returns: product object from dataset
    """
    return lifestore_products[id - 1]


def get_sale(id: int) -> list:
    """
    returns: sale object from dataset
    """
    return lifestore_sales[id - 1]


def get_categorie(product_id: int) -> str:
    """
    returns: categorie str from product_id
    """
    return lifestore_products[product_id - 1][3]


def get_date(sale_id: str) -> list:
    """
    returns: date ['15','09','2020'] by sale_id 
    """
    return lifestore_sales[sale_id - 1][3].split('/')


# Custom Getters

def get_categories(data: list = lifestore_products) -> list:
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


CATEGORIES = get_categories()


def get_dates(data: list = lifestore_sales) -> list:
    """
    data: any list with sales_id at [0]
    returns: dates list from input
    """
    return [[d[0], get_date(d[0])] for d in data]


DATES = get_dates()


def get_years(data: list) -> list:
    """
    returns: ordered year list from sales data
    """
    years = []
    for d in data:
        y = d[-1][-1]
        if y not in years:
            years.append(y)
    years.sort(reverse=True)
    return years


YEARS = get_years(DATES)
