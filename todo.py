from tkinter import *          # importing the required modules                                         
from tkinter import messagebox          # importing the messagebox module from the tkinter library  
import sqlite3 as sql       # importing the sqlite3 module as sql  
 

def add_task():         # defining the function to add tasks to the list  
    task_string = task_field.get()        # getting the string from the entry field  
    if len(task_string) == 0:       # checking whether the string is empty or not 
        messagebox.showinfo('Error', 'Field is Empty.')        # displaying a message box with 'Empty Field' message         
    else:  
        tasks.append(task_string)     # adding the string to the tasks list   
        the_cursor.execute('insert into tasks values (?)', (task_string ,))   # using the execute() method to execute a SQL statement    
        list_update()          # calling the function to update the list    
        task_field.delete(0, 'end')     # deleting the entry in the entry field
  
 
def list_update():  # defining the function to update the list      
    clear_list()   # calling the function to clear the list      
    for task in tasks:  # iterating through the strings in the list
        task_listbox.insert('end', task)   # using the insert() method to insert the tasks in the list box  
  

def delete_task():  # defining the function to delete a task from the list    
    try:  # using the try-except method    
        the_value = task_listbox.get(task_listbox.curselection())  # getting the selected entry from the list box        
        if the_value in tasks:  # checking if the stored value is present in the tasks list      
            tasks.remove(the_value)   # removing the task from the list
            list_update()   # calling the function to update the list  
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  # using the execute() method to execute a SQL statement
    except:   
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')   # displaying the message box with 'No Item Selected' message for an exception      
  
  
def delete_all_tasks():  # function to delete all tasks from the list
     
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')   # displaying a message box to ask user for confirmation      
    if message_box == True:  # if the value turns to be True        
        while(len(tasks) != 0):   # using while loop to iterate through the tasks list until it's empty              
            tasks.pop()  # using the pop() method to pop out the elements from the list        
        the_cursor.execute('delete from tasks')   # using the execute() method to execute a SQL statement          
        list_update()  # calling the function to update the list 
  
 
def clear_list():  # function to clear the list 
     
    task_listbox.delete(0, 'end')  # using the delete method to delete all entries from the list box 
  

def close():  # function to close the application 
     
    print(tasks)  # printing the elements from the tasks list       
    guiWindow.destroy()  # using the destroy() method to close the application
  
 
def retrieve_database():  # function to retrieve data from the database 
     
    while(len(tasks) != 0):  # using the while loop to iterate through the elements in the tasks list 
        tasks.pop()  # using the pop() method to pop out the elements from the list
    
    for row in the_cursor.execute('select title from tasks'):  # iterating through the rows in the database table          
        tasks.append(row[0])  # using the append() method to insert the titles from the table in the list 
  
 
if __name__ == "__main__":  # main function 
     
    guiWindow = Tk()  # creating an object of the Tk() class 
    
    guiWindow.title("To-Do List ")  # setting the title of the window  
    
    guiWindow.geometry("665x400+550+250")  # setting the geometry of the window  
  
    guiWindow.resizable(0, 0)    # disabling the resizable option  
    
    guiWindow.configure(bg = "#B5E5CF")  # setting the background color to #B5E5CF 
   
    the_connection = sql.connect('listOfTasks.db')  # using the connect() method to connect to the database  
     
    the_cursor = the_connection.cursor()  # creating the cursor object of the cursor class 
    
    the_cursor.execute('create table if not exists tasks (title text)')  # using the execute() method to execute a SQL statement  
      
    tasks = []  # defining an empty list      
    
    functions_frame = Frame(guiWindow, bg = "black") # defining frames using the tk.Frame() widget    
    
    functions_frame.pack(side = "top", expand = True, fill = "both")  # using the pack() method to place the frames in the application  
   
    task_label = Label( functions_frame,text = "Enter the Task:",  # defining another label using the Label() widget 
        font = ("arial", "14", "bold"),  
        background = "black", 
        foreground="white"
    )  
    task_label.place(x = 20, y = 30)   # using the place() method to place the label in the application  
      
    # defining an entry field using the Entry() widget  
    task_field = Entry(  
        functions_frame,  
        font = ("Arial", "14"),  
        width = 42,  
        foreground="black",
        background = "white",  
    )  
    # using the place() method to place the entry field in the application  
    task_field.place(x = 180, y = 30)  
  
    # adding buttons to the application using the Button() widget  
    add_button =Button(  
        functions_frame,  
        text = "Add Task",  
        width = 15,
        bg='#D4AC0D',font=("arial", "14", "bold"),
        command = add_task,
        
    )  
    del_button = Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 15,
        bg='#D4AC0D', font=("arial", "14", "bold"),
        command = delete_task,  
    )  
    del_all_button = Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 15,
        font=("arial", "14", "bold"),
        bg='#D4AC0D',
        command = delete_all_tasks  
    )  
    exit_button = Button(  
        functions_frame,  
        text = "Exit",  
        width = 52,
        bg='#D4AC0D',  font=("arial", "14", "bold"),
        command = close  
    )  
    # using the place() method to set the position of the buttons in the application  
    add_button.place(x = 18, y = 80,)  
    del_button.place(x = 240, y = 80)  
    del_all_button.place(x = 460, y = 80)  
    exit_button.place(x = 17, y = 330)  
  
    # defining a list box using the tk.Listbox() widget  
    task_listbox = Listbox(  
        functions_frame,  
        width = 57,  
        height = 7,  
        font="bold",
        selectmode = 'SINGLE',  
        background = "WHITE",
        foreground="BLACK",    
        selectbackground = "#D4AC0D",  
        selectforeground="BLACK"
    )  
    # using the place() method to place the list box in the application  
    task_listbox.place(x = 17, y = 140)  
  
    # calling some 
    retrieve_database()  
    list_update()  
    # using the mainloop() method to run the application  
    guiWindow.mainloop()  
    # establishing the connection with database  
    the_connection.commit()  
    the_cursor