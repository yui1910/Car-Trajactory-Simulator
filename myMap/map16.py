class Map:
    def __init__(self):
        self.x = 5
        self.y = 5    
        self.path = [   [(6, 2), (5, 2), (4, 2), (3, 2), (2, 2), (1, 2), (0, 2)],
                        [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4)],
                        [(6, 2), (5, 2), (4, 2), (3, 2), (2, 3), (2, 4), (2, 5), (2, 6)],
                        [(0, 4), (1, 4), (2, 4), (3, 4), (4, 3), (4, 2), (4, 1), (4, 0)],
                        [(4, 6), (4, 5), (5, 4), (6, 4)],
                        [(2, 0), (2, 1), (1, 2), (0, 2)]    ]

        self.zone_list = [        (1, 0),         (3, 0),
                          (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
                                  (1, 2),         (3, 2),
                          (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
                                  (1, 4),         (3, 4)         ]
        self.tunnel_list = [    [(1, 0), (0, 1)], [(3, 0), (4, 1)], [(0, 3), (1, 4)], [(3, 4), (4, 3)],
                                [(2, 1), (1, 2)], [(2, 3), (1, 2)], [(2, 1), (3, 2)], [(3, 2), (2, 3)]  ]

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
