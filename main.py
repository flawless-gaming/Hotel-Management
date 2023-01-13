#HOSTEL MANAGEMENT
import csv
import math
import os
import datetime
#Creating function showmenu to print the following part we are going to work
def ShowMenu():
          print("\n\n\n\t\t############ HOTEL YATRIK ###############")
          print("\n\t\t\t 1. CHECK-IN ")
          print("\n\t\t\t 2. CHECK-OUT ")
          print("\n\t\t\t 3. ALL ROOM STATUS ")
          print("\n\t\t\t 4. OTHER EXPENSES ")
          print("\n\t\t\t 5. ROOM ENQUIRY ")
          print("\n\t\t\t 6. CONTACT DETAIL")
          print("\n\t\t\t 0. LOG OUT ")
          print("\t\t#########################################")
#Creating function ShowAllRoomStatus to show all rooms vacant or occupied         
def ShowAllRoomStatus():
          #To display room details from csv file
          with open('rooms.csv',mode='r') as csvfile:
                    myreader = csv.reader(csvfile,delimiter=',')#to read the file
                    print("="*75)
                    print("%10s"%"FLOOR","%15s"%"ROOM NUMBER","%20s"%"ROOM TYPE","%15s"%"ROOM STATUS",'%10s'%'RATE')
                    print("="*75)
                    #to print data in csv file
                    for row in myreader:
                              if row[2]=="D":
                                        rtype="DELUXE"
                              elif row[2]=="SD":
                                        rtype="SEMI-DELUXE"
                              elif row[2]=="SDX":
                                        rtype="SUPER DELUXE"
                              elif row[2]=="HDX":
                                        rtype="EXECUTIVE SUITE"
                              if row[3]=="V":
                                        status="VACANT"
                              else:
                                        status ="OCCUPIED"
                              print("%10s"%row[0],"%15s"%row[1],"%20s"%rtype,"%15s"%status,'%10s'%row[4])
                    print("="*75)
          input('Press any key...')#can be changed to particular input using if function
#Creating function CheckRoomVacant to check availablity of room
def CheckRoomVacant(roomno):
          #to check data from csv file
          with open('rooms.csv',mode='r') as csvfile:
                    myreader = csv.reader(csvfile,delimiter=',')
                    found=False
                    # to check if room no exists or not  
                    for row in myreader:
                              if len(row)>0:
                                        if str(row[1])==str(roomno):
                                                  found=True
                                                  return row[3],row[4]#to give back values of vacant or occupied and price of the room
                    #if entered room no doesnot exists
                    if not found:
                              return 'INVALID'
                    
          input('Press any key...')
#Creating function CheckIn to enter the data of visitor and add to csv           
def CheckIn():
          print('\n\n\t\t################# NEW VISITOR ARRIVAL #######################')
          Visitor_Number=None
          #to add data if file allready exists
          if os.path.exists('Visitor.csv'):
                    with open('Visitor.csv',mode='r') as csvfile:
                              myreader = csv.reader(csvfile,delimiter=',')
                              l = len(list(myreader))
                              Visitor_Number = l + 1                        
          #if file doesnot exists
          else:
                    Visitor_Number = 1
          dt = datetime.datetime.now()#date and time
          today = str(dt.day)+'/'+str(dt.month)+'/'+str(dt.year)+' '+str(dt.hour)+':'+str(dt.minute)+':'+str(dt.second)#date and time of present day
          print('\n\t\t\t\t\t\t\t Today is :'+today)
          print('\n\t\t Visitor Number :',Visitor_Number)
          name = input('\t\t Enter Visitor Name :')#visitor name
          ID = input('\t\t Enter What Photo ID number :')
          age = int(input('\t\t Enter Age :'))
          gender = input('\t\t Choose gender 1-Male, 2-Female, 3-Transgender>>')
          coming_from = input('\t\t Enter the Place from where person is coming :')
          purpose = input('\t\t Enter purpose of Visit :')
          mobile = input('\t\t Enter Mobile Number :')
          c='go'#taken value as go
          roomno=0
          #to enter room number
          while c=='go':
                    roomno = int(input('\t\t Enter Room Number :'))
                    status = CheckRoomVacant(roomno)#t check wether the room no. entered is vacant or not
                    #if entered room no. doesnot exists 
                    if status[0]=='INVALID':
                              print('Enter Valid room number :')
                    #if entered room no. exists and vacant
                    elif status[0]=='V':
                              c='OK'
                    #if entered room no. exists and occupied
                    else:
                              print('\t\t Room Number not Vacant')
          print('\t\t Check in Date and Time :',today)#checked in day and time
          print('\t\t Room Rent @'+str(status[1])+' Day')#room price
          print('\t\t Advance To Pay :'+str(status[1]))#room advance payment
          ans = input('\n\t\t Confirm?(y)')#to confirm the room
          #to add in or create csv file 
          if ans.lower()=='y':
                    visitors=[Visitor_Number,name,ID,age,gender,coming_from,purpose,roomno,today,status[1],mobile]
                    #to add data visiters
                    with open('Visitor.csv','a') as vfile:
                              mywriter = csv.writer(vfile,delimiter=',',lineterminator='\n')
                              mywriter.writerow(visitors)#to add in csv file
                    print()
                    room=[]
                    #to add and read rows of csv
                    with open('rooms.csv','r') as rcsv:
                              myreader = csv.reader(rcsv,delimiter=',')
                              for row in myreader:
                                        if len(row)>0:
                                                  room.append(row)
                                                  #print(row)
                    #to edit status of room in csv file
                    with open('rooms.csv','w') as rcsv:
                              mywriter = csv.writer(rcsv,delimiter=',',lineterminator='\n')
                              for i in range(len(list(room))):
                                        if room[i][1]==str(roomno):
                                                  room[i][3]='O'
                                        #print(room[i])
                                        mywriter.writerow(room[i])
                    print('\t\t Successfully checked In')
