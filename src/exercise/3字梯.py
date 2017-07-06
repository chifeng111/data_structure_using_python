# coding: utf-8
from graph.graph import Graph
from basicDataStructure.myqueue import Queue


def buildGraph():
    d = {}
    g = Graph()
    # create buckets of words that differ by one letter
    with open('words4', 'r') as wfile:
        for line in wfile:
            word = line.strip()
            for i in range(4):
                bucket = word[:i] + '_' + word[i + 1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]       
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)                
    return g

def len4words():
    f = open('words4', 'w')
    with open('words', 'r') as f1:
        for line in f1:
            line = line.strip()
            if len(line) == 4:
                f.write(line.upper())
                f.write('\n')
    
    f.close()

def bfs(g, start):
    pred = {} #记录每个节点的前一个访问节点
    traveled = []
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while(vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr not in traveled:
                traveled.append(nbr)
                pred[nbr.id] = currentVert.id
                vertQueue.enqueue(nbr)
        if currentVert not in traveled:
            traveled.append(currentVert)    
    return pred

if __name__ == '__main__':
#     len4words()
    g = buildGraph()
    g.getVertex('FOOL')
    pred = bfs(g, g.getVertex('FOOL'))
#     print(pred)
    def traverse(x):
        y = x
        while y in pred:
            print(y, end = " ")
            y = pred[y] 
        print(y)

    traverse('HOPE')
        
        
        
        
        
        
        
        
        
        
        