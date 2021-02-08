class FenwickTree:
    def __init__(self, Column, Row):
        self.fenwicktree = [[0 for i in range(Column + 1)] for j in range(Row + 1)]
        self.Column = Column
        self.Row = Row

    
    def LSB(self, x):                                       # Function to get least significant bit 
        return x & (-x)     
 
    def Update(self, x, y, val):                            # A function to update the 2D BIT 
        x1 = x
        while x1 <= self.Row:           
            y1 = y
            while y1 <= self.Column:                        # This loop update all the 1D BIT inside the 
                self.fenwicktree[x1][y1] += val             # array of 1D BIT = ft[x] 
                y1 += self.LSB(y1)
            x1 += self.LSB(x1)
        
    def GetSum(self, y, x):                                 # A function to get sum from (0, 0) to (x, y) 
        Sum = 0
        x1 = x
        while x > 0:
            y1 = y
            while y1 > 0:                                   #This loop sum through all the 1D BIT 
                Sum += self.fenwicktree[x][y1]              # inside the array of 1D BIT = ft[x] 
                y1 -= self.LSB(y1)                      
            x -= self.LSB(x)
        return Sum

    def Querying(self, x1, y1, x2, y2):                     #x1 and y1 co-ordinates of bottom left 
                                                            #x2 and y2 co-ordinates of top right 
        return (
            self.GetSum(x2, y2) - self.GetSum(x1 - 1, y2) - 
            self.GetSum(x2, y1 - 1) + self.GetSum(x1 - 1, y1 - 1)
                )

    def Construct(self, matrix):                            #A function to create an auxiliary matrix 
        self.Column = len(matrix)                           #from the given input matrix 
        self.Row = len(matrix[0])
        for i in range(self.Row):
            for j in range(self.Column):
                self.Update(i + 1, j + 1, matrix[i][j])
    
    def Print(self):                                        # A function to print the matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=" ")
            print("\n")

    def Sum_Result(self,x1, y1, x2, y2):                    # A function to print the sum of sub matric query
        self.Construct(matrix)
        print("The Sum of the submatrix of the given co ordinates will be             : ",x.Querying(x1, y1, x2, y2))

    

class FenwickTree2:
    def __init__(self, Row,Column):
        self.fenwicktree = [[1 for i in range(Row + 1)] for j in range(Column + 1)]
        self.Column = Column
        self.Row = Row

    
    def LSB(self, x):                                       # Function to get least significant bit
        return x & (-x)     

    def Update(self, x, y, val):
        x1 = x
        while x1 <= self.Row:                               # This loop update all the 1D BIT inside the
            y1 = y                                          # array of 1D BIT = ft[x]
            while y1 <= self.Column:
                self.fenwicktree[x1][y1] *= val
                y1 += self.LSB(y1)
            x1 += self.LSB(x1)

    def prod(self, x, y):                                   # A function to get Product from (0, 0) to (x, y) 
        Prod = 1
        x1 = x
        while x > 0:                                        # This loop product through all the 1D BIT
            y1 = y                                          # inside the array of 1D BIT = ft[x]
            while y1 > 0:
                Prod *=self.fenwicktree[x][y1]          
                y1 -= self.LSB(y1)                      
            x -= self.LSB(x)
        return Prod


    def Product(self,x1,y1,x2,y2):                          # x1 and y1 co-ordinates of bottom left 
                                                            # x2 and y2 co-ordinates of top right 
                                                            # The general method if we wanted sub-matrix product:
        return ( ((self.prod(x2, y2))// ((self.prod (x1 - 1, y2)* self.prod (x2, y1-1))) * self.prod (x1-1, y1 - 1)) )                                        
            
                    
        
    def Construct(self, matrix):                            # A function to create an auxiliary matrix 
        self.Column = len(matrix[0])                        # from the given input matrix 
        self.Row = len(matrix[0])
        for i in range(self.Row):
            for j in range(self.Column):
                self.Update(i + 1, j + 1, matrix[i][j])

    def Print(self):                                        # A function to print the matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=" ")
            print("\n")

    def Prod_Result(self,x1, y1, x2, y2):                   # A function to print the product of sub matric query
        self.Construct(matrix)
        print("The product of the submatrix of the given co ordinates will be         : ",y.Product(x1, y1, x2, y2))


        
#Driver Code
if __name__ == "__main__":

    matrix = [  
            [1, 2, 3, 4],
            [5, 3, 8, 1],
            [4, 6, 7, 5],
            [2, 4, 8, 9]
                        ]


# x= FenwickTree(4, 4)
# y= FenwickTree2(4, 4)

# print ("The matrix is : ")
# print ()
# x.Print()
# x.Sum_Result(1, 1, 3, 2)
# print()
# y.Prod_Result(1 ,1, 3, 2)







