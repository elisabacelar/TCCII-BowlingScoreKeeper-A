from typing import List

from bowling.frame import Frame


class BowlingGame:
    def __init__(self):
        self.frames = []
        self.bonus_first = 0
        self.bonus_second = 0
        self.next_frame_bonus = False

    def add_frame(self, frame: Frame):
        if len(self.frames) == 10:
            raise Exception('A game cannot have more than 10 frames')
        if len(self.frames) == 9:
            frame.set_as_last_frame()
            if frame.is_spare() or frame.is_strike():
                self.next_frame_bonus = True
        self.update_frame_scores(frame)
        self.frames.append(frame)

    def update_frame_scores(self, frame: Frame):
        if (len(self.frames) != 0):
            last_frame = self.frames[len(self.frames) - 1]
            if last_frame.is_strike():
                last_frame.update_score(frame.first_throw)
                last_frame.update_score(frame.second_throw)
                if len(self.frames) > 1:
                    last_last_frame = self.frames[len(self.frames) - 2]
                    if last_last_frame.is_strike():
                        last_last_frame.update_score(frame.first_throw)
            if last_frame.is_spare():
                last_frame.update_score(frame.first_throw)

    def set_bonus(self, first_throw: int, second_throw: int):
        """ The the bonus throw """
        self.bonus_first = first_throw
        self.bonus_second = second_throw
        last_frame = self.frames[len(self.frames) - 1]
        if last_frame.is_spare():
            last_frame.update_score(first_throw)
        elif last_frame.is_strike():
            last_frame.update_score(first_throw)
            last_frame.update_score(second_throw)

        last_last_frame = self.frames[len(self.frames) - 2]
        if (last_last_frame.is_strike()):
            last_last_frame.update_score(first_throw)


    def score(self) -> int:
        score = 0

        for frame in self.frames:
            score = score + frame.score()

        return score

    def is_next_frame_bonus(self) -> bool:
        return self.next_frame_bonus
     