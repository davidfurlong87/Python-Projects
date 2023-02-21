class Ticket:
    def __init__(self, cost, time):
        self.cost = cost
        self.time = time
        
    def __str__ (self):
        return('Ticket ({}, {})'.format(self.cost,self.time))
    
    def is_evening(self):
        if int((self.time.split(':'))[0]) >= 18:
            return(True)
        else:
            return(False)
        
    def bulk_discount(self, n):
        self.n = n
        if self.n >= 5 and self.n <=9:
            return(10)
        elif self.n >= 10:
            return(20)
        else:
            return(0)
        
class MovieTicket(Ticket):
    def __init__(self, cost, time, movie_name):
        Ticket.__init__(self, cost, time)
        self.movie_name = movie_name
        
    def __str__(self):
        return('Movie Ticket ({}, {}, {})'.format(self.cost,self.time, self.movie_name))
    
    def afternoon_discount(self):
        if int(self.time.split(':')[0]) >=12 and int(self.time.split(':')[0])<=17:
            return(10)
        else:
            return(0)
        
        
davids_ticket = MovieTicket(10, '11:59', 'Asian Pussy')
print(davids_ticket)
print(davids_ticket.is_evening())
print(davids_ticket.bulk_discount(11))
print(davids_ticket.afternoon_discount())
        