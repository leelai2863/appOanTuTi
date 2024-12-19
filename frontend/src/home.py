import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from tkinter import ttk
from PIL import Image, ImageTk  # Thư viện Pillow để xử lý ảnh động

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Trang Chủ")
        self.root.geometry("1200x550")
        
        # Tạo Style cho tiêu đề
        self.style = Style("cosmo")  # Chọn giao diện ttkbootstrap
        self.create_styles()

        # Thêm background ảnh động
        self.add_animated_background("D:\\appOanTuTi\\frontend\\image\\giphy.webp")

        # Tiêu đề trang chủ
        title_label = ttk.Label(
            self.root,
            text="Welcome to OanTuTi!",
            font=("Times New Roman", 30, "bold"),
            style="Title.TLabel"  # Áp dụng style tiêu đề
        )
        title_label.place(relx=0.5, y=50, anchor="center")

        # Nút Play Online
        self.play_online_button = ttk.Button(self.root, text="Play Online", style="Custom.TButton", width=20, command=self.play_online)
        self.play_online_button.place(relx=0.5, y=150, anchor="center")

        # Nút Play Bots
        self.play_bots_button = ttk.Button(self.root, text="Play Bots", style="Custom.TButton", width=20, command=self.play_bots)
        self.play_bots_button.place(relx=0.5, y=250, anchor="center")

        # Nút Đăng Xuất
        self.logout_button = ttk.Button(self.root, text="Exit", style="Custom.TButton", width=20, command=self.logout)
        self.logout_button.place(relx=0.5, y=350, anchor="center")
        
        # Gọi hàm hiệu ứng chuyển màu chữ
        self.animate_text_colors()

    def create_styles(self):
        """Tạo style cho các thành phần giao diện"""
        # Style tiêu đề
        self.style.configure(
            "Title.TLabel",
            foreground="black",  # Màu chữ tiêu đề
        )

        # Style cho các nút
        self.style.configure(
            "Custom.TButton",
            font=("Arial", 14),
            foreground="black",  # Màu chữ mặc định
            background="#FFFFFF"
        )

    def add_animated_background(self, gif_path, target_width=1200, target_height=550):
        """Thêm ảnh động làm background"""
        self.canvas = tk.Canvas(self.root, width=target_width, height=target_height, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        # Mở file GIF động
        self.frames = []  # Danh sách các khung hình của GIF
        self.current_frame = 0  # Khung hình hiện tại

        gif = Image.open(gif_path)
        original_width, original_height = gif.size
        
        try:
            while True:
                resized_frame = gif.copy().resize((target_width, target_height), resample=Image.Resampling.LANCZOS)
                frame = ImageTk.PhotoImage(resized_frame)
                self.frames.append(frame)
                
                gif.seek(gif.tell() + 1)

        except EOFError:
            pass  # Kết thúc GIF
        
        self.update_background()

    def update_background(self):
        """Cập nhật từng khung hình của ảnh GIF"""
        frame = self.frames[self.current_frame]
        self.current_frame = (self.current_frame + 1) % len(self.frames)  # Lặp lại GIF
        self.canvas.create_image(0, 0, anchor="nw", image=frame)
        self.root.after(100, self.update_background)  # Cập nhật mỗi 100ms (tùy tốc độ GIF)

    def animate_text_colors(self):
        """Hiệu ứng chuyển đổi màu chữ cho các nút"""
        colors = ["#FF5733", "#33FF57", "#3357FF", "#FFC300", "#FF33FF"]

        def change_color(style_name, index=0):
            self.style.configure(style_name, foreground=colors[index % len(colors)])  # Đổi màu chữ
            self.root.after(500, change_color, style_name, index + 1)  # Lặp lại sau 500ms

        # Thay đổi màu chữ của nút "Custom.TButton"
        change_color("Custom.TButton")

    def play_online(self):
        print("Playing Online...")

    def play_bots(self):
        print("Playing with Bots...")

    def logout(self):
        self.root.quit()

# Chạy giao diện
if __name__ == "__main__":
    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()
