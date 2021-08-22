"""
Frontend modules
"""
# Login
def login():
    """
    admin:  admin
    secret: pass
    """
    def ask() -> tuple:
        """
        returns: user inputs (admin, secret)
        """
        admin = input('Input admin user: ')
        secret = input('Password: ')
        return admin, secret
    
    admin, secret = ask()
    while 'admin' != admin or 'pass' != secret:
        print('Login failed... try again')
        admin, secret = ask()
    print('Login succesful!')


def revenue():
    average_revenue = None
    average_sells = None
    
    best_months = None
