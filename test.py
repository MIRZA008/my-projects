while True:
    marks=int(input("Enter Marks :"))

    if marks > 100 or marks < 0:
        print ("Invalid marks")
        
    elif marks >= 50:
        print ("Pass")
        
    else:
        print ("Fail")
              
