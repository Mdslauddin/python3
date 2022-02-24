
# open a  file Read Mode 
#f=open("tesfile.txt","r")
#myfile=f.read()
#print(myfile)
#f.close()

# you can also specific how many character you want to print

#f=open("tesfile.txt","r")
#myfile=f.read(5)
#print(myfile)
#f.close()

# if you want to read line by line
#f=open("test2.txt", "r")
#print(f.readline())
#print(f.readline())
# if you can use many times 

# if you want to read the whole file 
#f=open("test2.txt","r")
#for x in f:
#	print(x)


# create a file 
#f=open("demofile1.txt","x")
#f=open("demofile1.txt","w")
#f.write("HI  you are learning python !")
#f.close()


#f=open("demofile1.txt","w")a 
#f.write("\n this is complete python course. ! ")
#f.close()


# the other way to open & close th file is the with statement if you are use with statement you #don't need to close file 

#with open('test2.txt','r') as f :
#	a=f.read()
#print(a)

# Rename & Delete python files.
#import os 
#old_file_name="demofile1.txt"
#new_file_name="demofile2.txt"
#with open(old_file_name) as f:
#	data=f.read()
#with open(new_file_name,"w") as f :
#	f.write(data)
#os.remove(old_file_name)		