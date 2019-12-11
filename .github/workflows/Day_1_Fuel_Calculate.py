import math

def advent_1_1():
    total_fuel=0    
    file_handle=open('day_1_1.txt','r') # Open the Input File
    total_fuel_for_modules=0
    for module_mass in file_handle:
        #print ('Calculating Fuel for Module',module_mass)
        fuel_for_module=0
        fuel_for_fuel=0
        module_mass=int(module_mass)
        fuel_for_module= math.floor((module_mass/3)) - 2
        check_enough_fuel=0
        fuel_for_fuel=fuel_for_module
        while check_enough_fuel == 0:        # Calculate the Fuel required for the weight of the Fuel
            fuel_for_fuel=math.floor((fuel_for_fuel/3)) - 2
            fuel_for_module=fuel_for_module+fuel_for_fuel            
            if math.floor((fuel_for_fuel/3)) - 2 <=0:
                check_enough_fuel=1
                
        total_fuel_for_modules = total_fuel_for_modules + fuel_for_module
        #print('Total Fuel Required for Module -',module_mass,' is :',fuel_for_module)
    
    
    print ('Total Fuel Required is:',total_fuel_for_modules)    
    



#Call the Function to get the Result
advent_1_1()