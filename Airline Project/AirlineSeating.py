# Yousif Alkhalaf

class Passenger(object):
    
    # Makes a Passenger according to a split line
    def __init__(self, info_list):
        self.fn = info_list[0]
        self.ln = info_list[1]
        self.seat_class = info_list[2]
        self.position = info_list[3]
        
        self.seat = (0, 'Z')
    
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
    
    # Returns passenger's assigned seat tuple
    def get_seat(self):
        return self.seat
    
    def all_same_row(party):
        target_row = party[0].get_seat()[0]
        if target_row == 0:
            return False
        for passenger in party:
            if passenger.get_seat()[0] != target_row:
                return False
        return True
    
    def in_proximity(party):
        pass

class Seats():
    taken_seats = []
    
    # Creates a list of numbers for rows within a given seat class
    def find_row_range(seat_class):
        if seat_class == 'First':
            row_range = [i for i in range(1, 4)]
        elif seat_class == 'Econ':
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
    
    def mark_seats_taken(seat_list):
        for seat in seat_list:
            Seats.taken_seats.append(seat)
    
    def choose_seats(party):
        now_taken_seats = []
        row_range = Seats.find_row_range(party[0].get_class())
        for row in row_range:
            for i in range(len(party)):
                seat_letters = Seats.find_letter_group(party[i].get_position())
                for letter in seat_letters:
                    seat = (row, letter)
                    if seat not in Seats.taken_seats and seat not in now_taken_seats:
                        party[i].set_seat(seat)
                        now_taken_seats.append(seat)
                        break
            if Passenger.all_same_row(party):
                Seats.mark_seats_taken(now_taken_seats  )
                return
            else:
                now_taken_seats.clear()
        
        
            

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

    
    

        

