from tkinter import Label , Entry , Button , messagebox ,Tk , LEFT , END 
from tkinter.filedialog import askopenfilename
import pyAesCrypt
from webbrowser import open_new_tab
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
window = Tk()
window.iconbitmap(r'icon.ico')
window.title(' AES file Encryption v2020.0.2 ')
window.geometry('500x670')
window.resizable(False , False)
bufferSize = 64 * 1024
def about_me():
    open_new_tab('http://sh-nobody.blog.ir')
def space():
    Label(text=" \n sh-nobody.blog.ir  - TEL = @aghamilouei \n " , bg = 'grey').pack(fill = 'x')
def ch_file():
    global file
    file=askopenfilename()
    address.config(text = file)
def get_from_password8():
   global userpass
   userpass = password8.get()
   password8.delete(0 , END)
   print(" ~ Now your password is {}".format(userpass))
def enc():
    print("<Encrypt>")
    bufferSize = 64 * 1024
    pyAesCrypt.encryptFile(file,file+".aes",userpass,bufferSize)
    result.configure(text=' file < Encrypted >')
def dec():
    bufferSize = 64 * 1024
    try:
        pyAesCrypt.decryptFile(file,file+"_decrypted",userpass,bufferSize)
        result.configure(text =' file < Decrypted >')

    except Exception as error:
        result.configure(text=error)
guide = Label(text='''
 $ with this app you can encrypt or decrypt encrypted files 
 first choose your file then Enter the your password after,
 You can choose <decrypt> or <encrypt> . $ \n please read the guide first ;)  User guide in footer . \n  ''' , bg = 'grey37' , fg ='white').pack(fill = 'x' , side = 'top')
def aboutme():
    messagebox.showinfo('User guide and about me' , ''' Hello this app encrypt and decrypt , encrypted files using 
    AES (Advance Encrypting Standard) and you can encrypt 
    and keep your files securely. 
    this app is built by AmirReza Ghamlouei and its alright reserved. 
    these are my contact information :
    TEL => @aghamilouei
    Blog => sh-nobody.blog.ir

    TO USE go throw these steps :
    1. choose your file.
    2. enter your pass and confirm it.
    3. almost there , now choose encrypt or decrypt.
    4. for decrypted files omit the last format part.
    ... Good luck ...
    سید امیررضا غمیلویی
    No one is friend , No one is enamy thats the way I dont get 
    suprised !''')
    open_new_tab('https://sh-nobody.blog.ir')
address = Label(text='@ the Address of file will be here',height = 2 ,bg='grey44' , justify = LEFT,font = ('tahoma' , 8) )
address.pack(fill='x')
choosethefile = Button(text = 'Choose Your File - click -  ' ,bg = 'grey25',fg = 'white', command = ch_file ).pack(fill = 'x' )
guide_0 = Label(text='Enter your password in the BOX BELOW \n \n ⇓ ⇓ ⇓ ⇓ ⇓ \n ').pack()
password8 = Entry(bg='grey37' , fg = 'white' , width= 35 , justify = 'center')
password8.pack(pady = 8)
confrim = Button(text=' I confrim my PASSWORD' , command = get_from_password8).pack()
Label(text = '').pack()
Button(text = '< Encrypt >' , command = enc).pack()
Label(text = '').pack()
Label(text = 'or').pack()
Label(text = '').pack()
Button(text = '< Decrypt >' , command = dec).pack()
Label(text="").pack()
result=Label(text=' You will see the result here' , font=('arial' , 14))
result.pack(fill = 'x') 
Label(text="").pack()
guide_1 = Label(text=' / after decryption process omit the ._decrypted at the end of the file \ ' , bg ='grey44').pack(side = 'bottom' , fill ='x')
about = Button(text = 'User guide and about me' , bg = 'seashell3' , command = aboutme ).pack(side='bottom')
window.mainloop()
 

















