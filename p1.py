
from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop

def dijkstras_shortest_path(src, dst, graph, adj):
	Dist = {}
	Prev = {}
	#and another one to check if nodes have been fully processed
	Processed = {}
	Dist[src] = 0
	queue = [(0,src)]
	
	found = False
	
	#while queue is not empty. If it's empty we've searched all valid points
	while(queue):
		curr = heappop(queue)
		Processed[curr[1]] = True
		#print "Popping %s with Distance" %(curr[1],)
		nextCells = navigation_edges(graph, curr[1])
		for i in range(0, len(nextCells)):
			if not (nextCells[i][1] in Processed):
				#update the distance in the current tuple
				nextCells[i] = (nextCells[i][0] + Dist[curr[1]], nextCells[i][1])
				#check if distance needs updating in the dict
				if not (nextCells[i][1] in Dist) or (Dist[nextCells[i][1]] > nextCells[i][0]):
					Dist[nextCells[i][1]] = nextCells[i][0]
					Prev[nextCells[i][1]] = curr[1]
					#push onto the queue
					heappush(queue, nextCells[i])
					if nextCells[i][1] == dst:
						found = True
						break
		if found:
			break
			
	if found:
		path = []
		curr = Prev[dst]
		while curr != src:
			path.append(curr)
			curr = Prev[curr]
		return path
			
			
		
		

def navigation_edges(level, cell):
	validCells = []
	x, y = cell
	for dx in [-1,0,1]:
		for dy in [-1,0,1]:
			next_cell = (x + dx, y + dy)
			dist = sqrt(dx*dx+dy*dy)
			if dist > 0 and next_cell in level['spaces']:
				validCells.append((dist, next_cell))
				
	return validCells
	

def test_route(filename, src_waypoint, dst_waypoint):
	level = load_level(filename)

	show_level(level)

	src = level['waypoints'][src_waypoint]
	dst = level['waypoints'][dst_waypoint]

	path = dijkstras_shortest_path(src, dst, level, navigation_edges)

	if path:
		show_level(level, path)
	else:
		print "No path possible!"

if __name__ ==  '__main__':
	import sys
	_, filename, src_waypoint, dst_waypoint = sys.argv
	test_route(filename, src_waypoint, dst_waypoint)
