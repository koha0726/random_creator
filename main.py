"""
アプリケーションの起動を担当するファイル
"""

from ui.main_window import MainWindow


def main() -> None:
    """アプリケーションを起動する。"""
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()