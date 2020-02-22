from csp import *
import itertools
import time

#function that returns a list of cartesian products
def cartesianProduct(pList):
    if pList == []:
        return [()]

    prodList = []

    for i in cartesianProduct(pList[:-1]):
        for j in pList[-1]:
            prodList.append(i + (j,))

    return prodList

#Kakuro puzzle modelisation class
class Kakuro_Modelisation():

    def __init__(self, lineValue, blankSquares):
        self.lineValue = lineValue
        self.blankSquares = blankSquares
        self.variables = None
        self.domains = None
        self.neighbors = None
        
    #method that sets variables depending on the length of the line value plus the number of blank squares 
    def setVariables(self):
        vars = []
        
        for i in range(len(self.lineValue) + self.blankSquares):
            vars.append(i + 1)
  
        self.variables = vars

    #method that sets domains by using the wanted line value and the number of blank squares
    def setDomains(self):
        domains = {}
 
        for i in range(self.blankSquares):  #set domains of blank squares
            domains[i + 1] = [1,2,3,4,5,6,7,8,9]
            
        for i in range(len(self.lineValue)):    
            productList = [] 
            
            for j in self.lineValue[i]:
                
                if type(j) != int: 
                    productList.append(domains[i + 1])
                    
            totalValues = cartesianProduct(productList) #calculate the cartesian products
            fixedValues = []

            for value in totalValues:
                    
                makeS = sum(value)  #calculate current item's sum
                
                if makeS == self.lineValue[i][-1]: #if value is valid
                    newValue = list(value)
                    
                    newValue.append((self.lineValue[i][0:len(self.lineValue[i]) - 1]))  #push variables in list
                    fixedValues.append(newValue)

            domIndex = i + (self.blankSquares + 1)  #index
            domains[domIndex] = fixedValues

            self.domains = domains

    #method that sets neighbors by using the wanted line value and the number of blank squares
    def setNeighbors(self):
            neighbors = {}

            for i in range(self.blankSquares):  #fix blank squares variables
                nList = [] #neighbors list
                sumIndex = 0 #index of checked sum

                for value in self.lineValue:
                    if "x" + str(i + 1) in value: #if variable exists in the sum of current line value
                        for val in value: 
                            if (type(val) != int) and (val != ("x" + str(i + 1))):   #ignore current variable and the line value
                                nList.append(int(val[1:])) #push neighbor to list

                        nList.append(sumIndex + (self.blankSquares + 1))
    
                    sumIndex += 1

                nList.sort() #sort neighbors list

                neighbors[i + 1] = nList

            for i in range(len(self.lineValue)):    #find variable's neighbors for each variable in a blank line
                nList = [] #neighbors list

                for value in self.lineValue[i]:
                    if type(value) != int: #ignore line value
                        nList.append(int(value[1:])) #push value's id in the list 

                nList.sort()    #sort neighbors list

                neigIndex = i + (self.blankSquares + 1) #index
                neighbors[neigIndex] = nList

            self.neighbors = neighbors

    #method that checks if values are valid (A,B must be neighbors)
    def setConstraints(self, A, a, B, b):
        
        #if A,B are blank squares
        if (type(a) == int) and (type(b) == int):
            return a != b   #neighbors must have different values

        if type(a) == int:   #if A is blank square
            index = 0

            for var in b[-1]:
                if A == int(var[1:]): #keep only variable id
                    if b[index] == a: #if id is found return True
                        return True
                    
                index += 1

        if type(b) == int:   #if A is blank square
            index = 0

            for var in a[-1]:
                if B == int(var[1:]):   #keep only variable id  
                    if a[index] == b: #if id is found return True
                        return True
                    
                index += 1

        return False
  
    def getBlankSquares(self):
        return self.blankSquares

    def getVariables(self):
        return self.variables

    def getDomains(self):
        return self.domains

    def getNeighbors(self):
        return self.neighbors

