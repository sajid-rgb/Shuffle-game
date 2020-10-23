from random import shuffle
count=0


while(True):

 point=1000-count*150

 a=[1,2,3,4,5,6]
 def my_list(l):
    shuffle(l)
    return l
 def gues_number(l):
    g=0
    while g not in a:
        g=int(input("Enter your choice: "))
    return g

 x=my_list(a)
 t=gues_number(a)

 count=count+1

 if(point<=0):
     print("Your current point is {}.You attemted {} times.\nYou didn't earn any single point so you lost the game".format(point,count) )
     break

 elif (x[0]==t):
     print("You Win\nand the list is {}\nand you attempted {} times\nand your point is {}".format(x,count,point))
     break



 else:
     print("Try again Dear")
     if(count==10):
         print("You lost the game")
         break



