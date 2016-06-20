import numpy as np
from random import shuffle

n=int(input())
p=float(input())
def creategraph_gml(n,p):
    header1 = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + '\n' + "<graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\""
    header2 = '\t' + '\t' + 'xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"' + '\n' + '\t' + '\t' + "xsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlns" + '\n' + '\t' + '\t' + "http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd\">"
    header = header1 + '\n' + header2
    n1 = round((n*(n-1)/2)*p)
    n0 = (n*(n-1)/2) - n1
    l1 = np.ones((n1,), dtype=np.int)
    l0 = np.zeros((n0,), dtype=np.int)
    list = []
    list.extend(l0)
    list.extend(l1)
    shuffle(list)
    gml = open('gml1.graphml', 'w')
    arr = np.zeros(shape=(n,n), dtype=np.int32)
    k=0
    gml.write(header)

    gml.write('  <graph id = "G" edgedefault = "undirected>'+'\n')
    for nodes in range(0,n):
        gml.write('    <node id=\"'+str(nodes + 1)+'\"/>\n')
    for i in range(0, n):
        for j in range(i+1,n):
            if list[k]==1:
               gml.write('    <edge source=\"'+str(i + 1)+'\" target=\"'+str(j + 1)+'\"/>\n')
            k+=1
    gml.write('  </graph>\n')
    gml.write('</graphml>')

creategraph_gml(n, p)