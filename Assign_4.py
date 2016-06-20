gdf = open('vasham.gdf', 'r')
output = open('output.json', 'w')
dict = {}
a=0
firstline= "{\"nodes\": ["
names = "{\"name\":\""
nameend = "\"}"
edges = "\"links\": ["
sources = "{\"source\": "
target = ",\"target\": "
value = ",\"value\": "
stend = "}"
x = ""
g="\"group\":"
output.write(firstline)
for line in gdf:
    if line.startswith('nodedef>name'):
        continue
    if line.startswith('edgedef>node1'):
        y = "]," + "\n" + edges
        break
    lane = line.rstrip('\n').split(",")
    group = lane[2][0:3]
    if group == "pos":
        group = group + "t"
    else:
        group = group + "r"
    if lane[0] not in dict.items():
        a = a + 1
        dict[lane[0]] = a
    x = x + "\n" + names + lane[0]  + "\"," + g + "\"" +group + nameend + ","
    p = x[:-1]
z = ""
for line in gdf:
    lane = line.rstrip('\n').split(",")
    if lane[0] in dict.keys():
        if lane[1] in dict.keys():
            z = z + "\n" + sources + str(dict[lane[0]]) + target + str(dict[lane[1]])  + stend + ","
output.write(p)
output.write(y)
output.write(z[:-1] + "]}")