stops 		= [] #initialize two blank arrays, for stops
conn = [] #and conn
sfile = open("curved_stops","r")       #open the plain text files
cfile = open("curved_connections","r")
for line in sfile.readlines():				  #for each line in the
	stops	   .append(line[:-1].split(", ")) #readfiles, split by
for line in cfile.readlines():                #commas, erase the \n
	conn.append(line[:-1].split(", ")) #and add to the arrays

sarr=[] #array of stops, for json
for i in stops:	#compile
	sarr.append("\t\t{\"name\":\""
		+ i[0] + "\", \"type\":\""
		+ i[2] + "\", \"boro\":\""
		+ i[3] + "\", \"deg\":"
		+ str(len(i[1])) + "},\n")
sarr[len(sarr)-1] = sarr[len(sarr)-1][:-2] + "\n" #erase last comma

def index(a, b): #returns the index of the listing for a given stop name
	for i in range(len(stops)):
		if (a == stops[i][0]) and (b in stops[i][1]): return i

carr=[]
for i in range(len(conn)):
	if (conn[i][0] == ""):
		conn[i][0] = conn[i-1][1]
	else: conn[i][0] = index(conn[i][0], conn[i][2])
	conn[i][1] = index(conn[i][1], conn[i][2])

for i in conn:
	carr.append("\t\t{\"source\":"
		+ str(i[0]) + ", \"target\":"
		+ str(i[1]) + ", \"line\":\""
		+ str(i[2]) +"\"},\n")
carr[len(carr)-1] = carr[len(carr)-1][:-2] + "\n"

json = open('curvedjsondata.json','w')
json.write("{\n\t\"nodes\":[\n")
for i in sarr:
	json.write(i)
json.write("\t],\n \t\"links\":[\n")
for i in carr:
	json.write(i)
json.write("\t]\n}")
