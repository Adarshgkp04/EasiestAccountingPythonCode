#Easiest accounting python console program>>> 
#_________________________________________________
#A parent class of account holder is created
class account_holder:
#initialization of default bankname    
    def __init__(self,bankname):
        self.bankname=bankname
        self.initamnt=0
#To fetch holder data        
    def collect_info(self):
        self.name=input('Enter name of account holder : ')
        self.accntNo=input('Enter account no. : ')
#_________________________________________________________
#Also reserving information is necessary so, this is done by data file handling
    def dataFile(self):
        fileptr=open('Detail.txt','a') #To append every data 'a' attribute is used
        fileptr.write('\nName : '+self.name+'\n') #Each data is ready to be written on Detaiol.txt
        fileptr.write('Account Number : '+self.accntNo+'\n')
        fileptr.write('Bank name : '+self.bankname+'\n')
        fileptr.write('_________________________________________________________________\n')
        fileptr.close()
#To fetch info from multiple user for loop is used instead of any jump statement
for i in range(1,100):
    choice=input('y for more and any to exit : ')
    if choice is 'y': #only data is written when y is pressed otherwise condition will break
        accnt1=account_holder('Punjab National Bank')
        accnt1.collect_info()
        accnt1.dataFile()
    else:
        break