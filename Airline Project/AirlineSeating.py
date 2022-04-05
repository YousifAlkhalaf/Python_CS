# Yousif Alkhalaf

class Passenger(object):
    
    # Makes a Passenger according to a split line
    def __init__(self, info_list):
        self.fn = info_list[0]
        self.ln = info_list[1]
        self.seat_class = info_list[2]
        self.position = info_list[3]
        
        self.seat = None
    
    def __str__(self):
        if self.seat == None:
            return f'{self.fn} {self.ln}: No seat assigned'
        return f'{self.fn} {self.ln}: Seat {self.seat[0]}{self.seat[1]}'
    
    def __repr__(self):
        return self.__str__()
    
    # Returns passenger seat class
    def get_class(self):
        return self.seat_class
    
    # Returns passenger seat position
    def get_position(self):
        return self.position
    
    # Sets passenger's seat to a given seat tuple
    def set_seat(self, seat):
        self.seat = seat

class Seats():
    taken_seats = []
    
    # Creates a list of numbers for rows within a given seat class
    def find_row_range(seat_class):
        if seat_class == 'First':
            row_range = [i for i in range(1, 4)]
        else:
            row_range = [i for i in range(6, 31)]
        return row_range
    
    # Creates a tuple of viable letters based on desired seat position
    def find_letter_group(position):
        if position == 'W':
            return ('A', 'F')
        elif position == 'A':
            return ('C', 'D')
        else:
            return ('B', 'E')
    
    def choose_seats(party):
        row_range = Seats.find_row_range(party[0].get_class())
        
            

passengers = []
with open ('passengers.txt', encoding='utf-8') as f:
    for line in f:
        line = line.split()
        passenger = Passenger(line)
        is_new_party = int(line[4]) != 0 
        
        if is_new_party:
            # New party is created
            passengers.append([passenger])
        else:
            # Passenger is put into last created party
            passengers[-1].append(passenger)

for party in passengers:
    Seats.choose_seats(party)

print(passengers)

    
    

        

