from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        # variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arreest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthmark=StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()

        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE',font=('times new roman',40,'bold'),bg='black',fg='white')
        lbl_title.place(x=0,y=0,width=1530,height=70)

        #logo
        img_logo=Image.open('img/logo.webp')
        img_logo=img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=80,y=5,width=60,height=60)

        #img_frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1530,height=130)

        #img_1
        img1=Image.open('img/p1.jpg')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)
        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        #img_2
        img_2=Image.open('img/p2.jpg')
        img_2=img_2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img_2)
        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)

        #img_3
        img_3=Image.open('img/p3.jpg')
        img_3=img_3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img_3)
        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1080,y=0,width=540,height=160)

        # frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=200,width=1500,height=560)

        #----------------upper frame---------------------
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information',font=('times new roman',11,'bold'),fg='red',bg='white')
        upper_frame.place(x=10,y=10,width=1480,height=270)

                                    # information entry
        # case_id
        caseid=Label(upper_frame,text='Case ID:',font=('arial',11,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        case_entry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('arial',11,'bold'))
        case_entry.grid(row=0,column=1,padx=2,sticky=W)

        # criminal_no
        criminal_no=Label(upper_frame,text='Criminal NO:',font=('arial',11,'bold'),bg='white')
        criminal_no.grid(row=0,column=2,padx=2,sticky=W,pady=7)

        text_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=('arial',11,'bold'))
        text_criminal_no.grid(row=0,column=3,padx=2,pady=7)

        # criminal_name
        criminal_name=Label(upper_frame,text='Criminal Name:',font=('arial',11,'bold'),bg='white')
        criminal_name.grid(row=1,column=0,padx=2,sticky=W,pady=7)

        text_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        text_name.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        # nickname
        nick_name=Label(upper_frame,text='NickName:',font=('arial',11,'bold'),bg='white')
        nick_name.grid(row=1,column=2,padx=2,sticky=W,pady=7)

        text_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=('arial',11,'bold'))
        text_nickname.grid(row=1,column=3,padx=2,pady=7)

        # arrestdate
        arrest_date=Label(upper_frame,text='Arrest Date:',font=('arial',11,'bold'),bg='white')
        arrest_date.grid(row=2,column=0,padx=2,sticky=W,pady=7)

        text_arreset_date=ttk.Entry(upper_frame,textvariable=self.var_arreest_date,width=22,font=('arial',11,'bold'))
        text_arreset_date.grid(row=2,column=1,padx=2,pady=7)

        # date of time
        date_of_crime=Label(upper_frame,text='Date Of Crime:',font=('arial',11,'bold'),bg='white')
        date_of_crime.grid(row=2,column=2,padx=2,sticky=W,pady=7)

        text_dcrime=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=('arial',11,'bold'))
        text_dcrime.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        # address
        address=Label(upper_frame,text='Address:',font=('arial',11,'bold'),bg='white')
        address.grid(row=3,column=0,padx=2,sticky=W,pady=7)

        text_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        text_address.grid(row=3,column=1,padx=2,pady=7)

        # age
        age=Label(upper_frame,text='Age:',font=('arial',11,'bold'),bg='white')
        age.grid(row=3,column=2,padx=2,sticky=W,pady=7)

        text_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('arial',11,'bold'))
        text_age.grid(row=3,column=3,padx=2,pady=7)

        # occupution
        occupution=Label(upper_frame,text='Occupation:',font=('arial',11,'bold'),bg='white')
        occupution.grid(row=4,column=0,padx=2,sticky=W,pady=7)

        text_occupution=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=('arial',11,'bold'))
        text_occupution.grid(row=4,column=1,padx=2,pady=7)

        # birthmark
        birth_mark=Label(upper_frame,text='Birth Mark:',font=('arial',11,'bold'),bg='white')
        birth_mark.grid(row=4,column=2,padx=2,sticky=W,pady=7)

        text_bm=ttk.Entry(upper_frame,textvariable=self.var_birthmark,width=22,font=('arial',11,'bold'))
        text_bm.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        # crime type
        crime_type=Label(upper_frame,text='Crime Type:',font=('arial',11,'bold'),bg='white')
        crime_type.grid(row=0,column=4,padx=2,sticky=W,pady=7)

        text_ct=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=('arial',11,'bold'))
        text_ct.grid(row=0,column=5,padx=2,pady=7)

        # fathername
        f_name=Label(upper_frame,text='Father Name:',font=('arial',11,'bold'),bg='white')
        f_name.grid(row=1,column=4,padx=2,sticky=W,pady=7)

        text_fname=ttk.Entry(upper_frame,textvariable=self.var_father_name,width=22,font=('arial',11,'bold'))
        text_fname.grid(row=1,column=5,padx=2,pady=7)

        # gender
        gender=Label(upper_frame,text='Gender:',font=('arial',11,'bold'),bg='white')
        gender.grid(row=2,column=4,padx=2,sticky=W,pady=7)

        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=730,y=90,width=190,height=30)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=('arial',9,'bold'),bg='white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W) #radio button

        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=('arial',9,'bold'),bg='white')
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)
        # wanted
        wanted=Label(upper_frame,text='Most Wanted:',font=('arial',11,'bold'),bg='white')
        wanted.grid(row=3,column=4,padx=2,sticky=W,pady=7)

        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white') #redio frame
        radio_frame_wanted.place(x=730,y=130,width=190,height=30)

        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='no',font=('arial',9,'bold'),bg='white')
        no.grid(row=0,column=0,pady=2,padx=5,sticky=W) #radio button

        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='Yes',font=('arial',9,'bold'),bg='white')
        yes.grid(row=0,column=1,pady=2,padx=5,sticky=W)

        # buttons
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white') 
        button_frame.place(x=5,y=200,width=620,height=45)
        # add button
        btn_add=Button(button_frame,command=self.add_data,text='Save',font=('arial',13,'bold'),width=14,bg='green',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)
        # update button
        btn_update=Button(button_frame,command=self.update_data,text='Update',font=('arial',13,'bold'),width=14,bg='green',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)
        # Delete button
        btn_del=Button(button_frame,command=self.delete_data,text='Delete',font=('arial',13,'bold'),width=14,bg='green',fg='white')
        btn_del.grid(row=0,column=2,padx=3,pady=5)
        # Clear button
        btn_clr=Button(button_frame,command=self.clear_data,text='Clear',font=('arial',13,'bold'),width=14,bg='green',fg='white')
        btn_clr.grid(row=0,column=3,padx=3,pady=5)
        # back ground right side img
        img_4=Image.open('img/p5.jpeg')
        img_4=img_4.resize((470,245),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img_4)
        self.img_4=Label(upper_frame,image=self.photo4)
        self.img_4.place(x=1000,y=0,width=470,height=245)

        #down frame 
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=280,width=1480,height=270)

        # search record 
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Criminal Record',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,text='Search By:',font=('arial',11,'bold'),bg='red',fg='white')
        search_by.grid(row=0,column=0,padx=2,sticky=W)

        self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial',11,'bold'),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=('arial',11,'bold'))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        # search button
        btn_search=Button(search_frame,command=self.search_data,text='Search',font=('arial',13,'bold'),width=14,bg='green',fg='white')
        btn_search.grid(row=0,column=3,padx=3,pady=5)
        # all button
        btn_all=Button(search_frame,command=self.fetch_data,text='Show All',font=('arial',13,'bold'),width=14,bg='green',fg='white')
        btn_all.grid(row=0,column=4,padx=3,pady=5) 

        crime_agency=Label(search_frame,text='NATIONAL CRIME AGENCY',font=('arial',30,'bold'),bg='white',fg='crimson')
        crime_agency.grid(row=0,column=5,padx=50,sticky=W,pady=0)

        # table frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,columns=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='CaseId')
        self.criminal_table.heading('2',text='Criminal No')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='Nick Name')
        self.criminal_table.heading('5',text='Arrest Date')
        self.criminal_table.heading('6',text='Crime of Date')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='Birth Mark')
        self.criminal_table.heading('11',text='Crime Type')
        self.criminal_table.heading('12',text='Father Name')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')

        self.criminal_table['show']='headings'

        self.criminal_table.column('1',width=100)
        self.criminal_table.column('2',width=100)
        self.criminal_table.column('3',width=100)
        self.criminal_table.column('4',width=100)
        self.criminal_table.column('5',width=100)
        self.criminal_table.column('6',width=100)
        self.criminal_table.column('7',width=100)
        self.criminal_table.column('8',width=100)
        self.criminal_table.column('9',width=100)
        self.criminal_table.column('10',width=100)
        self.criminal_table.column('11',width=100)
        self.criminal_table.column('12',width=100)
        self.criminal_table.column('13',width=100)
        self.criminal_table.column('14',width=100)

        self.criminal_table.pack(fill=BOTH,expand=1)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    # Add Function
    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='root',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                                                            self.var_case_id.get(),
                                                                                                            self.var_criminal_no.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_nickname.get(),
                                                                                                            self.var_arreest_date.get(),
                                                                                                            self.var_date_of_crime.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_age.get(),
                                                                                                            self.var_occupation.get(),
                                                                                                            self.var_birthmark.get(),
                                                                                                            self.var_crime_type.get(),
                                                                                                            self.var_father_name.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_wanted.get()
                                                                                                           ))

                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record has been added')

            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

    # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='root',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from criminal')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()   

    # get cursor
    def get_cursor(self,event=""):
        cursur_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursur_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arreest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthmark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])

    # update

    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure update this criminal record')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='root',database='management')
                    my_cursor=conn.cursor() 
                    my_cursor.execute('Update criminal set Criminal_no=%s, Criminal_name=%s, Nick_name=%s, Arrest_Date=%s, Date_of_Crime=%s, Address=%s, age=%s, Occupation=%s, BirthMark=%s, CrimeType=%s, FatherName=%s, Gender=%s, Wanted=%s where Case_id=%s',(                                                                                                                                                                                                                                                   self.var_criminal_no.get(),
                                                                                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                                                                                        self.var_nickname.get(),
                                                                                                                                                                                                                                                        self.var_arreest_date.get(),
                                                                                                                                                                                                                                                        self.var_date_of_crime.get(),
                                                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                                                        self.var_age.get(),
                                                                                                                                                                                                                                                        self.var_occupation.get(),
                                                                                                                                                                                                                                                        self.var_birthmark.get(),
                                                                                                                                                                                                                                                        self.var_crime_type.get(),
                                                                                                                                                                                                                                                        self.var_father_name.get(),
                                                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                                                        self.var_wanted.get(),
                                                                                                                                                                                                                                                        self.var_case_id.get()
                                                                                                                                                                                                                                                       ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()  
                messagebox.showinfo('Success','Criminal record successfully added')  
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')
    
    # delete
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure update this criminal record')
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='root',database='management')
                    my_cursor=conn.cursor()
                    sql='delete from criminal where Case_id=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record successfully Deleted')  
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')

    # clear
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arreest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthmark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")

    # search
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All Fields are Required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='root',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from criminal where ' +str(self.var_com_search.get())+" Like'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()   
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')


if __name__=='__main__':
    root=Tk()
    obj=Criminal(root)
    root.mainloop()