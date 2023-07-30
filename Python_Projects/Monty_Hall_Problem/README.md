# Monty Hall Problem Simulation
Monty hall’s problem comes from a famous movie where three doors are used to help you win a car. How? Each door hides something behind it–a car and two goats. Any door can have the car while 
the remaining two have goats. The probability to find a car is ⅓. Now, if you select Door 1 and the host opens Door 3 to find a goat, your chances just become ⅔.

**Work Flow and Logic**

The following are the main points of the simulation:
- As there are three doors, a random permutation of the numbers 1, 2, and 3 would be generated, with each number representing a door. This permutation contains the first two numbers that correspond
  to the location of goats behind the door, and the third number corresponds to a car behind the door.
- Using images, the configuration is represented graphically. Every configuration has its own image.
- Only the door behind which there is a goat is to be revealed after the user has chosen a door number according to the puzzle. By selecting the door behind which the car is parked, the user can
  then reveal either of the other two doors. If the user selects a door behind which there is a goat, only one of the two remaining doors can be revealed (since the previously selected door cannot
  be revealed).
