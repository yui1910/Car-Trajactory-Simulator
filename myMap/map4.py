class Map:
    def __init__(self):
        
        self.x = 2
        self.y = 2    
        self.path = [   [(0, 1), (1, 1), (2, 1), (3, 1)],
                        [(0, 1), (1, 1), (2, 1), (2, 2), (2, 3)],
                        [(3, 2), (2, 2), (1, 2), (0, 2)],
                        [(3, 2), (2, 2), (2, 3)],
                        [(1, 0), (1, 1), (1, 2), (1, 3)]        ]
                        

        self.zone_list = [(0, 0), (1, 0),
                          (0, 1), (1, 1)        ]

        self.tunnel_list = [ ]

    def getPathCount(self):
        return len(self.path)
    def getPath(self):
        return self.path
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getZone(self):
        return self.zone_list
    def getTunnel(self):
        return self.tunnel_list