#to create function OtherExpenses for adding extra expenses
def OtherExpense():
          print("="*30," OTHER EXPENSE SCREEN ", "="*30)
          visitors=[]
          #to add csv data in visitos
          with open('Visitor.csv','r') as csvroom:
                    myreader = csv.reader(csvroom,delimiter=',')
                    for row in myreader:
                              visitors.append(row)
          vno = input('\n\t\t ENTER VISITOR NO :')#to ask visitor no
          found=False
          #to add extra expenses in bill if vno entered exists
          for rs in visitors:
                    if rs[0]==vno:
                              food = int(input('Enter Food Expense (0 if no expense):'))
                              laundry = int(input('Enter Laundry Expense (0 if no expense) :'))
                              misc = int(input('Enter any other expense (0 if no expense) :'))
                              #to create or add in csv file about expensis price
                              with open('expense.csv','a') as expcsv:
                                        mywriter = csv.writer(expcsv,delimiter=',',lineterminator='\n')
                                        today = datetime.datetime.now()
                                        today = str(today.day)+'/'+str(today.month)+'/'+str(today.year)
                                        exp = [vno,food,laundry,misc,today]
                                        mywriter.writerow(exp)
                              found=True
          #if vno entered entered does not exists
          if not found:
                    print("\n\t\t ### SORRY ROOM NUMBER NOT OCCUPIED ###")
