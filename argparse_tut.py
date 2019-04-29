"""
    @author : RituRaj
    creted : 29 Apr ,19

    Prob
        - Basics of argparse module 
"""
import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('number1' , help="First Number")
    parser.add_argument('number2' , help="Second Number")
    parser.add_argument('operation' , help="Operation",choices=["add","subtract","multiply"])
    
    args = parser.parse_args()
    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None
    if args.operation == "add":
        result = n1 + n2  
    elif args.operation == "subtract":
        result = n1 - n2  
    elif args.operation == "multiply":
        result = n1 * n2  
    else:
        result = "Invalid Operation"

    print ("Result:",result)