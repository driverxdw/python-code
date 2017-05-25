#use tkinter 
#!/usr/bin/python
#encoding=utf-8
#************************************
from Tkinter import *
import tkFont
class calculate():
	def clac(self,entry):
		input=entry.get()
		output=eval(input.strip())
		entry.delete('0','end')
		entry.insert(END,output)
	def entry_output(self,entry,digist):
		entry.insert(END,digist)
	def C(self,entry):
		entry.delete('0','end')
	def gui_display(self):
		root=Tk()
		root.title('cal made by xdw~')
		root.resizable(0,0)
		entry=Entry(root,justify='right')
		entry.grid(row=0,column=0,columnspan=3,padx=6,pady=6)
		b1=Button(root,text='1',width='2',height='2',command=lambda:self.entry_output(entry,'1')).grid(row=1,column=0)
		b2=Button(root,text='2',width='2',height='2',command=lambda:self.entry_output(entry,'2')).grid(row=1,column=1)
		b3=Button(root,text='3',width='2',height='2',command=lambda:self.entry_output(entry,'3')).grid(row=1,column=2)
		b4=Button(root,text='4',width='2',height='2',command=lambda:self.entry_output(entry,'4')).grid(row=2,column=0)
		b5=Button(root,text='5',width='2',height='2',command=lambda:self.entry_output(entry,'5')).grid(row=2,column=1)
		b6=Button(root,text='6',width='2',height='2',command=lambda:self.entry_output(entry,'6')).grid(row=2,column=2)
		b7=Button(root,text='7',width='2',height='2',command=lambda:self.entry_output(entry,'7')).grid(row=3,column=0)
		b8=Button(root,text='8',width='2',height='2',command=lambda:self.entry_output(entry,'8')).grid(row=3,column=1)
		b9=Button(root,text='9',width='2',height='2',command=lambda:self.entry_output(entry,'9')).grid(row=3,column=2)
		b10=Button(root,text='0',width='2',height='2',command=lambda:self.entry_output(entry,'0')).grid(row=4,column=0)
		b10=Button(root,text='+',width='2',height='2',command=lambda:self.entry_output(entry,'+')).grid(row=4,column=1)
		b11=Button(root,text='-',width='2',height='2',command=lambda:self.entry_output(entry,'-')).grid(row=4,column=2)
		b12=Button(root,text='*',width='2',height='2',command=lambda:self.entry_output(entry,'*')).grid(row=5,column=0)
		b13=Button(root,text='/',width='2',height='2',command=lambda:self.entry_output(entry,'/')).grid(row=5,column=1)
		b14=Button(root,text='C',width='2',height='2',command=lambda:self.C(entry)).grid(row=5,column=2)
		b15=Button(root,text='=',width='2',height='2',command=lambda:self.clac(entry)).grid(row=5,column=3)
		root.mainloop()
cal=calculate()
cal.gui_display()