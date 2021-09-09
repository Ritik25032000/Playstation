from subprocess import call
from tkinter import *
from tkinter import ttk


class Employee:
	def __init__(self,root):
		
		self.root=root
		self.root.title("Play Station")
		self.root.geometry("1550x800+0+0")


		title=Label(self.root,text="Play Station",font=("times new roman",30,"bold"),fg="black",bg="#4219c6",bd=4,relief=RAISED)
		title.pack(side=TOP,fill=X)

		
		#Game Frame1
		Game_frame1= Frame(self.root,bd=4,relief=RIDGE,bg="#CBD2DE")
		Game_frame1.place(x=10,y=60,width=670,height=200)
		
		#Game Title
		G1_title= Label(Game_frame1,text="Feed Snake",font=("times new roman",25,"bold"),fg="black",bg="#4219c6",bd=4,relief=RAISED)
		G1_title.grid(row=0,columnspan=2,padx=20,pady=20)
		
		#Play Button
		g1_btn=Button(Game_frame1,text="Play",width=8,height=1,fg="White",bg="#242536",command=self.snake)
		g1_btn.grid(row=1,column=0,padx=10,pady=10)
		
		#Game Frame2
		Game_frame2= Frame(self.root,bd=4,relief=RIDGE,bg="#CBD2DE")
		Game_frame2.place(x=690,y=60,width=670,height=200)
		
		#Game Title
		G2_title= Label(Game_frame2,text="Pong",font=("times new roman",25,"bold"),fg="black",bg="#4219c6",bd=4,relief=RAISED)
		G2_title.grid(row=0,columnspan=2,padx=20,pady=20)
		
		#Play Button
		g2_btn=Button(Game_frame2,text="Play",width=8,height=1,fg="White",bg="#242536",command=self.pong)
		g2_btn.grid(row=1,column=0,padx=10,pady=10)
		
		#Game Frame3
		Game_frame3= Frame(self.root,bd=4,relief=RIDGE,bg="#CBD2DE")
		Game_frame3.place(x=10,y=270,width=670,height=200)
		
		#Game Title
		G3_title= Label(Game_frame3,text="Tic Tac Toe",font=("times new roman",25,"bold"),fg="black",bg="#4219c6",bd=4,relief=RAISED)
		G3_title.grid(row=0,columnspan=2,padx=20,pady=20)
		
		#Play Button
		g3_btn=Button(Game_frame3,text="Play",width=8,height=1,fg="White",bg="#242536",command=self.tictac)
		g3_btn.grid(row=1,column=0,padx=10,pady=10)
		
		#Game Frame4
		Game_frame4= Frame(self.root,bd=4,relief=RIDGE,bg="#CBD2DE")
		Game_frame4.place(x=690,y=270,width=670,height=200)
		
		#Game Title
		G4_title= Label(Game_frame4,text="Flappy Bird",font=("times new roman",25,"bold"),fg="black",bg="#4219c6",bd=4,relief=RAISED)
		G4_title.grid(row=0,columnspan=2,padx=20,pady=20)
		
		#Play Button
		g4_btn=Button(Game_frame4,text="Play",width=8,height=1,fg="White",bg="#242536",command=self.flappy)
		g4_btn.grid(row=1,column=0,padx=10,pady=10)
		
		#Game Frame5
		Game_frame5= Frame(self.root,bd=4,relief=RIDGE,bg="#CBD2DE")
		Game_frame5.place(x=10,y=480,width=670,height=200)
		
		#Game Title
		G5_title= Label(Game_frame5,text="Sudoku",font=("times new roman",25,"bold"),fg="black",bg="#4219c6",bd=4,relief=RAISED)
		G5_title.grid(row=0,columnspan=2,padx=20,pady=20)
		
		#Play Button
		g5_btn=Button(Game_frame5,text="Play",width=8,height=1,fg="White",bg="#242536",command=self.sudoku)
		g5_btn.grid(row=1,column=0,padx=10,pady=10)
		
				
	def snake(self):
		call(["python","snake.py"])
	
	def pong(self):
		call(["python","pong.py"])
	
	def tictac(self):
		call(["python","tictactoe.py"])
	
	def flappy(self):
		call(["python","flappy.py"])
	
	def sudoku(self):
		call(["python","sudoku.py"])
	
	



root=Tk()
ob=Employee(root)
root.mainloop()


