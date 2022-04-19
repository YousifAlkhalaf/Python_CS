# Yousif Alkhalaf
import math

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

# Adds a list of seats to the taken seats list
def mark_seats_taken(seat_list):
    for seat in seat_list:
        taken_seats.append(seat)

# Checks if all party members are in the same row
def all_same_row(party):
    target_row = party[0].get_seat_row() # 1st member's row is used as target
    if target_row == 0: # Disqualify placeholders
        return False
    for passenger in party:
        if passenger.get_seat_row() != target_row: 
            return False
    return True

# Picks out seats for a party
def choose_seats(party):
    now_taken_seats = [] # List of seats to later mark as taken
    row_range = find_row_range(party[0].get_class()) # Determines 1st class/econ based on 1st party member
    for row in row_range:
        for i in range(len(party)): # Loops through party members
            seat_letters = find_letter_group(party[i].get_position()) #Viable seat letters are picked based on desired seat position
            for letter in seat_letters: # Checks both viable seat letters
                seat = (row, letter)
                if seat not in taken_seats and seat not in now_taken_seats:
                    party[i].set_seat(seat)
                    now_taken_seats.append(seat) # Seat is ready to be taken
                    break # Next passenger is selected
        if all_same_row(party):
            mark_seats_taken(now_taken_seats) # Seats are officially marked as taken
            Passenger.make_proximate(party)
            return # Seat assignments end
        else:
            now_taken_seats.clear() # Process repeats for next row

class Passenger(object):
    
    # Makes a Passenger according to a split line
    def __init__(self, info_list):
        self.fn = info_list[0]
        self.ln = info_list[1]
        self.seat_class = info_list[2]
        self.position = info_list[3]
        
        self.seat = (0, 'Z') # Placeholder
    
    def __str__(self):
        if self.seat == (0, 'Z'):
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
    
    def get_seat_row(self):
        return self.seat[0]
    
    def get_seat_letter(self):
        return self.seat[1]
    
    def swap_seat_letter(self): # Moves seat to opposite side with same position
        
        current_letter = self.get_seat_letter()
        
        if self.get_seat_row() < 6:
            return
        
        if current_letter == 'A':
            new_letter = 'F'
        elif current_letter == 'B':
            new_letter = 'E'
        elif current_letter == 'C':
            new_letter = 'D'
        elif current_letter == 'D':
            new_letter = 'C'
        elif current_letter == 'E':
            new_letter = 'B'
        elif current_letter == 'F':
            new_letter = 'A'
        
            
        prospect_seat = (self.get_seat_row(), new_letter) # New seat is made, checked to see if taken
        if prospect_seat not in taken_seats:
            self.set_seat(prospect_seat)
    
    def make_proximate(party):
        max_distance = len(party) - 1 
        for passenger in party: # Main passenger being made proximate
            letter = ord(passenger.get_seat_letter())
            for other_person in party: # Members of party checked for proximity
                other_letter = ord(other_person.get_seat_letter())
                if math.fabs(letter - other_letter) > max_distance: # Distance is too large
                    passenger.swap_seat_letter()
        
        
            

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
    choose_seats(party)

print(passengers)

    
    

        

