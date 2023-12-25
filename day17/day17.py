from heapq import *
from typing import Self
from typing import Dict
from typing import List
from typing import Tuple

up, down, left, right, start = -1+0j, 1+0j, 0-1j, 0+1j, 0+0j

class State:
    def __init__(self, pos: complex=0, steps: int=0, dir: complex=start):
        self.pos = pos
        self.steps = steps
        self.dir = dir
    def __key(self):
        return (self.pos, self.steps, self.dir)
    def __eq__(self,other):
        return self.__key() == other.__key()
    def __hash__(self):
        return hash(self.__key())
    def __repr__(self):
        return (f'pos {self.pos}, steps {self.steps}, dir {self.dir}')

with open('input.txt', 'r') as file:
    grid = file.read().splitlines()
    grid = [[int(x) for x in list(line)] for line in grid]

m,n = len(grid), len(grid[0])

Q: List[Tuple[int, int, State, State]] = []

def push(cost: int, state: State, pred: State):
    push.counter += 1
    heappush(Q, (cost, push.counter, state, pred))
push.counter = 0

push(0, State(), State(pos=-1-1j))
D: Dict[State, int] = {}
P: Dict[State, State] = {}

while len(Q) > 0:
    cost, counter, current_state, pred = heappop(Q)

    if current_state in D: continue

    D[current_state] = cost
    P[current_state] = pred

    cy = current_state.pos.real
    cx = current_state.pos.imag

    def add_state(dir):
        if current_state.steps==3 and dir==current_state.dir: 
            return
        
        neighbour = State(pos=current_state.pos+dir, dir=dir)
        neighbour.steps=current_state.steps+1 if current_state.dir==dir else 1

        if neighbour.pos == pred.pos:
            return
        
        if neighbour in D:
            return

        ny, nx = int(neighbour.pos.real), int(neighbour.pos.imag)
        push(D[current_state] + grid[ny][nx], neighbour, current_state)

    if cy+1 < m:
        add_state(down)
    if cy-1 >= 0:
        add_state(up)
    if cx+1 < n:
        add_state(right)
    if cx-1 >= 0:
        add_state(left)

end_pos = (m-1) + (n-1)*1j
end_nodes = [(v,k) for k,v in D.items() if k.pos==end_pos]
min_end = min(end_nodes)

print('Part1', min_end[0])


Q.clear()
push(0, State(), State(pos=-1-1j))
D = {}
P = {}

while len(Q) > 0:
    cost, counter, current_state, pred = heappop(Q)

    if current_state in D: continue

    D[current_state] = cost
    P[current_state] = pred

    cy = current_state.pos.real
    cx = current_state.pos.imag

    def add_state(dir):
        if current_state.steps==10 and dir==current_state.dir: 
            return
        
        if current_state.dir != start and current_state.steps < 4 and dir != current_state.dir:
            return
        
        neighbour = State(pos=current_state.pos+dir, dir=dir)
        neighbour.steps=current_state.steps+1 if current_state.dir==dir else 1

        if neighbour.pos == pred.pos:
            return
        
        if neighbour in D:
            return

        ny, nx = int(neighbour.pos.real), int(neighbour.pos.imag)
        push(D[current_state] + grid[ny][nx], neighbour, current_state)

    if cy+1 < m:
        add_state(down)
    if cy-1 >= 0:
        add_state(up)
    if cx+1 < n:
        add_state(right)
    if cx-1 >= 0:
        add_state(left)

# print(D)

end_pos = (m-1) + (n-1)*1j
end_nodes = [(v,i,k) for i,(k,v) in enumerate(D.items()) if k.pos==end_pos]
min_end = min(end_nodes)

print('Part2', min_end[0])