"""
PROJECT 1
This is a basic python based data science solution
author: juan_dm93@hotmail.com
"""
# Imports
from utils.frontend import login, interface


# main program
def main():
    """
    login and report interface
    """
    # Login to use it
    if login():
        interface()


if __name__ == "__main__":
    main()
