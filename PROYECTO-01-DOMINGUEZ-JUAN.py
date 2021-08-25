"""
PROJECT 1
This is a basic python based data science solution
author: juan_dm93@hotmail.com
"""
# Imports
from utils.frontend import login, ask_cats


# main program
def main():
    """
    login interface
    report by categories
    """
    # Login
    login()

    # Input categories
    ask_cats()


if __name__ == "__main__":
    main()
