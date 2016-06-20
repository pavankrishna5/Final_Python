def gdf_to_gml(gdf, gml):
    header1 = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + '\n' + "<graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\""
    header2 = '\t' + '\t' + 'xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"' + '\n' + '\t' + '\t' + "xsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlns" + '\n' + '\t' + '\t' + "http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd\">"
    header = header1 + '\n' + header2
    head = '\t' + "<graph id=\"G\" edgedefault=\"undirected\">" + '\n'
    e = '\t' + '\t'
    f = ''
    nodeId = "<node id=\""
    nodeEnd = "\"/>"
    es = "<edge source=\""
    t = "\" target=\""
    tn = "\"/>"
    for line in gdf:
        lane = line.rstrip('\n').split(',')
        if line.startswith('nodedef>name'):
            continue
        if len(lane)>4:
            e = e + nodeId + lane[0] + nodeEnd + '\n' + '\t' + '\t'
        elif line.startswith('edgedef>node1'):
            continue
        else:
            f = f + es + lane[0] + t + lane[1] + tn + '\n' + '\t' + '\t'
    f = f[:-1]
    g = "</graph>" + '\n' + "</graphml>"
    gm = header + '\n' + head + e + f + g
    print(gm)
    gml.write(gm)

gdf = open('vasham.gdf', 'r')
gml = open('GraphML.graphml', 'w')

gdf_to_gml(gdf, gml)
gdf.close()
gml.close()