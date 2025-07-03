import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta  # Import datetime modules for time checking

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("File Transfer")

        self.transfer_btn = Button(self, text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        self.exit_btn = Button(self, text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10, 20), pady=(0, 15))

        self.sourceDir_btn = Button(self, text="Select Source", width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        self.source_dir = Entry(self, width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30, 0))

        self.destDir_btn = Button(self, text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15, 10))

        self.destination_dir = Entry(self, width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        self.source_dir.delete(0, END)
        self.source_dir.insert(0, selectSourceDir)

    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)

    def transferFiles(self):
        # Get current time
        now = datetime.now()
        # Calculate cutoff time for 24 hours ago
        cutoff = now - timedelta(hours=24)

        source = self.source_dir.get()
        destination = self.destination_dir.get()

        # Basic validation for source and destination paths
        if not source or not destination:
            print("Please select both source and destination directories.")
            return
        if not os.path.exists(source):
            print("Source directory does not exist.")
            return

        # List all files in the source directory
        source_files = os.listdir(source)

        for file_name in source_files:
            full_path = os.path.join(source, file_name)

            # Get last modified time and convert it to a datetime object
            mod_time = datetime.fromtimestamp(os.path.getmtime(full_path))

            # Check if the file was modified in the last 24 hours
            if mod_time > cutoff:
                # Move file to destination directory
                shutil.move(full_path, destination)
                print(f"{file_name} was successfully transferred.")
            else:
                print(f"{file_name} skipped (not modified in last 24 hours).")

    def exit_program(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x150")  # Set window size so widgets fit
    App = ParentWindow(root)
    App.pack(fill=BOTH, expand=YES)
    root.mainloop()
