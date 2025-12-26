import tkinter as tk
from tkinter import messagebox,ttk #ttk is themed tkinter updated version of tkinter

def add_contact():
    data = (entry_name.get(), entry_phone.get(), entry_email.get(), entry_address.get())
    if all(data[:2]): #name and phone are mandatory 
        #if all checks insert upto 2 index means atleast name and phone then only add_contact works
        tree.insert("", tk.END, values=data) #"" means it is the main root in which we have to add , tk.end means last empty box se add krna stzrt karo
        clear_entries() #values jo data me h wo bharna h
    else:
        messagebox.showwarning("Input Error")
    
def delete_contact():
    selected = tree.selection()
    if selected:
        tree.delete(selected)
    else:
        messagebox.showwarning("selection error") 

def update_contact():
    selected = tree.selection()
    if selected:
        data = (entry_name.get(), entry_phone.get(), entry_email.get(), entry_address.get())
        tree.item(selected, values=data)
        clear_entries()
    else:
        messagebox.showwarning("selection error")

def search_contact():
    query = entry_name.get().lower() #entry_name yaha name h bcoz hum name se search krenge
    #.get data fetch krne ko h , .lower() hai bcoz if user n input capital me kiya toh automaticaly by default search hoga small m
    if not query:
        messagebox.showwarning("enter name in namefield to search")
        return
    for item in tree.get_children(): #get children root ka hrr ek ek row h row ko children bola h
        if query in str(tree.item(item)['values']).lower(): #tree.tree(item) detail de rahi h pure selected row kee , values definee h taki keval jo value likhi h name , phone etc.. wahi de value m
            tree.selection_set(item)
            tree.focus(item)
            return
        messagebox.showinfo("search result not found")

def view_contact():
    all_items = tree.get_children()
    if not all_items:
        messagebox.showinfo("Info", "The contact list is empty!")
    else:
        tree.selection_remove(tree.selection())#firstly pehle k data ko clear krte h fr newshow hota h 
        messagebox.showinfo("Contact List", f"Total contacts: {len(all_items)}")
    
def fill_entries_from_selection(item):
    clear_entries()
    values = tree.item(item)["values"]
    entry_name.insert(0,values[0])
    entry_phone.insert(0,values[1])
    entry_email.insert(0,values[2])
    entry_address.insert(0,values[3])

def on_tree_select(event):
    selected = tree.selection()
    if selected:
        fill_entries_from_selection(selected[0]) #fill entries ek baar me ek ka hi data deta h or tkinter ka treeview ek baar me bahoot sare data de skta h toh hum 0 se specify kr rahe h pehli selected row ka deta de do


    

def clear_entries():
        entry_name.delete(0, tk.END) #0 se lekr tk.end means pure last value tk delete kro
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_address.delete(0, tk.END)
    
    #----window GUI setup------
root = tk.Tk()  #tk.TK creates main window root is name of main window
root.title("Contact book")
root.geometry("400x250")
    
    #----input fields----
frame_field = tk.LabelFrame(root, text = "Contact Information") #frame_field is a invisible container
frame_field.pack(pady=10, padx=20) #label sbhi buttons, or necessary text,images show krta h

    #name section
label_name = tk.Label(frame_field, text="Name:").grid(row=0, column=0, sticky="w")
entry_name= tk.Entry(frame_field, width=35)
entry_name.grid(row=0, column=1, pady=5, padx=10)#grid row ND Column create krta h 


#phone
label_phone = tk.Label(frame_field, text="phone:").grid(row=1, column=0, sticky="w")
entry_phone = tk.Entry(frame_field, width=35)
entry_phone.grid(row=1, column=1, pady=5, padx=10)
    #email
label_email = tk.Label(frame_field, text="Email:" ).grid(row=2, column=0, sticky="w")
entry_email = tk.Entry(frame_field, width=35)
entry_email.grid(row=2, column=1, pady=5, padx=10)

    #address
label_address= tk.Label(frame_field, text="Address:,").grid(row=3, column=0, sticky="w")
entry_address = tk.Entry(frame_field, width=35)
entry_address.grid(row=3, column=1, pady=5, padx=10)



        #buttons
frame_btns= tk.Frame(root)
frame_btns.pack(pady=10)

tk.Button(frame_btns, text="Add Contact", command=add_contact, width=12, background= "#0008D9", foreground="#FFFFFF").pack(side=tk.LEFT, padx=5)
tk.Button(frame_btns, text="search contact", width=12, command=search_contact, background="#541faf", foreground="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame_btns, text="Delete contact", command=delete_contact, width=12, background="#2C240B", foreground="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame_btns, width=12, text="update contact", command=update_contact, background="#dc3535", foreground="white").pack(side=tk.LEFT, padx=5)
        #pack shows and set all data in a line

        #treeview section
columns= ("Name", "Phone", "Email", "Address")
tree = ttk.Treeview(root, columns=columns, show='headings') #treeview is widget of tkinter that show data in table

for col in columns:# loop h jo col naam ke variable m column ke shabd ko daalti h first time name then phone etc
        tree.heading(col, text=col)#text = col shows heading pr kya likha hua dikhna chahhye
        tree.column(col, width=20, anchor="center")
        
#bind selection
tree.bind('<<TreeViewSelect>>'),on_tree_select#tree is variable name of treeview .bind joins action and function
#<<treeviewselect>> is a virtual event jp signal deta h jb user table ki kisi bhi row pr click karke use select kare
#on tree select is a function jo tb chlta h jb select hota h 
#scrollbar for table
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side = tk.RIGHT, fill=tk.Y)#pack krna jaruri h taki screen pr dikje
tree.pack(pady=15, padx=15, fill=tk.BOTH, expand=True)#fill means gap in box ko fill krna both means from both up down left right
root.mainloop()#expand means to expand if needed = true
#ttk.scollbar se hum ek scrollbar ka widget bana rahe h orient = verticall shows scrollbar is up down scollbar
#tree.yview this line tells scrollbar to move in y axis when user do from mouse
#yscrll= scrollbar.set ,scollbar.set gives signal jb mouse wheel table ko upar neeche krta hai so it gives signal uske hisaab se scollbar kee lambayi or position ko set krte h 
#side means right side me scrollbar hoga , fill=tk.y means pure y axis me hoga 