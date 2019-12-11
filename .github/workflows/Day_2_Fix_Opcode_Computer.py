def fix_the_computer():
    file_handle=open('Day_2_1.txt','r')
    code_list=[]
    #Convert the Input into a List
    for line in file_handle:
        for get_codes in line.split(','):
            code_list.append(int(get_codes))
    
    #Traverse the List and Prepare a new List
    halt_program=False
    next_opcode=0
    print('Instructions',code_list)
    while not halt_program:   #Loop through all the Opcodes till we reach the opcode to halt
        print('Opcode is:',code_list[next_opcode])
        if code_list[next_opcode]==99:
            halt_program=True
            print('Halt the Program')
        elif code_list[next_opcode] !=1 and code_list[next_opcode] !=2 :
            halt_program=True
            print('**Unknown Opcode at Position**',next_opcode)
        else:
            #Execute the Instructions
            if code_list[next_opcode]==1:
                print('Opcode is 1 , Add')
                result=code_list[code_list[next_opcode+1]] + code_list[code_list[next_opcode+2]]
                code_list[code_list[next_opcode+3]]=result
                next_opcode=next_opcode+4
                halt_program=False
            elif code_list[next_opcode]==2:
                result=code_list[code_list[next_opcode+1]] * code_list[code_list[next_opcode+2]]
                code_list[code_list[next_opcode+3]]=result
                next_opcode=next_opcode+4
                halt_program=False
            else:
                halt_program=True
                
    print('Manipulated List :',code_list)       
         
            
            
            

#Run the Code
fix_the_computer()
        