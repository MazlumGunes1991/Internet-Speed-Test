from tkinter import *
import speedtest

root = Tk()
root.title("Internet Speed Test")
root.geometry("360x600")
root.resizable(False,False)
root.configure(bg="#1a212d")

def Test():

    test = speedtest.Speedtest()

    Uploading = round(test.upload() / (1024 * 1024),2)
    upload.config(text=Uploading)

    Downloading = round(test.download() / (1024 * 1024),2)
    download1.config(text=Downloading)
    download2.config(text=Downloading)

    serverNames = []
    test.get_servers(serverNames)
    ping.config(text=test.results.ping)

# Icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

# Images
Top = PhotoImage(file="top.png")
Label(root,image=Top,bg="#1a212d").pack()

Main = PhotoImage(file="main.png")
Label(root,image=Main,bg="#1a212d").pack(pady=20)

Btn = PhotoImage(file="button.png")
Button = Button(root,image=Btn,bg="#1a212d",bd=0,activebackground="#1a212d",cursor="hand2",command=Test)
Button.pack(pady=10)

# Label
Label(root,text="PING",bg="#384056",font="arial 10 bold").place(x=50,y=0)
Label(root,text="DOWNLOAD",bg="#384056",font="arial 10 bold").place(x=140,y=0)
Label(root,text="UPLOAD",bg="#384056",font="arial 10 bold").place(x=260,y=0)

Label(root,text="MS",font="arial 7 bold",bg="#384056",fg="white").place(x=60,y=80)
Label(root,text="MBPS",font="arial 7 bold",bg="#384056",fg="white").place(x=165,y=80)
Label(root,text="MBPS",font="arial 7 bold",bg="#384056",fg="white").place(x=275,y=80)

Label(root,text="Download",font="arial 15 bold",bg="#384056",fg="white").place(x=140,y=260)
Label(root,text="Mbps",font="arial 15 bold",bg="#384056",fg="white").place(x=160,y=360)

ping = Label(root,text="00",font="arial 13 bold",bg="#384056",fg="white")
ping.place(x=70,y=60,anchor="center")
download1 = Label(root,text="00",font="arial 13 bold",bg="#384056",fg="white")
download1.place(x=180,y=55,anchor="center")
upload = Label(root,text="00",font="arial 13 bold",bg="#384056",fg="white")
upload.place(x=290,y=55,anchor="center")

download2 = Label(root,text="00",font="arial 40 bold",bg="#384056")
download2.place(x=185,y=325,anchor="center")

root.mainloop()