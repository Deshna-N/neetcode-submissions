# same destination and there are n cars going there 
# given position and speed of each car
# destination is = target

## cannot overtake more ahead car, so if pos1 > pos2, pos2 can only drive at same speed together
## car fleet is squad of cars driving same pos same speed
## every pos on track including when pos = target, if same speed same pos then car is in car fleet

### tracking different car fleets and how many get to the destination aka target

## 
## nlogn so prob wanna use sort method -> wanna sort by position??

## could store in a dict the position as key and speed as value, then sort the dict??


## so length of pos equals number of cars currently active aka how many current fleets there are
## output can equal length of position then 

# only compare a car with the one directly infront -> determines if joins fleet or it stays its own fleet

# use a list with tuples inside for (pos, speed) then sort based on pos

## i need a way to track that if the fleets all have passed the target destination then its all done!!
## maybe need a while loop

## FOCUS ON HOURS NOT ACTU MOVEMENT!


class Solution: 
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_store = [] ## monotonic stack

        cars = list(zip(position, speed))
        cars = sorted(cars, reverse = True) ## farthest aka closest to target looked at first

        #### while loop here?????
        for position, speed in cars:
            time = (target - position) / speed
            
            if not time_store:
                time_store.append(time)
            else:               
                if time > time_store[-1]:
                    ######## technically i gotta make the curr_fleet's speed same as prev one but is that needed since output wont return that info?????
                    time_store.append(time)
                ##else: ## different posiitons, not combining fleets
        return len(time_store)


## distance of 10, cars = [(4,2) , (1,3)], output = 2
## so fleet 1 at 4 with 2 mi/hr and fleet2 at 1 with 3 mi/hr
## prevfleet_pos = 4
##--
##only going to do (1,3) based on for loop
## curr_fleet_pos = 1
## 1 != 4 so dont combine, and prevfleet_pos = 1 



## target of 10, fleet1 at 7 with 1 mi/hr, fleet 2 at 4 with 2 mi/hr, fleet 3 at 1 with 2 mi/hr, fleet 4 at 0 with 1 mi/hr
## so output = 4 rn for the 4 fleets

## ex 2: cars = [(7,1) , (4,2), (1,2). (0,1)]
## starting with fleet 2 at 4 with 2 mi/hr
## if the pos of fleet 2 = pos of previous fleet then one less fleet

        





 






# c1    c2
# [1 2 3 4 5 6 7 8 9 10]
## ex 1: car1 at pos 1 at speed 3 mi/hr, car2 at pos 4 speed 2 mi/hr, going to pos 10 miles.
## hr 2, car1 at pos 4, car2 at pos 6
## hr 3, car1 at pos 7, car2 at pos 8
# hr 4, car1 at pos 10, car2 at pos 10 -> same pos and since same pos (car1 caught up) so now same speed
## -> thus same pos same speed so in a fleet so they in 1 fleet now so only 1 fleet at destination, no other cars left so output is 1

## 

        