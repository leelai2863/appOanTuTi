import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Trang Chủ")
        self.root.geometry("1200x550")

        # Tiêu đề trang chủ
        ttk.Label(self.root, text="Welcome to OanTuTi!", font=("Arial", 24, "bold")).pack(pady=20)

        # Nút Play Online
        ttk.Button(self.root, text="Play Online", bootstyle="primary", width=20, command=self.play_online).pack(pady=20)

        # Nút Play Bots
        ttk.Button(self.root, text="Play Bots", bootstyle="info", width=20, command=self.play_bots).pack(pady=20)

        # Nút Đăng Xuất
        ttk.Button(self.root, text="Đăng Xuất", bootstyle="danger", width=20, command=self.logout).pack(pady=20)

    def play_online(self):
        """Chức năng Play Online"""
        print("Chơi Online được chọn")

    def play_bots(self):
        """Chức năng Play Bots"""
        print("Chơi với Bots được chọn")

    def logout(self):
        """Đăng xuất và quay lại trang đăng nhập"""
        self.root.quit()  # Đóng cửa sổ trang chủ
        self.root.destroy()  # Đảm bảo hoàn toàn thoát khỏi cửa sổ trang chủ

# if __name__ == "__main__":
#     root = ttk.Window("Home", themename="cosmo")
#     HomePage(root)
#     root.mainloop()