#Kakuro puzzle solver class 
class Kakuro_Solver(CSP):

    #constructor of the class
    def __init__(self, variables, domains, neighbors, constraints, blankSquares):
        self.blankSquares = blankSquares 

        CSP.__init__(self,variables,domains,neighbors,constraints)  #call CSP's constructor

    #method that solves the puzzle using forward checking algorithm with minimum remaining values and least constraining value heuristics
    def FC_MRV_LCV(self):

        start = time.time() #start of algorithm's execution

        result = backtracking_search(self,select_unassigned_variable=mrv,order_domain_values=lcv,inference=forward_checking)

        end = time.time()   #end of algorithm's execution

        if result:
            i = 0
            
            print("The correct solution of the puzzle is:\n")

            while i < self.blankSquares:
                print("x" + str(i + 1) + " = " + str(result[i + 1]), end = "\t")
                i += 1
                if i % 10 == 0:
                    print("\n", end = "")

            runTime = round(end - start,5)

            print("\n\nThe puzzle is solved in " + str(runTime) + " seconds (using FC with MRV and LCV heuristics)")
            print("Extra assignments made before solving the puzzle with FC: " + str(self.nassigns - self.blankSquares) + "\n")

        else:
            print("This puzzle can not be solved\n")

    #method that solves the puzzle using maintaining arc consistency algorithm with minimum remaining values and least constraining value heuristics
    def MAC_MRV_LCV(self):

        start = time.time() #start of algorithm's execution

        result = backtracking_search(self,select_unassigned_variable=mrv,order_domain_values=lcv,inference=mac)

        end = time.time()   #end of algorithm's execution

        if result:  
            runTime = round(end - start,5)

            print("\nThe puzzle is solved in " + str(runTime) + " seconds (using MAC with MRV and LCV heuristics)")
            print("Extra assignments made before solving the puzzle with MAC: " + str(self.nassigns - self.blankSquares) + "\n\n")

        else:
            print("This puzzle can not be solved\n")
         
#Below we present 7 kakuro puzzles of different grid size and game difficulty
#The first puzzle is the one given in the homework
#The rest of them can be found in the following link: https://www.kakuroconquest.com

#Homework puzzle (Grid 4 x 3 very easy)
puzzle1 = [ ["x1","x2",3], ["x3","x4","x5","x6",10], ["x7","x8",3], ["x1","x3",4], 
            ["x2","x4",3], ["x5","x7",6], ["x6","x8",3]
        ]
blank1 = 8

#Grid 8 x 8 easy 
puzzle2 = [ ["x1","x2","x3",7], ["x4","x5",3], ["x6","x7","x8",6],
            ["x9","x10","x11","x12",10], ["x13","x14","x15","x16","x17",15],
            ["x18","x19",4], ["x20","x21",4], ["x22","x23",4],
            ["x24","x25",4], ["x26","x27",3], ["x28","x29",3], 
            ["x30","x31","x32","x33","x34",15], ["x35","x36","x37","x38",11], 
            ["x39","x40","x41",14], ["x42","x43",4], ["x44","x45","x46",7], 
            ["x1","x6","x13",6], ["x28","x35",4], ["x2","x7","x14",7], 
            ["x24","x29","x36","x42",11], ["x3","x8","x15","x20","x25",15], 
            ["x37","x43",3], ["x16","x21",4], ["x30","x38",3], ["x9","x17",4], 
            ["x26","x31",3], ["x4","x10",4], ["x22","x27","x32","x39","x44",22], 
            ["x5","x11","x18","x23",10], ["x33","x40","x45",6], ["x12","x19",3], 
            ["x34","x41","x46",9]
        ]
blank2 = 46

#Grid 8 x 8 intermediate 
puzzle3 = [ ["x1","x2",10], ["x3","x4","x5","x6",28], ["x7","x8",17], 
            ["x9","x10","x11","x12","x13",18], ["x14","x15","x16","x17",19], 
            ["x18","x19",16], ["x20","x21",14], ["x22","x23","x24",11], 
            ["x25","x26","x27",20], ["x28","x29",3], ["x30","x31",13], 
            ["x32","x33","x34","x35",25], ["x36","x37","x38","x39","x40",24],
            ["x41","x42",6], ["x43","x44","x45","x46",26], ["x47","x48",11], 
            ["x1","x7","x14",19], ["x25","x30","x36","x43",27], ["x2","x8","x15",11],
            ["x26","x31","x37","x44",10], ["x16","x20","x27",24], ["x38","x45",12], 
            ["x9","x17","x21",22], ["x39","x46",16], ["x3","x10",11], 
            ["x28","x32","x40",17], ["x4","x11",13], ["x22","x29","x33",6],
            ["x5","x12","x18","x23",26], ["x34","x41","x47",22], 
            ["x6","x13","x19","x24",15], ["x35","x42","x48",10]
        ]
