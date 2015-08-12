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
