import os
import socket
import threading
from tkinter import *
from tkinter import filedialog, messagebox

# Initialize main window
root = Tk()
root.title("File Transfer")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False, False)

# Function to get the absolute path of an image
def get_image_path(filename):
    path = os.path.join(os.getcwd(), "Images", filename)
    if not os.path.exists(path):
        messagebox.showerror("Error", f"Image file '{filename}' not found!")
        return None
    return path

# -------------------- SEND FILE FUNCTION --------------------
def send_file():
    sender = Toplevel(root)
    sender.title("Send File")
    sender.geometry("450x300+500+250")
    sender.configure(bg="#f4fdfe")
    sender.resizable(False, False)

    def browse_file():
        global filename
        filename = filedialog.askopenfilename()
        file_label.config(text=f"File: {os.path.basename(filename)}")

    def send():
        if not filename:
            messagebox.showerror("Error", "Please select a file!")
            return
        
        receiver_ip = ip_entry.get()
        port = int(port_entry.get())

        try:
            s = socket.socket()
            s.connect((receiver_ip, port))
            file = open(filename, "rb")
            file_data = file.read(1024)
            
            while file_data:
                s.send(file_data)
                file_data = file.read(1024)
            
            file.close()
            s.close()
            messagebox.showinfo("Success", "File sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"File transfer failed: {e}")

    # UI Elements for Sending
    Label(sender, text="Enter Receiver IP:", bg="#f4fdfe").place(x=20, y=20)
    ip_entry = Entry(sender, width=30)
    ip_entry.place(x=150, y=20)

    Label(sender, text="Enter Port:", bg="#f4fdfe").place(x=20, y=60)
    port_entry = Entry(sender, width=10)
    port_entry.place(x=150, y=60)
    port_entry.insert(0, "9999")  # Default port

    Button(sender, text="Browse File", command=browse_file).place(x=20, y=100)
    file_label = Label(sender, text="No file selected", bg="#f4fdfe")
    file_label.place(x=150, y=105)

    Button(sender, text="Send File", command=send).place(x=150, y=150)

# -------------------- RECEIVE FILE FUNCTION --------------------
def receive_file():
    receiver = Toplevel(root)
    receiver.title("Receive File")
    receiver.geometry("450x300+500+250")
    receiver.configure(bg="#f4fdfe")
    receiver.resizable(False, False)

    def start_server():
        port = int(port_entry.get())
        
        try:
            s = socket.socket()
            s.bind(("", port))
            s.listen(1)
            messagebox.showinfo("Info", f"Waiting for connection on port {port}...")
            
            conn, addr = s.accept()
            messagebox.showinfo("Connected", f"Connected with {addr}")

            file = open("received_file", "wb")
            file_data = conn.recv(1024)
            
            while file_data:
                file.write(file_data)
                file_data = conn.recv(1024)
            
            file.close()
            conn.close()
            messagebox.showinfo("Success", "File received successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"File reception failed: {e}")

    # UI Elements for Receiving
    Label(receiver, text="Enter Port:", bg="#f4fdfe").place(x=20, y=20)
    port_entry = Entry(receiver, width=10)
    port_entry.place(x=150, y=20)
    port_entry.insert(0, "9999")  # Default port

    Button(receiver, text="Start Receiving", command=lambda: threading.Thread(target=start_server).start()).place(x=150, y=60)

# -------------------- MAIN UI --------------------
# Load main window icon
icon_path = get_image_path("icon.png")
if icon_path:
    image_icon = PhotoImage(file=icon_path)
    root.iconphoto(False, image_icon)

# Title Label
Label(root, text="File Transfer", font=('Acumin Variable Concept', 20, 'bold'), bg="#f4fdfe").pack(pady=20)

# Separator Frame
Frame(root, width=400, height=2, bg="#f3f5f6").place(x=25, y=80)

# Load Send Button Image
send_image_path = get_image_path("icon.png")
if send_image_path:
    send_image = PhotoImage(file=send_image_path)
    send_button = Button(root, image=send_image, bg="#f4fdfe", bd=0, command=send_file)
    send_button.place(x=50, y=100)

# Load Receive Button Image
receive_image_path = get_image_path("receive.png")
if receive_image_path:
    receive_image = PhotoImage(file=receive_image_path)
    receive_button = Button(root, image=receive_image, bg="#f4fdfe", bd=0, command=receive_file)
    receive_button.place(x=300, y=100)

# Button Labels
Label(root, text="Send", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=65, y=200)
Label(root, text="Receive", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=300, y=200)

# Load Background Image
background_path = get_image_path("background.png")
if background_path:
    background = PhotoImage(file=background_path)
    Label(root, image=background).place(x=-2, y=323)

# Run the application
root.mainloop()