blank3 = 48

#Grid 9 x 11 intermediate 
puzzle4 = [ ["x1","x2",9], ["x3","x4",9], ["x5","x6",16], ["x7","x8","x9",14],
            ["x10","x11","x12","x13","x14",24], ["x15","x16","x17","x18",10], ["x19","x20",8], 
            ["x21","x22",12], ["x23","x24",5], ["x25","x26","x27",15], ["x28","x29",8],
            ["x30","x31","x32","x33","x34",31], ["x35","x36","x37","x38","x39",30],
            ["x40","x41","x42","x43","x44",30], ["x45","x46", 15], ["x47","x48","x49",20], 
            ["x50","x51",14], ["x52","x53",13], ["x54","x55",16], ["x56","x57","x58","x59",12], 
            ["x60","x61","x62","x63","x64",32], ["x65","x66","x67",24], ["x68","x69",13],
            ["x70","x71",14], ["x72","x73",16], ["x7","x15","x21","x28",11], ["x40","x47",14],
            ["x60","x68",17], ["x1","x8","x16","x22","x29",19], 
            ["x41","x48","x54","x61","x69",17], ["x2","x9","x17",21], 
            ["x35","x42","x49","x55","x62",35], ["x18","x23",3], ["x36","x43",9],
            ["x63","x70",17], ["x3","x10",7], ["x24","x30","x37","x44","x50",34],
            ["x64","x71",13], ["x4","x11",14], ["x31","x38",8], ["x51","x56",14],
            ["x12","x19","x25","x32","x39",32], ["x57","x65","x72",20],
            ["x5","x13","x20","x26","x33",34], ["x45","x52","x58","x66","x73",28],
            ["x6","x14",10], ["x27","x34",7], ["x46","x53","x59","x67",26]
        ]
blank4 = 73

#Grid 8 x 8 hard 
puzzle5 = [ ["x1","x2","x3",23], ["x4","x5",7], ["x6","x7","x8","x9",23], 
            ["x10","x11","x12",23], ["x13","x14","x15",24], ["x16","x17","x18","x19",30],
            ["x20","x21","x22",24], ["x23","x24",16], ["x25","x26",17],
            ["x27","x28","x29",24], ["x30","x31","x32","x33",29], ["x34","x35","x36",23], 
            ["x37","x38","x39",23], ["x40","x41","x42","x43",29], ["x44","x45",16], 
            ["x46","x47","x48",15], ["x6","x13",16], ["x25","x30","x37","x44",30], 
            ["x1","x7","x14",14], ["x26","x31","x38","x45",29], ["x2","x8","x15","x20",30], 
            ["x32","x39",17], ["x3","x9",17], ["x21","x27","x33",24], ["x16","x22","x28",23], 
            ["x40","x46",16], ["x10","x17",16], ["x29","x34","x41","x47",30], 
            ["x4","x11","x18","x23",25], ["x35","x42","x48",13], 
            ["x5","x12","x19","x24",29], ["x36","x43",17]
        ]
blank5 = 48

