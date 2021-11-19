## import required packages
import os
import io
import pandas as pd
try:
  from tkinter import *
except:
  from Tkinter import *  
from tkinter import filedialog
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Plotter:

    #main window
    __window=Tk()
    __df=pd.DataFrame([])


    # Logo for main window
    __photo = PhotoImage(file = "img/logo.png")
    __window.iconphoto(False, __photo)

    # Frames in the main window
    __thisframe1=Frame(__window,width=300,height=650,highlightbackground='#454545',highlightthickness=0,bg='#454545')
    __thisframe2=Frame(__window,width=1000,height=650,highlightbackground='#3498DB',highlightthickness=0,bg='white')
    __thisframe3=Frame(__thisframe2,width=80,height=600,highlightbackground='#3498DB',highlightthickness=0,bg='#221870')
    __thisframe4=Frame(__thisframe2,width=800,height=600,highlightbackground='#454545',highlightthickness=1,bg='white')

    # Lables for logo and name of application
    __photo0 = PhotoImage(file = r"img/logo1.png")
    __l00=Label(__thisframe1,image=__photo0,bd=0)
    __l01=Label(__thisframe1,text = "PLOTTER",fg = "white",font=('arial',26,'bold'),bg='#454545')
    
    

    # Label and option menu to select plot type
    
    __clicked1=StringVar() # Variable to store selected plot-type option value
    __clicked1.set(' Select ')
    __plots=['Scatterplot','Barplot','Lineplot'] # plot types list
    __thisdrop1=OptionMenu(__thisframe1,__clicked1,*__plots)
    __l1=Label(__thisframe1,text = "plot type : ",fg = "white",font=('arial',12,'bold'),bg='#454545')
    

    
   
    
    # Text Area to display text on window
    __thisTextArea = Text(__thisframe4,padx=80,spacing2= 5,bg='white',fg='blue',height=33, width=79,pady=30)

    # Canvas to show plots on window 
    __thiscanvas = Canvas(__thisframe4,width=794,height=594,bg="white")
    __f=Figure(figsize=(7,7),dpi=80)
    __a=__f.add_subplot(111)
    __thiscanvasf=FigureCanvasTkAgg(__f,master =__thisframe4)

    # Images used for button widgets
    
    __photo1 = PhotoImage(file = r"img/uploads.png")
    __photo2 = PhotoImage(file = r"img/plots.png")
    __photo3 = PhotoImage(file = r"img/data.png")
    __photo4 = PhotoImage(file = r"img/desc.png")
    __photo5 = PhotoImage(file = r"img/info.png")
    __photo6 = PhotoImage(file = r"img/clear.png")
    __photo7 = PhotoImage(file = r"img/help.png")
    __photo8 = PhotoImage(file = r"img/exit.png")
    
    
    
    
    
    
      
    

    def __init__(self):
           
            self.__import_file_path=None
            self.__window.title('Plotter')
            self.__window.configure(bg='#F8B850')
            self.__window.geometry("1366x768+0+0")

            # Placing Frames on window
            self.__thisframe1.grid(row=0,column=0,padx=20,pady=20)
            self.__thisframe2.grid(row=0,column=1,pady=30)
            self.__thisframe3.grid(row=0,column=0,padx=15,pady=20)
            self.__thisframe4.grid(row=0,column=1,padx=20,pady=20)

            # Placing logo and name of application
            self.__l00.place(x=110,y=10)
            self.__l01.place(x=70,y=100)
            

            # Buttons Used
            self.__b1=Button(self.__thisframe3,image = self.__photo1,bg='#221870',activebackground='#221870',bd=0,command=self.getCSV)
            self.__b2=Button(self.__thisframe3,image = self.__photo2,bg='#221870',activebackground='#221870',bd=0,command=self.plot)
            self.__b3=Button(self.__thisframe3,image = self.__photo3,bg='#221870',activebackground='#221870',bd=0,command=self.getData)
            self.__b4=Button(self.__thisframe3,image = self.__photo4,bg='#221870',activebackground='#221870',bd=0,command=self.descript)
            self.__b5=Button(self.__thisframe3,image = self.__photo5,bg='#221870',activebackground='#221870',bd=0,command=self.getInfo)
            self.__b6=Button(self.__thisframe1,image = self.__photo6,bg='#454545',activebackground='#454545',bd=0,command=self.clear)
            self.__b7=Button(self.__thisframe1,image = self.__photo7,bg='#454545',activebackground='#454545',bd=0,command=self.help)
            self.__b8=Button(self.__thisframe1,image = self.__photo8,bg='#454545',activebackground='#454545',bd=0,command=self.quit)

            # placing buttons on window
            self.__b1.grid(row=0,column=0,padx=20,pady=20)
            self.__b2.grid(row=1,column=0,padx=20,pady=20)
            self.__b3.grid(row=2,column=0,padx=20,pady=20)
            self.__b4.grid(row=3,column=0,padx=20,pady=20)
            self.__b5.grid(row=4,column=0,padx=20,pady=20)
            self.__b6.place(x=180,y=520)
            self.__b7.place(x=30,y=580)
            self.__b8.place(x=180,y=580)
            
           
            # placing canvas on window
            self.__thiscanvas.grid(row=0,column=0)
            
            # fixing the frame width and height as mentioned
            self.__thisframe1.grid_propagate(0)
            self.__thisframe2.pack_propagate(0)
            self.__thisframe3.pack_propagate(0)
            self.__thisframe4.grid_propagate(0)
            self.__thiscanvas.grid_propagate(0)
            self.__thisTextArea.grid_propagate(0)

            self.__l1.place(x=15,y=210)
            self.__thisdrop1.place(x=110,y=210)

            # Labels and drop down menu to select columns from dataset
            self.cols=['No Columns']
            self.clicked2=StringVar()
            self.clicked3=StringVar()
            self.__l2=Label(self.__thisframe1,text = "column1 : ",height = 2,fg = "white",font=('arial',12,'bold'),bg='#454545')
            self.__l3=Label(self.__thisframe1,text = "column2 : ",height = 2,fg = "white",font=('arial',12,'bold'),bg='#454545')
            self.__thisdrop2=OptionMenu(self.__thisframe1,self.clicked2,*self.cols)
            self.__thisdrop3=OptionMenu(self.__thisframe1,self.clicked3,*self.cols)
            self.clicked2.set('No Columns')
            self.clicked3.set('No Columns')
            self.__l2.place(x=15,y=270)
            self.__thisdrop2.place(x=100,y=270)
            self.__l3.place(x=15,y=330)
            self.__thisdrop3.place(x=100,y=330)
            
                                             
            
    def getCSV(self):
        self.__import_file_path = filedialog.askopenfilename(filetypes =[('CSV Files', '*.CSV')])

        try :
            self.__df = pd.read_csv (self.__import_file_path)
            self.__window.title('Plotter  ('+os.path.basename( self.__import_file_path)+')')
            self.cols=[col for col in self.__df.select_dtypes(include='number')]
            self.__thisdrop2=OptionMenu(self.__thisframe1,self.clicked2,*self.cols)
            self.__thisdrop3=OptionMenu(self.__thisframe1,self.clicked3,*self.cols)
            self.__thisdrop2.place(x=100,y=270)
            self.__thisdrop3.place(x=100,y=330)
            self.clicked2.set('column 1')
            self.clicked3.set('column 2') 
               
        except:
            self.__window.title('Plotter  (No file chosen)')
            self.cols=['No Columns']
            self.clicked2.set('No Columns')
            self.clicked3.set('No Columns')
            self.__thisdrop2=OptionMenu(self.__thisframe1,self.clicked2,*self.cols)
            self.__thisdrop3=OptionMenu(self.__thisframe1,self.clicked3,*self.cols)
            self.__thisdrop2.place(x=100,y=270)
            self.__thisdrop3.place(x=100,y=330)
         
            

    def plot(self):
        
            self.__a.clear()
            self.__thisTextArea.delete(1.0,END)  
            self.__thisTextArea.grid_forget()
            self.__thiscanvas.grid(row=1,column=0)
            self.__df=self.__df.dropna(how="any")
     
            if self.__df.empty != True:

                   try:
         
                       if self.__clicked1.get() == 'Scatterplot':
                              self.__a.scatter(self.__df[self.clicked2.get()],self.__df[self.clicked3.get()],color = ['red'])

                       elif self.__clicked1.get() == 'Barplot':
                              self.__a.bar(self.__df[self.clicked2.get()],self.__df[self.clicked3.get()],color = ['red'])

                       elif self.__clicked1.get() == 'Lineplot':
                              self.__a.plot(self.__df[self.clicked2.get()],self.__df[self.clicked3.get()],linestyle='dashed')

                       else:
                              messagebox.showerror("Error", "Select Appropriate plot type")
                              return


                       self.__a.set_title(self.clicked2.get() +'  Vs  '+ self.clicked3.get() )
                       self.__a.set_xlabel(self.clicked2.get())
                       self.__a.set_ylabel(self.clicked3.get())  
                       self.__thiscanvasf.draw()
                       self.__thiscanvasf.get_tk_widget().grid(row=1,column=0)
                       self.__clicked1.set(' Select ')  
                       self.clicked2.set('column 1')
                       self.clicked3.set('column 2')

                   except KeyError:
                              messagebox.showerror("Error", "Select appropriate columns")
            else:
               messagebox.showerror("Error", "No Data is present to plot")
                    

    def getData(self):
      
      if  self.__import_file_path != None and self.__df.empty != True:
        self.__thiscanvas.grid_forget()
        self.__thiscanvasf.get_tk_widget().grid_forget()
        self.__thisTextArea.grid(row=0,column=0,padx=2)
        self.__thisTextArea.grid_propagate(0)
        self.__thisTextArea.delete(1.0,END)
        
        self.__thisTextArea.insert(1.0,"#--------      Data in the Dataset ("+os.path.basename( self.__import_file_path)+")      --------#\n\n\n\n")
        self.__thisTextArea.insert(10.0,self.__df)
      else:
        messagebox.showerror("Error", "Select Appropriate Dataset")             


    def descript(self):

       if  self.__import_file_path != None and self.__df.empty != True:
        
          self.__thiscanvas.grid_forget()
          self.__thiscanvasf.get_tk_widget().grid_forget()
          self.__thisTextArea.grid(row=0,column=0)
          self.__thisTextArea.delete(1.0,END)
          self.__thisTextArea.insert(1.0,"#--------    This is Description of Numerical Data in Dataset    --------#\n\n\n\n")
          self.__thisTextArea.insert(15.0,self.__df.describe())
          
       else:
          messagebox.showerror("Error", "Select Appropriate Dataset") 


    def getInfo(self):
      
      if  self.__import_file_path != None and self.__df.empty != True:
        self.__thiscanvas.grid_forget()
        self.__thiscanvasf.get_tk_widget().grid_forget()
        self.__thisTextArea.grid(row=0,column=0)
        self.__thisTextArea.delete(1.0,END)
        buffer = io.StringIO()
        self.__df.info(buf=buffer)
        s = buffer.getvalue()
        self.__thisTextArea.insert(1.0,"#--------   Info about Data in the Dataset ("+os.path.basename( self.__import_file_path)+")  --------#\n\n\n\n")
        self.__thisTextArea.insert(25.0,s)
      else:  
        messagebox.showerror("Error", "Select Appropriate Dataset")


    def help(self):
      messagebox.showinfo("Help", "Simple GUI application 'PLOTTER' to plot data from csv files.") 

    def quit(self):
       ans=messagebox.askquestion("Quit Application","Are You Sure?")
       if ans=='yes':
           self.__window.destroy()
       else:
         return

    def clear(self):
            self.__thiscanvasf.get_tk_widget().grid_forget()
            self.__thisTextArea.delete(1.0,END)
      
    def run(self):
        self.__window.mainloop()

plot=Plotter()
plot.run()

    



