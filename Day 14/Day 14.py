import re
from dataclasses import dataclass

@dataclass
class Reindeer():

    name: str
    speed:  int
    endurance: int
    rest_time: int
    distance: int = 0

    def distance_traveled(self,race_time):
        self.distance = 0
        cycles, time_remaining = divmod(race_time, self.endurance + self.rest_time)

        self.distance = self.speed*(self.endurance * cycles +
        (time_remaining if time_remaining < self.endurance else self.endurance))

        return(self.distance)

class Race():

    def __init__(self, file, race_time, old_scoring = True) -> None:

        with open(file) as f:
            reindeer = [line.strip() for line in f.readlines()]
        stats  = [[re.findall('([A-Z][a-z]+)', line), (re.findall('[\d]+',line))] for line in reindeer]

        self.racers = [Reindeer(
            racer[0][0],
            int(racer[1][0]),
            int(racer[1][1]),
            int(racer[1][2]))
            for racer in stats]
        
        self.race_time = race_time
        self.old_scoring = old_scoring


    def start(self):

        if self.old_scoring:
            
            positions = [racer.distance_traveled(self.race_time) for racer in self.racers]
            return(max(positions))

        else:
            
            score = {racer.name:0 for racer in self.racers}

            timer = 1
            while timer < self.race_time:
                
                positions = [racer.distance_traveled(timer) for racer in self.racers]
                lead_position = max(positions)
                leaders = [racer.name for racer in self.racers if racer.distance == lead_position]

                for leader in leaders:
                    score[leader] +=1
                
                timer += 1
            
            return(score)


if __name__ == "__main__":
    race_time = 2503
    part1 = Race('input.txt', race_time, old_scoring = True).start()
    part2 = max(Race('input.txt', race_time, old_scoring = False).start().values())

    print(f'The answers to part 1 and 2 are {part1} and {part2} respectively')

