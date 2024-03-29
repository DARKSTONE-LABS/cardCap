import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageGrab

class Viewfinder(tk.Toplevel):
    def __init__(self, parent, width=320, height=320):
        super().__init__(parent)
        self.width = width
        self.height = height
        self.configure(bg='black')
        self.geometry(f"{width}x{height}+200+200")
        self.attributes("-topmost", True, "-alpha", 0.3)
        self.overrideredirect(True)
        self.bind("<B1-Motion>", self.drag_window)

    def drag_window(self, event):
        x = self.winfo_pointerx() - self.width // 2
        y = self.winfo_pointery() - self.height // 2
        self.geometry(f"+{x}+{y}")

class ScreenCaptureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Capture Tool")
        self.root.geometry("400x200")  # Make initial window larger

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), borderwidth='4')
        self.style.configure('TFrame', background='#334353')
        self.style.configure('TLabel', background='#334353', foreground='white')
        self.style.configure('TEntry', foreground='black', font=('Helvetica', 12))

        self.frame = ttk.Frame(root, padding="10", style='TFrame')
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.filename_label = ttk.Label(self.frame, text="Filename:", style='TLabel')
        self.filename_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.filename_entry = ttk.Entry(self.frame, font=('Helvetica', 12), width=20)
        self.filename_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        self.filename_entry.insert(0, "captured_animation.gif")

        self.launch_viewfinder_btn = ttk.Button(self.frame, text="Launch Viewfinder", command=self.launch_viewfinder)
        self.launch_viewfinder_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        self.start_capture_btn = ttk.Button(self.frame, text="Start Capture", state="disabled", command=self.start_capture)
        self.start_capture_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        self.stop_and_export_btn = ttk.Button(self.frame, text="Stop and Export", state="disabled", command=self.stop_and_export)
        self.stop_and_export_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        self.viewfinder = None
        self.frames = []

    def launch_viewfinder(self):
        if not self.viewfinder or not self.viewfinder.winfo_exists():
            self.viewfinder = Viewfinder(self.root)
            self.start_capture_btn['state'] = 'normal'
        else:
            messagebox.showinfo("Info", "Viewfinder is already launched.")

    def capture_screen(self):
        if self.viewfinder:
            x0 = self.viewfinder.winfo_rootx()
            y0 = self.viewfinder.winfo_rooty()
            x1 = x0 + self.viewfinder.width
            y1 = y0 + self.viewfinder.height
            img = ImageGrab.grab(bbox=(x0, y0, x1, y1))
            self.frames.append(img)

    def start_capture(self):
        self.capturing = True
        self.stop_and_export_btn['state'] = 'normal'
        self.start_capture_btn['state'] = 'disabled'
        self.capture_frames()

    def capture_frames(self):
        if self.capturing:
            self.capture_screen()
            self.root.after(100, self.capture_frames)

    def stop_and_export(self):
        self.capturing = False
        gif_path = self.filename_entry.get()
        if self.frames:
            self.frames[0].save(gif_path, save_all=True, append_images=self.frames[1:], optimize=False, duration=40, loop=0)
            messagebox.showinfo("Success", f"Animation saved as {gif_path}")
            self.frames.clear()
        self.launch_viewfinder_btn['state'] = 'normal'
        self.stop_and_export_btn['state'] = 'disabled'
        if self.viewfinder:
            self.viewfinder.destroy()

def main():
    root = tk.Tk()
    app = ScreenCaptureApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
