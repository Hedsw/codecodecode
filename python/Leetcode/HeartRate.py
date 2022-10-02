import heapq

# Maximum HeartRate for hikers in 2KM
class limitation:
    distance = 2000

class hiker:
    def __init__(self, personid):
        self.personid = personid
        self.heartbeat = {} # key - distance, value - heartbeat 
        self.distanceinLimitation = []
    
    def checkHeartbeat(self, heartbeat, currentdistance):
        self.heartbeat[currentdistance] = heartbeat
        
    def getMaximumHeartBeat(self, limit_distance):
        for i in self.heartbeat: # Distance체크
            if i < limit_distance: # 마지막 2KM 
                self.distanceinLimitation.append(self.heartbeat[i])
               
        heapq._heapify_max(self.distanceinLimitation)
        return heapq._heappop_max(self.distanceinLimitation)

class hikers:
    def __init__(self):
        self._hikers = [] 
    
    def addUsers(self, hiker):
        self._hikers.append(hiker)


def main():
    maximumHeartRate = 0 
    hikersobj = hikers()

    hiker1 = hiker(1)  
    hikersobj.addUsers(hiker1)

    hikersobj._hikers[0].checkheartbeat(210, 64000)
    
    # Once finish to add heartbeat, call getMaximumHeartBeat
    for i in range(0, len(hikersobj._hikers)):
        if maximumHeartRate < hikersobj.hikers[i].getMaximumHeartBeat(limitation.distance):
            maximumHeartRate = hikersobj.hikers[i].getMaximumHeartBeat(limitation.distance)
    
    return maximumHeartRate