#to checkout hotel, function CheckOut is created
def CheckOut():
          print('\n\n')
          print('='*30,' CHECK OUT SCREEN ' , '='*30)
          roomstatus=[]
          #this will read all room status
          with open('rooms.csv','r') as csvroom:
                    myreader = csv.reader(csvroom,delimiter=',')
                    for row in myreader:
                              roomstatus.append(row)
          rno = input('\n\t\t ENTER ROOM NO :')#to ask room no
          found=False
          vis=[]
          fexp=0
          lexp=0
          mexp=0
          total=0
          oexp=0
          #to calculate all totals
          for rs in roomstatus:
                    #to check wether the room no. entered is occupied
                    if rs[1]==rno and rs[3]=='O':
                              total=total + int(rs[4])
                              print('Checking....')
                              #to add csv data in vis
                              with open('Visitor.csv','r') as vcsv:
                                        myreader = csv.reader(vcsv,delimiter=',')
                                        for row in myreader:
                                                  if rno == row[7]:
                                                            vis = row
                                                            print("In")
                              #to calculate expenses from csv data
                              with open('expense.csv','r') as ecsv:
                                        myreader = csv.reader(ecsv,delimiter=',')
                                        for row in myreader:
                                                  if row[0]==vis[0]:
                                                            fexp = fexp + int(row[1])
                                                            lexp = lexp + int(row[2])
                                                            mexp = mexp + int(row[3])
                              oexp = fexp + lexp + mexp
                              found=True
          #if room no. entered is not occupied
          if not found:
                    print('\t\t ## ROOM NOT BOOKED ##')
          #to display all calculated data
          else:
                    today = datetime.datetime.now()
                    today = str(today.day)+'/'+str(today.month)+'/'+str(today.year)+' '+str(today.hour)+':'+str(today.minute)+':'+str(today.second)
                    print('\n\n')
                    print('='*30,'CHECK OUT (BILL)','='*30)
                    print('\t\t CHECK IN DATE : ',vis[8])
                    print('\t\t CHECK OUT DATE :',today)
                    print('-'*75)
                    print('\t\t Visitor Number : ',vis[0])
                    print('\t\t Visitor Name   : ',vis[1])
                    print('\t\t Visitor Age    : ',vis[3])
                    g=''
                    if vis[4]=='1':
                              g='Male'
                    if vis[4]=='3':
                              g='Transegender'
                    if row[4]=='2':
                              g='Female'
                              
                    print('\t\t Visitor Gender : ',g)
                    
                    print('\t\t Coming From     : ',vis[5])
                    print('\t\t Purpose of Visit: ',vis[6])
                    print('-'*75)

                    d1 = datetime.datetime.strptime(vis[8],"%d/%m/%Y %H:%M:%S")
                    d2 = datetime.datetime.strptime(today,"%d/%m/%Y %H:%M:%S")
                    d3 = d2-d1
                    day=0
                    #to calculate no of days stayed
                    if d3.days<=1:
                              day=1
                    else:
                              day = math.ceil(d3.days)
                    print('\n\t\t Total days          :',day)#no of days stayed
                    print('\t\t Room Rent @'+str(total)+'/Day :Rs.',total*day)#total price of days stayed
                    print('\t\t Food Expense        :Rs.',fexp)#expenses
                    print('\t\t Laundry Expense     :Rs.',lexp)
                    print('\t\t Misc. Expense       :Rs.',mexp)
                    print('-'*75)
                    print('\t\t\t GRAND TOTAL : Rs.',(total+oexp))#final total
                    ans = input('\n\t\t Confirm?(y)')#to confirm the room
                    #to add in or create csv file 
                    if ans.lower()=='y':
                            room=[]
                            #to add and read rows of csv
                            with open('rooms.csv','r') as rcsv:
                                      myreader = csv.reader(rcsv,delimiter=',')
                                      for row in myreader:
                                                if len(row)>0:
                                                          room.append(row)
                                                          #print(row)
                            #to edit status of room in csv file
                            with open('rooms.csv','w') as rcsv:
                                      mywriter = csv.writer(rcsv,delimiter=',',lineterminator='\n')
                                      for i in range(len(list(room))):
                                                if room[i][1]==str(rno):
                                                          room[i][3]='V'
                                                #print(room[i])
                                                mywriter.writerow(room[i])
                            print('\t\t Checked Out Successfully!')
#created function RoomEnquiry to check visitor is checked in or not                     
def RoomEnquiry():
          print('\n\n')
          print('='*30,' VISITOR ENQUIRY SCREEN ' , '='*30)
          vn = input("\n\t\t ENTER VISITOR NAME : ")
          fs = "%5s %-15s %6s %10s %15s %15s %8s %-20s"
          print(fs % ("VID","VISITOR NAME","AGE","GENDER","COMING FROM","PURPOSE","ROOMNO","CHECKIN DATE"))
          print("="*110)
          found=False
          gender=''
          #to dispay asked visitor's data
          with open('Visitor.csv','r') as vcsv:
                    myreader = csv.reader(vcsv,delimiter=',')
                    for row in myreader:
                              if row[1].lower()==vn.lower():
                                        if row[4]=='1':
                                            gender='Male'
                                        if row[4]=='2':
                                            gender='Female'
                                        if row[4]=='3':
                                            gender='Transgender'
                                        
                                        print(fs%(row[0],row[1],row[3],gender,row[5],row[6],row[7],row[8]))
                                        found=True
          print("="*110)
          #if entered visitor's name does not exists in data
          if not found:
                    print("\n\t\t\t VISITOR NAME NOT FOUND ")
#to contact the management
def Contact():
          print("\n\n============================== CONTACT INFORMATION ==============================")
          print("\n\t\t Project Name : YATRIK HOTEL MANAGEMENT SYSTEM ")
          print("\n\t\t Developed By : RISHI JAIN ")
          print("\n\t\t Language     : PYTHON ")
          print("\n\t\t Topic        : CSV FILE HANDLING ")
          print("\n\t\t E-Mail       : rishigpay2835@gmail.com")


#all assembeled to run
choice=0
#to run menu again and again after end of each query while function is used
while choice!=None:
          ShowMenu()
          choice = int(input('\t\t\t ENTER YOUR CHOICE :'))
          if choice==1:
                    CheckIn()
          elif choice==2:
                    CheckOut()
          elif choice==3:
                    ShowAllRoomStatus()
          elif choice==4:
                    OtherExpense()
          elif choice==5:
                    RoomEnquiry()
          elif choice==6:
                    Contact()
          elif choice==0:
                    choice=None
                    print('\n\t\t\t THANK YOU! ')
          #if entred input is not from asked inpuut
          else:
                    print('\n\t\t\t == INVALID CHOICE == ')
          

