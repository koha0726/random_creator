"""
メインウィンドウを管理するモジュール
"""

import customtkinter as ctk
from logic.generator import generate_character


class MainWindow(ctk.CTk):
    """アプリケーションのメインウィンドウ"""

    def __init__(self) -> None:
        super().__init__()

        # -------------------------
        # ウィンドウ設定
        # -------------------------
        self.title("ランダム創作ネタ生成器")
        self.geometry("800x600")
        self.minsize(700, 500)

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # -------------------------
        # フレーム作成
        # -------------------------
        self.create_header()
        self.create_control()
        self.create_result()

    # ==================================================
    # Header
    # ==================================================

    def create_header(self) -> None:
        """タイトル部分を作成"""

        self.header_frame = ctk.CTkFrame(self)
        self.header_frame.pack(fill="x", padx=15, pady=(15, 10))

        title = ctk.CTkLabel(
            self.header_frame,
            text="ランダム創作ネタ生成器",
            font=("Yu Gothic UI", 24, "bold")
        )

        title.pack(pady=15)

    # ==================================================
    # Control
    # ==================================================

    def create_control(self) -> None:
        """操作部分を作成"""

        self.control_frame = ctk.CTkFrame(self)
        self.control_frame.pack(fill="x", padx=15, pady=10)

        # ----- タイトル -----

        label = ctk.CTkLabel(
            self.control_frame,
            text="生成対象"
        )

        label.grid(row=0, column=0, sticky="w", padx=20, pady=(15, 10))

        # ----- ラジオボタン -----

        self.mode = ctk.StringVar(value="character")

        character = ctk.CTkRadioButton(
            self.control_frame,
            text="キャラクター",
            variable=self.mode,
            value="character"
        )

        world = ctk.CTkRadioButton(
            self.control_frame,
            text="世界観（未実装）",
            variable=self.mode,
            value="world"
        )

        character.grid(row=1, column=0, sticky="w", padx=35)
        world.grid(row=2, column=0, sticky="w", padx=35)

        # ----- 生成ボタン -----

        generate_button = ctk.CTkButton(
            self.control_frame,
            text="生成",
            command=self.generate
        )

        generate_button.grid(row=3, column=0, pady=20)

    # ==================================================
    # Result
    # ==================================================

    def create_result(self) -> None:
        """結果表示エリア"""

        self.result_frame = ctk.CTkFrame(self)
        self.result_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(10, 15)
        )

        label = ctk.CTkLabel(
            self.result_frame,
            text="生成結果",
            font=("Yu Gothic UI", 18, "bold")
        )

        label.pack(pady=(15, 10))

        self.result_box = ctk.CTkTextbox(
            self.result_frame,
            width=500,
            height=300
        )

        self.result_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

    # ==================================================
    # イベント
    # ==================================================

    def generate(self) -> None:
        """生成ボタン押下時の処理"""

        result = generate_character()

        self.result_box.delete("1.0", "end")

        text = ""

        for key, value in result.items():
            text += f"{key}：{value}\n"

        self.result_box.insert("1.0", text)