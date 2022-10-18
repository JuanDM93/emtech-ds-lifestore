from backend.globals import get_categorie


def clean_list(data: list) -> list:
    """
    data: any list with id at [0] and to_clean_list at [-1]
    returns: clean list
    """
    if len(data) > 0:
        if type(data[0][1]) is list:
            return [d for d in data if len(d[1]) > 0]
        return [d for d in data if d[1] > 0]
    return data


def custom_sort(data: list, reverse: bool = True) -> list:
    """
    data: any list with id at [0] and to_sort_list at [-1]
    reverse: ordering type, default -> most
    returns: sorted custom list
    """
    if len(data) > 0:
        result = data[:]
        if type(result[0][-1]) is not list:
            result.sort(key=lambda p: p[-1], reverse=reverse)
        else:
            result.sort(key=lambda p: len(p[-1]), reverse=reverse)
        return result
    return data


def filter_categories(data: list, cat: str) -> list:
    """
    data: any list with product_id at [0]
    cat: a custom categorie
    returns: list of products filtered by cats
    """
    return [d for d in data if get_categorie(d[0]) == cat]
