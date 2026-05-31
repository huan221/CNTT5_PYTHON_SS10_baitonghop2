playlist = []


def show_menu():
    print("\n===== PLAYLIST MENU =====")
    print("1. Thêm bài hát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát")
    print("4. Sắp xếp / Trích xuất")
    print("5. Thoát")

while True:
    show_menu()

    try:
        choice = int(input("Chọn chức năng: "))
    except:
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên!")
        continue

    if choice == 1:
        song_name = input("Nhập tên bài hát: ")

        print("1. Thêm vào cuối")
        print("2. Chèn vào vị trí")

        try:
            sub_choice = int(input("Chọn: "))
        except:
            print("Lựa chọn không hợp lệ!")
            continue

        if sub_choice == 1:
            playlist.append(song_name)
            print(f"Đã thêm '{song_name}'. Tổng bài hát: {len(playlist)}")

        elif sub_choice == 2:
            try:
                index = int(input("Nhập vị trí (bắt đầu từ 1): ")) - 1
                if index < 0 or index > len(playlist):
                    print("Vị trí không hợp lệ.")
                else:
                    playlist.insert(index, song_name)
                    print(f"Đã chèn '{song_name}'. Tổng bài hát: {len(playlist)}")
            except:
                print("Vui lòng nhập số nguyên!")

        else:
            print("Lựa chọn không hợp lệ!")
                         
    elif choice == 2:
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
        else:
            print("\n--- DANH SÁCH PHÁT ---")
            for i, song in enumerate(playlist, start=1):
                print(f"{i}. {song}")

    elif choice == 3:
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
            continue

        print("1. Xóa theo tên")
        print("2. Xóa theo vị trí")

        try:
            sub_choice = int(input("Chọn: "))
        except:
            print("Lựa chọn không hợp lệ!")
            continue

        if sub_choice == 1:
            song_name = input("Nhập tên bài hát cần xóa: ")
            if song_name in playlist:
                playlist.remove(song_name)
                print(f"Đã xóa '{song_name}' khỏi danh sách.")
            else:
                print("Không tìm thấy bài hát trong danh sách phát.")

        elif sub_choice == 2:
            try:
                index = int(input("Nhập vị trí (bắt đầu từ 1): ")) - 1
                if index < 0 or index >= len(playlist):
                    print("Vị trí không hợp lệ.")
                else:
                    removed_song = playlist.pop(index)
                    print(f"Đã xóa '{removed_song}' khỏi danh sách.")
            except:
                print("Vui lòng nhập số nguyên!")

        else:
            print("Lựa chọn không hợp lệ!")


    elif choice == 4:
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
            continue

        print("1. Sắp xếp theo bảng chữ cái")
        print("2. Xem 3 bài đầu tiên")

        try:
            sub_choice = int(input("Chọn: "))
        except:
            print("Lựa chọn không hợp lệ!")
            continue

        if sub_choice == 1:
            playlist.sort()
            print("Danh sách đã được sắp xếp:")
            for i, song in enumerate(playlist, start=1):
                print(f"{i}. {song}")

        elif sub_choice == 2:
            print("3 bài hát đầu tiên:")
            for song in playlist[:3]:
                print(song)

        else:
            print("Lựa chọn không hợp lệ!")

    elif choice == 5:
        print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ!")