#Grid 8 x 8 challenging 
puzzle6 = [ ["x1","x2","x3","x4",17], ["x5","x6",15], ["x7","x8","x9","x10",28], 
            ["x11","x12","x13",19], ["x14","x15",16], ["x16","x17","x18","x19",16],
            ["x20","x21","x22",20], ["x23","x24",13], ["x25","x26",13],
            ["x27","x28","x29",11], ["x30","x31","x32","x33",11], ["x34","x35",4], 
            ["x36","x37","x38",12], ["x39","x40","x41","x42",10], ["x43","x44",11], 
            ["x45","x46","x47","x48",18], ["x1","x7",6], ["x25","x30","x36","x43",11], 
            ["x2","x8","x14",22], ["x26","x31","x37","x44",20], ["x3","x9","x15","x20",26], 
            ["x32","x38",13], ["x4","x10",10], ["x21","x27","x33",20], ["x16","x22","x28",19], 
            ["x39","x45",12], ["x11","x17",4], ["x29","x34","x40","x46",11], ["x5","x12","x18","x23",27], 
            ["x35","x41","x47",6], ["x6","x13","x19","x24",23], ["x42","x48",4]
        ]
blank6 = 48

#puzzle7 takes more than 7 minutes to be solved
#Comment out puzzle7 and the corresponding tuple in the below puzzles list to test it

# #Grid 9 x 11 expert 
# puzzle7 = [ ["x1","x2",16], ["x3","x4",8], ["x5","x6","x7",11], 
#             ["x8","x9","x10","x11","x12",34], ["x13","x14","x15",18], 
#             ["x16","x17","x18","x19",14], ["x20","x21","x22",12], 
#             ["x23","x24",11], ["x25","x26","x27",10], ["x28","x29",7],
#             ["x30","x31","x32",11], ["x33","x34",13], ["x35","x36","x37","x38","x39",29],
#             ["x40","x41",14], ["x42","x43","x44",9], ["x45","x46", 8], 
#             ["x47","x48","x49",11], ["x50","x51",9], ["x52","x53","x54",19], 
#             ["x55","x56","x57","x58",10], ["x59","x60","x61",18], 
#             ["x62","x63","x64","x65","x66",30], ["x67","x68","x69",21], ["x70","x71",14], 
#             ["x72","x73",16], ["x1","x8","x16","x23",26], ["x40","x45",15],
#             ["x59","x67",16], ["x2","x9","x17","x24",15], ["x41","x46","x52","x60","x68",16], 
#             ["x10","x18",10], ["x30","x35",8], ["x53","x61","x69",24], 
#             ["x3","x11","x19","x25","x31","x36",33],["x47","x54",14], ["x4","x12",8], 
#             ["x26","x32","x37","x42","x48",34], ["x62","x70",14], ["x20","x27",11], 
#             ["x38","x43","x49","x55","x63","x71",22], ["x5","x13","x21",19],
#             ["x39","x44",6], ["x56","x64",6], ["x6","x14","x22","x28","x33",17], 
#             ["x50","x57","x65","x72",16], ["x7","x15",3], ["x29","x34",13], ["x51","x58","x66","x73",27]
#         ]
#blank7 = 73

#list of tupples containing puzzles, puzzles' blank squares and puzzles' difficulty
puzzles = [(puzzle1,blank1,"4 x 3 very easy"), (puzzle2,blank2,"8 x 8 easy"), (puzzle3,blank3,"8 x 8 intermediate"),
            (puzzle4,blank4,"9 x 11 intermediate"), (puzzle5,blank5,"8 x 8 hard"), (puzzle6,blank6,"8 x 8 challenging")]#, (puzzle7,blank7,"9 x 11 expert")]

if __name__ == "__main__":
    print ("\n")

    for i in range(len(puzzles)):  #repeat for every puzzle
        print ("\t\t\t*** %s ***\n" % puzzles[i][2])

        #initialize a Kakuro model
        model = Kakuro_Modelisation(puzzles[i][0],puzzles[i][1])   
        model.setVariables()
        model.setDomains()
        model.setNeighbors()

        #call kakuro solver using FC with MRV and LCV
        fcSolver = Kakuro_Solver(model.getVariables(),model.getDomains(),model.getNeighbors(),model.setConstraints,model.getBlankSquares())
        fcSolver.FC_MRV_LCV()

        #call kakuro solver using MAC with MRV and LCV
        macSolver = Kakuro_Solver(model.getVariables(),model.getDomains(),model.getNeighbors(),model.setConstraints,model.getBlankSquares())
        macSolver.MAC_MRV_LCV()
