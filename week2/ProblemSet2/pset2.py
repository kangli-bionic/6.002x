# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

# For Python 2.7:
from ps2_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, you are not using 
# Python 2.7 and using most likely Python 2.6:
# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# Enter your code for RectangularRoom in this box
# 6.00.2x Problem Set 2: Simulating robots
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.tiles = {}
        
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        m = int(pos.getX())
        n = int(pos.getY())
        self.tiles[m,n] = 'clean'
        

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        #self.tile = [['unclean' for x in xrange(self.width)] for x in xrange(self.height)]
        #if self.pos[n-1][m-1] == 'clean':
            #return True
        return (math.floor(m), math.floor(n)) in self.tiles
       
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        totalTile = self.width*self.height
        return totalTile

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.tiles)
        
    def getRandomPosition(self):
        """
        Return a random position inside the room.
        
        returns: a Position object.
        """
        return Position(random.randrange(self.width), random.randrange(self.height))
        
    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.
        
        pos: a Position object.
        returns:True if pos is in the room, False otherwise.
        """
        if (pos.getX() < self.width and pos.getY() < self.height and pos.getY() >= 0 and pos.getX() >= 0):
            return True
        else:
            return False

class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room ## do we declare room is an object of RectangularRoom?
        ## we are told room is a RectangularRoom object
        ## i guess it should be created somewhere else where room = RectangularRoom()
        self.speed = speed
        self.direction = random.randint(0,359)
        self.position = room.getRandomPosition()  #performs getRandomPosition
        # how do we know size of room?
        # init means the size of the room must be given when the object is created?
        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return  self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!

# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having been cleaned.
        """
        position = self.getRobotPosition()
        newPosition = position.getNewPosition(self.getRobotDirection(),self.speed)
        ## originally i tried self.position = position.getNewPosition()
	if self.room.isPositionInRoom(newPosition):
	   self.setRobotPosition(newPosition)
	   if not self.room.isTileCleaned(math.floor(newPosition.getX()),math.floor(newPosition.getY())):
	       self.room.cleanTileAtPosition(newPosition)
	else: 
	     self.setRobotDirection(random.randint(0,359))
	       
	## originally tried self.cleanTileAtPosition

# Uncomment this line to see your implementation of StandardRobot in action!
# testRobotMovement(StandardRobot, RectangularRoom)

# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    
    trialsList = []
    #run num_trials amount of trials
    for trial in range(num_trials):
    #create list of robots    
    #create room
        room = RectangularRoom(width,height)
    #create list of robots that will be cleaning the room  
        botList = []
        for n in range(num_robots):
            botList.append(robot_type(room,speed))

    #create step counter
        steps = 0        
    #while room is not clean, clean room    
        while (1.0*room.getNumCleanedTiles()/room.getNumTiles() <= min_coverage):
    # for each robot clean the position of the robot
            for bot in botList:
                bot.updatePositionAndClean()
            steps +=1
        trialsList.append(steps)
    return float(sum(trialsList)/len(trialsList))        

# Uncomment this line to see how much your simulation takes on average
print  runSimulation(1, 1.0, 10, 10, 0.9, 30, StandardRobot)
