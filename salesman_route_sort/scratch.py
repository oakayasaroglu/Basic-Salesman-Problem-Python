memo=73489

citydistance=[[0,11,22,14,8,20,16,19,18,14],
              [16,0,18,1,1,5,25,6,14,13],
              [20,8,0,23,14,9,7,23,8,10],
              [14,11,3,0,5,17,22,1,20,16],
              [18,12,4,15,0,15,18,13,8,10],
              [2,15,19,7,12,0,2,5,14,6],
              [16,25,7,22,13,2,0,8,4,10],
              [19,6,20,21,5,15,18,0,14,15],
              [18,24,6,2,8,4,14,4,0,5],
              [17,3,11,13,5,2,20,6,5,0]]

for a in range(10):
	for b in range(10):
		if a!=b:
			for c in range(10):
				if a!=c and b!=c:
					for d in range(10):
						if a!=d and b!=d and c!=d:
							for e in range(10):
								if a!=e and b!=e and c!=e and d!=e:
									for f in range(10):
										if a!=f and b!=f and c!=f and d!=f and e!=f:
											for g in range(10):
												if a!=g and b!=g and c!=g and d!=g and e!=g and f!=g:
													for h in range(10):
														if a!=h and b!=h and c!=h and d!=h and e!=h and f!=h and g!=h:
															for i in range(10):
																if a!=i and b!=i and c!=i and d!=i and e!=i and f!=i and g!=i and h!=i:
																	for j in range(10):
																		if a!=j and b!=j and c!=j and d!=j and e!=j and f!=j and g!=j and h!=j and i!=j:
																			routedistance=citydistance[a][b]+citydistance[b][c]+citydistance[c][d]+citydistance[d][e]+citydistance[e][f]+citydistance[f][g]+citydistance[g][h]+citydistance[h][i]+citydistance[i][j]+citydistance[j][a]
																			if memo>routedistance:
																				memo=routedistance
																				bestroute=[a+1,b+1,c+1,d+1,e+1,f+1,g+1,h+1,i+1,j+1,a+1]


print ('Shortest route:', bestroute)
print ('Distance: ', memo)

xyz=input()
