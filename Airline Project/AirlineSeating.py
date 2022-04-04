# Yousif Alkhalaf

class Passenger(object):
    
    def __init__(self, fn, ln, seat_class, position):
        self.fn = fn
        self.ln = ln
        self.seat_class = seat_class
        self.position = position
        
        self.seat = None
    
    def __str__(self):
        return f'{self.fn} {self.ln} Seat {self.seat[0]}{self.seat[1]}'
    
    def get_class(self):
        return self.seat_class
    
    def get_position(self):
        return self.position
    
    def set_seat(self, seat):
        self.seat = seat

class Seats():
    taken_seats = []
    
    def find_row_range(seat_class):
        if seat_class == 'First':
            row_range = [i for i in range(1, 4)]
        else:
            row_range = [i for i in range(6, 31)]
        return row_range
    
    def find_letter_group(position):
        if position == 'W':
            return ('A', 'F')
        elif position == 'A':
            return ('C', 'D')
        else:
            return ('B', 'E')
    
    def choose_seats(passengers):
        if type(passengers) != list:
            row_range = Seats.find_row_range(passengers.get_class())
            letter_group = Seats.find_letter_group(passengers.get_position())
            
            for num in row_range:
                for letter in letter_group:
                    seat = (num, letter)
                    
                    if seat not in Seats.taken_seats:
                        passengers.set_seat(seat)
                        Seats.taken_seats.append(seat)
                        return seat
                
        
    
 
with open('passengers.txt', encoding='utf-8') as f:
    for line in f:
        line = line.split()
        passenger = Passenger(line[0], line[1], line[2], line[3])
        
        Seats.choose_seats(passenger)
        print(passenger)