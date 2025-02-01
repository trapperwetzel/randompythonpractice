
class LeetCodeSolver:
    
    def  __init__(self):
        self.leet_code_problems = [] 
    


    def fizzbuzz(self,n: int):

        answerlist = [] 

        for i in range(1, + n+1):
             
            s = "" 
            
            if(i % 3 == 0):
                s+="fizz"
            if(i % 5 == 0):
                s+="buzz"
            elif(i % 3 != 0 and i % 5 != 0):

                s+= str(i)

            answerlist.append(s)     

        return answerlist


solver = LeetCodeSolver()

answer = solver.fizzbuzz(3)
print(answer)