import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import sqlite3
from tkinter import Canvas, messagebox
import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk
from LoginRis import create_database
from home import HomePage

class LoginRegisterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Oẳn Tù Tì - Đăng Nhập & Đăng Ký")
        self.root.geometry("1200x550")
        self.root.resizable(False, False)

        create_database()
        self.add_main_background()
        self.setup_ui()

    def add_main_background(self):
        """Thêm hình nền vào cửa sổ chính."""
        # Đường dẫn đến hình nền
        bg_image_path = Path.cwd() / "frontend" / "image" / "backgroundLoginRis.png" 

        # Tải ảnh bằng PIL
        image = Image.open(bg_image_path)
        self.bg_image = ImageTk.PhotoImage(image.resize((700, 550)))
        # Thêm ảnh vào Canvas
        self.canvas = Canvas(self.root, width=700, height=550)
        self.canvas.place(x=500, y=32)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)

    def setup_ui(self):
        """Tạo giao diện chính với các tab Đăng Nhập và Đăng Ký"""
        notebook_width = 500
        notebook_height = 550

        x_offset = 0
        y_offset = (550 - notebook_height) // 2

        self.notebook = ttk.Notebook(self.root, bootstyle="primary")
        self.notebook.place(x=x_offset, y=y_offset, width=notebook_width, height=notebook_height)

        self.create_login_tab()
        self.create_register_tab()

    def create_login_tab(self):
        """Tạo giao diện cho tab Đăng Nhập"""
        self.login_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.login_frame, text="Login")
        
        # Tiêu đề "Đăng Nhập"
        ttk.Label(
            self.login_frame,
            text="Login",
            bootstyle="light",
            font=("Arial", 24, "bold"),
            foreground="Black", 
        ).place(relx=0.5, y=40, anchor="center")

        ttk.Label(self.login_frame, text="User name:", bootstyle="secondary", font=("Arial", 12)).place(relx=0.5, y=100, anchor="center")
        self.login_username = ttk.Entry(self.login_frame, bootstyle="info", font=("Arial", 12))
        self.login_username.place(relx=0.5, y=140, width=400, anchor="center")

        ttk.Label(self.login_frame, text="Password:", bootstyle="secondary", font=("Arial", 12)).place(relx=0.5, y=180, anchor="center")
        self.login_password = ttk.Entry(self.login_frame, show="*", bootstyle="info", font=("Arial", 12))
        self.login_password.place(relx=0.5, y=220, width=400, anchor="center")

        ttk.Button(self.login_frame, text="Login", bootstyle="success outline", command=self.handle_login).place(relx=0.5, y=270, anchor="center")

    def create_register_tab(self):
        """Tạo giao diện cho tab Đăng Ký"""
        self.register_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.register_frame, text="Register")

        # Tiêu đề "Đăng Ký"
        ttk.Label(
            self.register_frame,
            text="Register",
            bootstyle="light",
            font=("Arial", 24, "bold"),
            foreground="black",
        ).place(relx=0.5, y=40, anchor="center")

        ttk.Label(self.register_frame, text="Phone number:", bootstyle="secondary", font=("Arial", 12)).place(relx=0.5, y=100, anchor="center")
        self.register_phone_number = ttk.Entry(self.register_frame, bootstyle="info", font=("Arial", 12))
        self.register_phone_number.place(relx=0.5, y=140, width=400, anchor="center")

        ttk.Label(self.register_frame, text="User name:", bootstyle="secondary", font=("Arial", 12)).place(relx=0.5, y=180, anchor="center")
        self.register_username = ttk.Entry(self.register_frame, bootstyle="info", font=("Arial", 12))
        self.register_username.place(relx=0.5, y=220, width=400, anchor="center")

        ttk.Label(self.register_frame, text="Password:", bootstyle="secondary", font=("Arial", 12)).place(relx=0.5, y=260, anchor="center")
        self.register_password = ttk.Entry(self.register_frame, show="*", bootstyle="info", font=("Arial", 12))
        self.register_password.place(relx=0.5, y=300, width=400, anchor="center")

        ttk.Label(self.register_frame, text="Confirm password:", bootstyle="secondary", font=("Arial", 12)).place(relx=0.5, y=340, anchor="center")
        self.register_confirm_password = ttk.Entry(self.register_frame, show="*", bootstyle="info", font=("Arial", 12))
        self.register_confirm_password.place(relx=0.5, y=380, width=400, anchor="center")

        ttk.Button(self.register_frame, text="Register", bootstyle="success outline", command=self.handle_register).place(relx=0.5, y=430, anchor="center")

    def add_background_to_tab(self, parent, image_path):
        """Chèn hình nền vào toàn bộ tab"""
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((700, 550), Image.Resampling.LANCZOS)  # Resize hình ảnh cho vừa với kích thước tab
        bg_photo = ImageTk.PhotoImage(bg_image)

        # Tạo Canvas để làm nền
        canvas = Canvas(parent, width=700, height=550)
        canvas.place(x=0, y=0)  # Đặt canvas ở góc trên trái của tab
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
        canvas.image = bg_photo  # Lưu tham chiếu để tránh bị xóa

    def handle_login(self):
        """Xử lý logic khi nhấn nút Đăng Nhập"""
        username = self.login_username.get()
        password = self.login_password.get()

        if not username or not password:
            messagebox.showwarning("Lỗi", "Vui lòng điền đầy đủ thông tin!")
        else:
            # Kiểm tra thông tin đăng nhập
            conn = sqlite3.connect("appOanTuTi_data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            user = cursor.fetchone()

            if user:
                messagebox.showinfo("Thông báo", f"Đăng nhập thành công!\nTài khoản: {username}")

                # Tạo cửa sổ HomePage mới
                self.root.withdraw()  # Ẩn cửa sổ đăng nhập
                home_root = tk.Toplevel(self.root)  # Tạo cửa sổ mới cho trang chủ
                app = HomePage(home_root)

            else:
                messagebox.showerror("Lỗi", "Tài khoản hoặc mật khẩu không đúng!")

            conn.close()

    def handle_register(self):
        """Xử lý logic khi nhấn nút Đăng Ký"""
        phone_number = self.register_phone_number.get()
        username = self.register_username.get()
        password = self.register_password.get()
        confirm_password = self.register_confirm_password.get()

        if not phone_number or not username or not password or not confirm_password:
            messagebox.showwarning("Lỗi", "Vui lòng điền đầy đủ thông tin!")
        elif password != confirm_password:
            messagebox.showerror("Lỗi", "Mật khẩu xác nhận không khớp!")
        else:
            # Kiểm tra nếu phone_number đã tồn tại trong cơ sở dữ liệu
            conn = sqlite3.connect("appOanTuTi_data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE phone_number = ?", (phone_number,))
            existing_user = cursor.fetchone()

            if existing_user:
                messagebox.showerror("Lỗi", "Số điện thoại đã được sử dụng!")
            else:
                # Thêm người dùng mới vào cơ sở dữ liệu
                cursor.execute("INSERT INTO users (phone_number, username, password) VALUES (?, ?, ?)", 
                            (phone_number, username, password))
                conn.commit()
                conn.close()

                messagebox.showinfo("Thông báo", f"Đăng ký thành công!\nTài khoản: {username}")



if __name__ == "__main__":
    app = ttk.Window("Oẳn Tù Tì - Đăng Nhập & Đăng Ký", themename="cosmo")
    LoginRegisterApp(app)
    app.mainloop()
