# kwargs: specifies that arbitrarily many keyword arguments can be provided (in addition to any keyword arguments already
# accepted by other parameters). Such a parameter can be defined by prepending the parameter name with **
# https://docs.python.org/3/glossary.html
def list_term(**terms):
    for key, value in terms.items():
        print(f'{key}: {value}')

list_term(IDE='Integrated Developement Environment', РК= 'Primary Key')
list_term(DBMS= 'Database Management System')