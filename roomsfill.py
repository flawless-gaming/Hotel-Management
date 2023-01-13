import csv
rooms=[
          ["I","101","SD","V",1200],
          ["I","102","SD","V",1200],
          ["I","103","D","V",1500],
          ["I","104","SD","V",1200],
          ["I","105","SDX","V",2000],
          ["I","106","SD","V",1200],
          ["II","201","SDX","V",2000],
          ["II","202","SD","V",1200],
          ["II","203","D","V",1500],
          ["II","204","D","V",1500],
          ["II","205","SDX","V",2000],
          ["II","206","SD","V",1200],
          ["III","301","SDX","V",2000],
          ["III","302","HDX","V",4000],
          ["III","303","SDX","V",2000],
          ["III","304","D","V",1500],
          ["III","305","SDX","V",2000]]
          
          
          
with open('rooms.csv',mode='w') as csvfile:
    mywriter = csv.writer(csvfile,delimiter=',',lineterminator='\n')
    for r in rooms:
        mywriter.writerow(r)
          
