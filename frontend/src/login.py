import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import Canvas, messagebox
from PIL import Image, ImageTk


class LoginRegisterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Oẳn Tù Tì - Đăng Nhập & Đăng Ký")
        self.root.geometry("700x550")
        self.root.resizable(False, False)

        self.setup_ui()

    def setup_ui(self):
        """Tạo giao diện chính với các tab Đăng Nhập và Đăng Ký"""
        self.notebook = ttk.Notebook(self.root, bootstyle="primary")
        self.notebook.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_login_tab()

        self.create_register_tab()

    def create_login_tab(self):
        """Tạo giao diện cho tab Đăng Nhập"""
        self.login_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.login_frame, text="Đăng Nhập")

        # Chèn hình nền vào tab Đăng Nhập
        bg_image_path = "D:\\python_learning\\appOanTuTi\\frontend\\image\\backgroundLoginRis.png"
        self.add_background_to_tab(self.login_frame, bg_image_path)

        # Tiêu đề "Đăng Nhập"
        ttk.Label(
            self.login_frame,
            text="Đăng Nhập",
            bootstyle="light",
            font=("Arial", 24, "bold"),
            foreground="Black", 
        ).place(relx=0.5, y=40, anchor="center")

        ttk.Label(self.login_frame, text="Tài khoản:", bootstyle="secondary", font=("Arial", 12)).place(relx=0.5, y=100, anchor="center")
        self.login_username = ttk.Entry(self.login_frame, bootstyle="info", font=("Arial", 12))
        self.login_username.place(relx=0.5, y=140, width=400, anchor="center")

        ttk.Label(self.login_frame, text="Mật khẩu:", bootstyle="secondary", font=("Arial", 12)).place(relx=0.5, y=180, anchor="center")
        self.login_password = ttk.Entry(self.login_frame, show="*", bootstyle="info", font=("Arial", 12))
        self.login_password.place(relx=0.5, y=220, width=400, anchor="center")

        ttk.Button(self.login_frame, text="Đăng Nhập", bootstyle="success outline", command=self.handle_login).place(relx=0.5, y=270, anchor="center")

    def create_register_tab(self):
        """Tạo giao diện cho tab Đăng Ký"""
        self.register_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.register_frame, text="Đăng Ký")

        # Chèn hình nền vào tab Đăng Ký
        bg_image_path = "D:\\python_learning\\appOanTuTi\\frontend\\image\\backgroundLoginRis.png"
        self.add_background_to_tab(self.register_frame, bg_image_path)

        # Tiêu đề "Đăng Ký"
        ttk.Label(
            self.register_frame,
            text="Đăng Ký",
            bootstyle="light",
            font=("Arial", 24, "bold"),
            foreground="black",
        ).place(relx=0.5, y=40, anchor="center")

        ttk.Label(self.register_frame, text="Tài khoản:", bootstyle="secondary", font=("Arial", 12)).place(relx=0.5, y=100, anchor="center")
        self.register_username = ttk.Entry(self.register_frame, bootstyle="info", font=("Arial", 12))
        self.register_username.place(relx=0.5, y=140, width=400, anchor="center")

        ttk.Label(self.register_frame, text="Mật khẩu:", bootstyle="secondary", font=("Arial", 12)).place(relx=0.5, y=180, anchor="center")
        self.register_password = ttk.Entry(self.register_frame, show="*", bootstyle="info", font=("Arial", 12))
        self.register_password.place(relx=0.5, y=220, width=400, anchor="center")

        ttk.Label(self.register_frame, text="Xác nhận mật khẩu:", bootstyle="secondary", font=("Arial", 12)).place(relx=0.5, y=260, anchor="center")
        self.register_confirm_password = ttk.Entry(self.register_frame, show="*", bootstyle="info", font=("Arial", 12))
        self.register_confirm_password.place(relx=0.5, y=300, width=400, anchor="center")

        ttk.Button(self.register_frame, text="Đăng Ký", bootstyle="success outline", command=self.handle_register).place(relx=0.5, y=350, anchor="center")

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
            messagebox.showinfo("Thông báo", f"Đăng nhập thành công!\nTài khoản: {username}")

    def handle_register(self):
        """Xử lý logic khi nhấn nút Đăng Ký"""
        username = self.register_username.get()
        password = self.register_password.get()
        confirm_password = self.register_confirm_password.get()

        if not username or not password or not confirm_password:
            messagebox.showwarning("Lỗi", "Vui lòng điền đầy đủ thông tin!")
        elif password != confirm_password:
            messagebox.showerror("Lỗi", "Mật khẩu xác nhận không khớp!")
        else:
            messagebox.showinfo("Thông báo", f"Đăng ký thành công!\nTài khoản: {username}")


if __name__ == "__main__":
    app = ttk.Window("Oẳn Tù Tì - Đăng Nhập & Đăng Ký", themename="cosmo")
    LoginRegisterApp(app)
    app.mainloop()
