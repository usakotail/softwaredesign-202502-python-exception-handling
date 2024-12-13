def open_not_exist_file() -> None:
    # 存在しないファイルを開こうとする
    with open("config.txt", "r") as f:
        config = f.read()
        print(f"configファイルを読み込みました。{config=}")
