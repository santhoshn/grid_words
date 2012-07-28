#!/usr/bin/python
import time

wgrid=[['a', 'b'],
	  ['c', 'd']]

dirs=[[1,0], [0,1], [-1,0], [0,-1]]  # d,r,u,l
cnt_val={2:2, 3:3, 4:3, 5:3, 6:2}
vgrid_val={2:6, 3:4, 4:5}
ncnt_val={2:2, 3:2, 4:3}

def print_grid(g):
	if 0:
		for i in range(len(g)):
			print g[i]
		print ""
		time.sleep(1)
	return

def print_str(str):
	print str
	return

def gridval(g, x, y):
	gw,gh=len(g[0]),len(g)
	if x>=0 and x<gh and y>=0 and y<gw:
		return g[x][y]
	else:
		return -1

def grid_words_xy(grid, x, y):
	vgrid=[[0 for g in grid[0]] for h in grid]
	gw,gh=len(vgrid[0]),len(vgrid)

	px,py=x,y
	str=""
	bfg=1
	while bfg:
		bfg=0
		# Fill empty cells starting from px and py. The 
		# value at a cell will be equal to the number of 
		# surrounding cells, which are empty.
		#print "Fill cells px=%d py=%d"%(px,py)
		ffg=1
		while ffg:
			ffg=0
			npx=npy=cnt=0
			for k in range(len(dirs)):
				dx,dy=dirs[k][0],dirs[k][1]
				if gridval(vgrid, px+dx, py+dy)==0:
					cnt+=1
					if ffg==0:
						npx,npy=px+dx,py+dy
					ffg=1
			vgrid[px][py]=cnt
			str+=grid[px][py]
			print_str(str)
			if cnt:
				px,py=npx,npy
			print_grid(vgrid)

		# Track back
		#print "Backtrack px=%d py=%d"%(px,py)
		tfg=1
		while tfg:
			tfg=0
			for i in range(len(dirs)):
				npx,npy=px+dirs[i][0],py+dirs[i][1]
				gval=gridval(vgrid, npx, npy)

				if gval==1:
					px,py=npx,npy
					vgrid[px][py]=0
					str=str[:-1]
					tfg=1
					break
				
				if gval==2 or gval==3 or gval==4:
					cnt=0
					for k in range(len(dirs)):
						if gridval(vgrid, npx+dirs[k][0], npy+dirs[k][1])==0:
							cnt+=1
					if cnt==cnt_val[gval]:	
						px,py=npx,npy
						vgrid[px][py]=vgrid_val[gval]
						str=str[:-1]
						
						ncnt=0
						for k in range(len(dirs)):
							dx,dy=dirs[k][0],dirs[k][1]
							if gridval(vgrid, px+dx, py+dy)==0:
								ncnt+=1
								if ncnt==ncnt_val[gval]:
									px,py=px+dx,py+dy
									bfg=1
									break
						break
				
				if gval==5 or gval==6:
					cnt=0
					for k in range(len(dirs)):
						if gridval(vgrid, npx+dirs[k][0], npy+dirs[k][1])==0:
							cnt+=1
					if cnt==cnt_val[gval]:	
						px,py=npx,npy
						vgrid[px][py]=0
						str=str[:-1]
						tfg=1
						break
			#print_str(str)
			print_grid(vgrid)

def grid_words(grid):
	for i in range(len(grid[0])):
		for j in range(len(grid)):
			grid_words_xy(grid,i,j)

print_grid(wgrid)
grid_words(wgrid)
