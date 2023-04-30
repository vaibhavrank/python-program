# import math;
import math
  
# Function for calculating sin value
def cal_sin(n):
  
    accuracy = 0.0001
      
    # Converting degrees to radian
    n = n * (3.142 / 180.0); 
      

    x1 = n
      
    # maps the sum along the series
    sinx = n;     
      
    # holds the actual value of sin(n)
    sinval = math.sin(n); 
    i = 1
    while(True):
      
        denominator = 2 * i * (2 * i + 1)
        x1 = -x1 * n * n / denominator
        sinx = sinx+ x1
        i = i + 1
        if(accuracy <= abs(sinval - sinx)):
            break
          
    print(round(sinx))
  
# Driver Code
n=0

cal_sin(n)
      
# This code is contributed by mits