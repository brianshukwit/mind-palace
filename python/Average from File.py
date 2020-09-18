# Average from file
import functools
def sum(x,y):
    return x+y

def main():
    fname = input("Enter filename:")
    infile = open(fname, "r")
    
    total = 0
    num_of_entries = 0
    lines = infile.readlines()
    
    
       
    for line in lines:
        nums = list(map(int, line.split()))
        num_of_entries += len(nums)
        total += functools.reduce(sum, nums)
        
    

    
    average = total/num_of_entries
    
    print(average) 

main()