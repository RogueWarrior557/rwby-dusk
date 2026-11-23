"""Compose hand-placed layer segments into a full .pxs grid (authoring helper)."""
import sys
W=H=32
def blank(): return [['.']*W for _ in range(H)]
def paint(grid, segs, dy=0, dx=0):
    for y,x,pat in segs:
        for i,ch in enumerate(pat):
            if ch!='.':
                X,Y=x+i+dx,y+dy
                assert 0<=X<W and 0<=Y<H,(y,x,pat)
                grid[Y][X]=ch
    return grid
shield=[(14,6,"oooooo"),(15,4,"oodddccc"),(16,3,"oddhhhhgg"),(17,3,"odhhhuggg"),
(18,2,"odhhguwugg"),(19,2,"ochguvwvug"),(20,2,"ocggguvugf"),(21,2,"ocggggugff"),
(22,3,"obgggffff"),(23,3,"obbfffffb"),(24,4,"oobbbbbb"),(25,6,"oooooo")]
body=[(2,14,"ooo"),(3,12,"ohiiho"),(4,10,"ohhggggo"),(5,9,"ohgfooooooo"),
(6,9,"ogfodeedccco"),(7,9,"ofodeeddcccbo"),(8,10,"ooddddcccbbo"),(9,11,"oddccccbbbo"),
(10,11,"occcbooCooo"),(11,11,"occbbcdcbbo"),(12,11,"obcbbbcbbao"),(13,12,"obbabbbao"),
(14,12,"oabccbao"),(15,11,"ocddcccddco"),(16,11,"obcghhgccbo"),(17,11,"obcghggbcbo"),
(18,11,"oabgggfabcc"),(19,11,"onppvppnoo"),(20,11,"ofghggffo"),(21,11,"ofghggffo"),
(22,12,"ofggffo"),(23,12,"obcbocbbo"),(24,12,"oaco.ocbo"),(25,12,"oabo.ocbo"),
(26,12,"opqo.oqpo"),(27,11,"onpqo.oqqpo"),(28,11,"ooooo.ooooo")]
sword=[(5,24,"oo"),(6,23,"oedo")]+[(y,23,"oeco") for y in range(7,17)]+[(17,22,"oodboo"),
(18,21,"ouvwwvuo"),(19,20,"obccdco"),(20,21,"ooopno"),(21,23,"ovuo"),(22,24,"oo")]
g=blank(); 
for layer in (shield,body,sword): paint(g,layer,dy=2)
print("\n".join("".join(r) for r in g))
