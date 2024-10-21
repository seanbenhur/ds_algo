class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars  = [[p,s] for p,s in zip(position,speed)]
        cars = sorted(cars,reverse=True)

        time_to_reach = fleet = 0


        for position,speed in cars:
            time = (target-position)/speed

            if time > time_to_reach:
                time_to_reach = time
                fleet += 1
        return fleet

        