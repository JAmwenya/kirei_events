# lib/cli.py

from helpers import (
    exit_program,
    create_artist,
    list_artists,
    delete_artist,
    create_album,
    list_albums,
    delete_album
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_artist()
        elif choice == "2":
            list_artists()
        elif choice == "3":
            delete_artist()
        elif choice == "4":
            create_album()
        elif choice == "5":
            list_albums()
        elif choice == "6":
            delete_album()
        else:
            print("Invalid choice")

def menu():
    print("\nAlbum Management System")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a new artist")
    print("2. List all artists")
    print("3. Delete an artist")
    print("4. Create a new album")
    print("5. List all albums")
    print("6. Delete an album")

if __name__ == "__main__":
    main()
