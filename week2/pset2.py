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

