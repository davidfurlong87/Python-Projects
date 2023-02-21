from random import randint

class RestaurantCheck:
    def __init__(self, check_number, sales_tax_percent, subtotal, table_number, server_name):
        self.check_number = check_number
        self.sales_tax_percent = sales_tax_percent
        self.subtotal = subtotal
        self.table_number = table_number
        self.server_name = server_name
        
    def calculate_total(self):
        self.total = self.subtotal + (self.subtotal * (self.sales_tax_percent/100))
        return(self.total)
    
    def print_check(self):
        f = open('check{}.txt'.format(self.check_number), 'a')
        print(self.table_number, file = f)
        print(self.server_name, file=f)
        print(self.subtotal, file = f)
        print(self.sales_tax_percent, file = f)
        print(self.total, file = f)
        
run = True
while run:
    check_number = randint(100, 999)
    server_name = input('Who is the server? ')
    table_number = input('Whats the table number? ')
    subtotal = eval(input('How much is the bill? $'))
    tax = eval(input('Whats the sales tax percentage? $'))   
    check = RestaurantCheck(check_number, tax, subtotal, table_number, server_name)
    print('The total bill is {}'.format(check.calculate_total()))
    check.print_check()
    
        
