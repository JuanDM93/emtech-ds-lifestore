"""
PROJECT 1
This is a basic python based data science solution
author: juan_dm93@hotmail.com
"""
# Imports
from utils.frontend import login, report
from utils.backend import get_categories


# main program
def main():
    """
    login interface
    report by categories
    """
    login()
    CATEGORIES = get_categories()
    report(CATEGORIES)


if __name__ == "__main__":
    main()
