def pharmacy( disease,patient) :
    
    
    
    disease=["headache","malaria","cough"]

    drugs=["paracetamol" ,"joy ointment","panadol"]

 
    
    
    
    if patient <=18  and  disease ==headache:
        
        return    f"take two doses of {drugs[2]}"


    if patient >=18 and patient < 50: 

        return  f"take just one dose of {drugs[2]}"
    
    

    elif patient >50: 

        return    f"please get a lab screening and take one dose of {drugs[1]}"
    

    elif  disease== disease[1] and patient >18 :

        return  f"take {drugs[ 1]} and {drugs[2]}"


    else:

        return "CALL OUR CUSTOMER SERVICE 1234567890"
    
    

Patient_disease= input("what are you suffering from :  ")

patient_age= int(input("how old are you right now : "))



print(pharmacy(Patient_disease,patient_age))


    
    





