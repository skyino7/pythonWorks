import cmd


def main():

    booksList = []

    # infile = open("BooksList.txt", "r")
    # line = infile.readline()
    # while line:
    #     booksList.append(line.rstrip("\n").split(","))
    #     line = infile.readline()
    # infile.close()

    choice = 0
    while choice != 4:
        print("*** Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")
        print("4) Quit")
        choice = int(input())

        if choice == 1:
            print("Adding a book...")
            nBook = input("Enter the name of the book >>> ")
            nAuthor = input("Enter the name of the Author >>> ")
            nPages = input("Enter the number of pages >>> ")
            booksList.append([nBook, nAuthor, nPages])


if __name__ == "__main__":
    main()
