	
#akhil jarodia 2017130 B1
def dijkstra(Graph,source):
	
	dist=[]
	prev=[]
	q=[]
	
	from math import inf
	for i in range(len(Graph[1])):
		dist.append(inf)
		q.append(i)
	dist[source]=0	
	from copy import deepcopy
				
	

	while len(q)>0:
		
		t=[]
		for i in q:
			t.append(dist[i])
		u=q[t.index(min(t))]	
		
		
		q.remove(u)
		
		
		
		for r in Graph[0][u]:
			alt=dist[u]+Graph[1][u][Graph[0][u].index(r)]
			if alt<dist[r]:
				dist[r]=alt
		


		
		
	return dist
        	


def bfs(Graph, s): 
  	#n is the total number of nodes
        visited[:n] = [False] 

        queue = [] 
        queue.append(s) 
        visited[s] = True
  
        while queue: 
            s = queue.pop(0) 
            print (s, end = " ") 
            for i in Graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
	
if __name__=='__main__'	:	
	n=int(input())#no of vertex

	f=[]
	e=[]
	for i in range(n):
		b=[]
		c=int(input())
		a=[]
		for j in range(c):
			d=input().split()
			d=list(map(int,d))	
			b.append(d[0])
			a.append(d[1])
		e.append(b)#connection to diff tiles	
		f.append(a)#weights
	g=[]#graph
	g.append(e)
	g.append(f)
	t=input("Enter source :")
	t=int(t)
	print(bfs(g,t))
	print(dijkstra(g,t))
		
		
		


			
