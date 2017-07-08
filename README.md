# SimEarth
A quick pythonskript as shwocase for the SimEarth project

--- === Definitions: === ---

-= state =- //
A matrix which holds every information about the current state of the simulated objects

-= function =- //
like its mathematical counterpart it takes elements from the matrix as input, makes some calculations and writes the output 
back into the matrix

-= even =-//
a organized collection of functions, used for better organization of the code and the simulation in generall 

---

the numpy array state is our state

state = np.array = ([100, 200, 130, 1.05, 1.02, 0.75])

the first number is the totale population of our species 100
the seconde number is the fertility of land, basically how many individuals the world can sustain and feed 200
the third number is the food supply - how much food there currently is available in our world
the fourth number is a constant, it is the rate of births in percent, in that case 5% or 1.05
the fifth number is also a constatn, it is the rate of deaths in the population, also in %, 2% or 1.02
the sixth number is also a constant, here it is the fertility factor. just something you can change to change the impact of a large population onto the food supplie.

---------------------------

function_food_growth(array):
  this function determines how much new food there is available

function_food_consumption
  this functions determines how much food gets eaten per day
  
 function_deaths
  this function calculates the deaths in the population
  
function_births
  this function calculates the number of births in the population
 
-------------------------
calculate average
  this is NOT a function in OUR SENSE
  it takes to different matricies A and B
  then it calculates the average of the elements a_ij and b_ij for every element in A and B and returns a new matrix
  
 ----------------------
 Event_New_Day
  this is an Event. it organizes the functions and returns a new state
  
