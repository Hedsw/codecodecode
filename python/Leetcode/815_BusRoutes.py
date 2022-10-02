class Solution:
    
    # Time Comp - O(N^2) 
    # Space Comp - O(N^2)
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
	# stop2bus means what bus(es) is/are available at each stop
        stop2bus = defaultdict(list)
	# bus2stop means which stop(s) does each bus go
        bus2stop = dict()
        
        for idx, val in enumerate(routes):
            for stop in val:
                stop2bus[stop].append(idx)
            bus2stop[idx] = val[:]
            
        q = deque([source])
        seenBus = set([-1])
        seenStation = set([source])
        
        res = 0
        while q:
            # Setting up BFS with counter
            N = len(q)
            for i in range(N):
                # What station am I currently at?
                station = q.popleft()
                # Have I reached the target already?
                if station == target:
                    return res
                # What buses are available here?
                buses = stop2bus[station]
                for bus in buses:
                    # Did i take this bus just now already?
                    if bus in seenBus:
                        continue
                    seenBus.add(bus)
                    # For each bus, where can I go?
                    for reachable_stop in bus2stop[bus]:
                        # Did I come this stop already? If yes, there is no need to explore it.
                        if reachable_stop in seenStation:
                            continue
                        q.append(reachable_stop)
                        seenStation.add(reachable_stop)
            res += 1
        return -1