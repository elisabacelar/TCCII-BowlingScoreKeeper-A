class Frame:
    def __init__(self, first_throw: int, second_throw: int) -> None:
        if (first_throw + second_throw) > 10:
            raise Exception('Sum of two throughs should not exceed 10')
        self.first_throw = first_throw
        self.second_throw = second_throw
        self.current_score = self.first_throw + self.second_throw
        self.last_frame = False

    def score(self) -> int:
        """ The score of a single frame """
        return self.current_score
    
    def update_score(self, throw):
        self.current_score = self.current_score + throw

    def is_strike(self) -> bool:
        if (self.first_throw == 10 and self.second_throw == 0):
            return True
        else:
            return False    

    def is_spare(self) -> bool:
        if self.is_strike():
            return False
        if (self.first_throw + self.second_throw) == 10:
            return True
        else:
            return False

    def set_as_last_frame(self):
        self.last_frame = True

    def is_last_frame(self) -> bool:
        return self.last_frame
