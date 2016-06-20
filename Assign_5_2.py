gdf = open('vasham.gdf', 'r')
output = open('pajek.paj', 'w')
output1 = open('pajek.net', 'w')
dict  = {}
a = 0
list = []
for line in gdf:
    if line.startswith('nodedef>name'):
        continue
    if line.startswith('edgedef>node1'):
        break
    lane = line.rstrip('\n').split(',')
    list.append(lane)
    if lane[0] not in dict.keys():
        a = a + 1
        dict[lane[0]] = a
b = len(dict.keys())
vertices = "*vertices" + " " + str(b)
e = vertices + '\n'
for i in list:
    c = dict[i[0]]
    d = i[0]
    e = e + str(c) + ' ' + d + '\n'
e = e + '*edges' + '\n'
for j in gdf:
    k = j.rstrip('\n').split(',')
    e = e + str(dict[k[0]]) + ' ' + str(dict[k[1]]) + '\n'
print(e)
output.write(e)
output1.write(e)
output.close()
output1.close()