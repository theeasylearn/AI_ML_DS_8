#create function that count, sum & findout average of given values 
def doCalculate(*values):
    count = 0
    sum = 0 
    average = 0
    for number in values:
        count += 1
        sum += number # sum = sum + number
    
    average = sum / count 
    return count, sum, average 
    #function return multiple value 

# result = doCalculate(100,200,300,1200)
# result = doCalculate(100,200,300,1200,'ankit')
print(result)
