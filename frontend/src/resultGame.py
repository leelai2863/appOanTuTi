import tkinter as tk
from tkinter import Toplevel, Button, Canvas
from PIL import Image, ImageTk
from pathlib import Path


class ResultWindow:
    def __init__(self, root, result_type, gif_path, next_callback):
        """
        Tạo cửa sổ hiển thị kết quả (thắng, thua, hòa).
        
        :param root: Cửa sổ gốc.
        :param result_type: Kiểu kết quả ("win", "lose", "draw").
        :param gif_path: Đường dẫn đến file GIF.
        :param next_callback: Hàm callback khi nhấn nút "Next".
        """
        self.root = root
        self.result_window = Toplevel(root)  # Tạo cửa sổ mới
        self.result_window.title(f"Kết quả: {result_type.upper()}")
        self.result_window.geometry("800x600")
        self.result_window.resizable(False, False)

        # Thêm ảnh GIF động
        self.frames = []
        self.current_frame = 0
        self.load_gif(gif_path)

        self.canvas = Canvas(self.result_window, width=800, height=500, highlightthickness=0)
        self.canvas.pack()
        self.update_gif()

        # Thêm nút Next
        next_button = Button(self.result_window, text="Next", font=("Arial", 16), command=self.handle_next)
        next_button.pack(pady=20)

        # Lưu callback cho nút Next
        self.next_callback = next_callback

    def load_gif(self, gif_path):
        """Load các khung hình từ file GIF."""
        gif = Image.open(gif_path)
        while True:
            try:
                resized_frame = gif.resize((800, 500), Image.Resampling.LANCZOS)
                frame = ImageTk.PhotoImage(resized_frame)
                self.frames.append(frame)
                gif.seek(len(self.frames))  # Chuyển sang khung hình tiếp theo
            except EOFError:
                break  # Kết thúc GIF

    def update_gif(self):
        """Cập nhật từng khung hình của GIF động."""
        if self.frames:
            frame = self.frames[self.current_frame]
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.canvas.create_image(0, 0, image=frame, anchor="nw")
            self.result_window.after(100, self.update_gif)  # Cập nhật mỗi 100ms

    def handle_next(self):
        """Xử lý khi nhấn nút Next."""
        self.result_window.destroy()  # Đóng cửa sổ kết quả
        if self.next_callback:
            self.next_callback()  # Gọi callback để tiếp tục trò chơi

if __name__ == "__main__":
    def next_round():
        print("Next round triggered!")

    app = tk.Tk()
    app.withdraw()  # Ẩn cửa sổ chính (nếu không cần)
    
    # Sử dụng Path để tạo đường dẫn đến file GIF
    # gif_path = Path.cwd() / "frontend" / "image" / "giphyWinner.webp"
    
    # ResultWindow(
    #     app, 
    #     result_type="win",  # hoặc "lose", "draw"
    #     gif_path=str(gif_path),  # Chuyển sang chuỗi nếu cần
    #     next_callback=next_round  # Hàm callback
    # )
    # app.mainloop()

    gif_path = Path.cwd() / "frontend" / "image" / "giphyLosing.webp"
    
    ResultWindow(
        app, 
        result_type="lose",  # hoặc "lose", "draw"
        gif_path=str(gif_path),  # Chuyển sang chuỗi nếu cần
        next_callback=next_round  # Hàm callback
    )
    app.mainloop()

    # gif_path = Path.cwd() / "frontend" / "image" / "giphyDrawing.webp"
    
    # ResultWindow(
    #     app, 
    #     result_type="draw",  # hoặc "lose", "draw"
    #     gif_path=str(gif_path),  # Chuyển sang chuỗi nếu cần
    #     next_callback=next_round  # Hàm callback
    # )
    # app.mainloop()