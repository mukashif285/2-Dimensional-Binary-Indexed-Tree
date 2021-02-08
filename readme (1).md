# Two Dimensional Binary Indexed Trees:

##### Fenwick Tree is used to answer range or interval queries in an array in logarithmic time. Fenwick tree can be generalized to multiple dimensions. 2D Fenwick tree is one such implementation used to answer sub-matrix queries, i.e. queries in 2 dimensions. Fenwick tree is considered a prerequisite to understand 2D Fenwick tree. Like 1D, 2D Fenwick tree also requires the operation to be invertible.

### 1. Sum of sub-matrix bound by coordinates (x1, y1) and (x2, y2) is given by:

**sum((x1, y1), (x2, y2)) = sum((0, 0), (x2, y2)) - sum((0, 0), (x1 - 1, y2)) - sum((0, 0), (x2, y1 - 1)) + sum((0, 0), (x1 - 1, y1 - 1))**

### 2. Sub-matrix product, the general method would still be same:


**Prod ((x1, y1), (x2, y2)) = Prod((0, 0),(x2, y2))// (Prod((0, 0), (x1 - 1, y2) * Prod((0, 0), (x2, y1-1) * Prod((0, 0), (x1-1, y1 - 1)**

`Queries of the form - x1, y1, x2, y2 `

_For example the query- {1, 1, 3, 2} means the sub-matrix-_ 

        y 
        /\ 
    1   |       1 2 3 4      Sub-matrix       
    2   |       5 3 8 1      {1,1,3,2}      --->     1 2 3 
    3   |       4 6 7 5                              5 3 8 
    4   |       2 4 8 9 
        | 
     -- |------ 1 2 3 4 ----> x 
        | 



**Hence sum of the sub-matrix will be = 1+2+3+5+3+8 =  22**  
**And Product of sub-matrix will be  = 1x2x3x5x3x8 =  720**
    