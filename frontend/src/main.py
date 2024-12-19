import ttkbootstrap as ttk
from login import LoginRegisterApp
from home import HomePage

def start_login_page():
    login_root = ttk.Window("Oẳn Tù Tì - Đăng Nhập & Đăng Ký", themename="cosmo")
    LoginRegisterApp(login_root)
    login_root.mainloop()

def start_home_page():
    root = ttk.Window("Trang Chủ", themename="cosmo")
    HomePage(root)
    root.mainloop()

if __name__ == "__main__":
    start_login_page()
