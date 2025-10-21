import os


class Book:
    def __init__(self, title, author, year, genre, price, availability):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.price = price
        self.availability = availability
    
    def Num_Books(self):
        with open("books.txt", "r") as file:
            lines = file.readlines()
            return len(lines)

    def Num_Available(self):
        with open("books.txt", "r") as file: 
            count = 0
            for line in file:
                parts = line.strip().split()
                if parts[-1] == 'Yes':  
                    count += 1
            return count   

    def Update_Availability(self, new_availability):
        self.availability = new_availability
        
        with open("books.txt", "r") as file:
            lines = file.readlines()
        
        with open("books.txt", "w") as file:
            for line in lines:
                attributes = line.strip().split(' ')
                title = attributes[0]
                if title == self.title:
                    attributes[-1] = new_availability
                    line = ' '.join(attributes) + '\n'
                file.write(line)

    def Add_Remove_Book(self, action):
        if action == 'add':
            with open("books.txt", "a") as file:
                file.write(f"{self.title} {self.author} {self.year} {self.genre} {self.price} {self.availability}\n")
        elif action == 'remove':
            with open("books.txt", "r") as file:
                lines = file.readlines()
            with open("books.txt", "w") as file:
                for line in lines:
                    attributes = line.strip().split(' ')
                    title = attributes[0]
                    if title != self.title:
                        file.write(line)

    def Book_Info(self, attribute, info):
        with open("books.txt", "r") as file:
            lines = file.readlines()

        with open("books.txt", "w") as file:
            for line in lines:
                parts = line.strip().split()
                if parts and parts[0] == self.title:
                    if attribute == "title":
                        parts[0] = str(info)
                    elif attribute == "author":
                        parts[1] = str(info)
                    elif attribute == "year":
                        parts[2] = str(info)
                    elif attribute == "genre":
                        parts[3] = str(info)
                    elif attribute == "price":
                        parts[-2] = str(info)
                    elif attribute == "availability":
                        parts[-1] = str(info)
                    line = " ".join(parts) + "\n"
                file.write(line)

        

def instansiate():
    objects = []
    with open("books.txt", "r") as file:
        lines = file.readlines()

        for book in lines:
            attributes = book.strip().split(' ')
            title = attributes[0]
            author = attributes[1]
            year = attributes[2]
            genre = attributes[3]
            price = float(attributes[-2])
            availability = attributes[-1]

            if genre == 'crime':
                victim = attributes[4] if len(attributes) > 6 else ""
                killer = attributes[5] if len(attributes) > 6 else ""
                obj = Crime_Book(title, author, year, genre, victim, killer, price, availability)
            elif genre == 'fantasy':
                fantasy_attributes = attributes[4:-2]
                world = fantasy_attributes[0] if len(fantasy_attributes) >= 1 else "" 
                time = fantasy_attributes[1] if len(fantasy_attributes) >= 2 else ""
                character = fantasy_attributes[2] if len(fantasy_attributes) >= 3 else ""
                obj = Fantasy_Book(title, author, year, genre, world, time, character, price, availability)
            else:
                obj = Book(title, author, year, genre, price, availability)
            objects.append(obj)
            


def Edit_Book(title, **updates):
    with open("books.txt", "r") as file:
        lines = file.readlines()

    with open("books.txt", "w") as file:
        for line in lines:
            parts = line.strip().split(' ')
            if parts[0] == title:
                for key, value in updates.items():
                    k = key.lower()
                    if k == "title":
                        parts[0] = str(value)
                    elif k == "author":
                        parts[1] = str(value)
                    elif k == "year":
                        parts[2] = str(value)
                    elif k == "genre":
                        parts[3] = str(value)
                    elif k == "victim" and len(parts) > 4:
                        parts[4] = str(value)
                    elif k == "killer" and len(parts) > 5:
                        parts[5] = str(value)
                    elif k == "world" and "fantasy" in parts[3]:
                        if len(parts) > 4: parts[4] = str(value)
                        else: parts.insert(4, str(value))
                    elif k == "time" and "fantasy" in parts[3]:
                        if len(parts) > 5: parts[5] = str(value)
                        else: parts.insert(5, str(value))
                    elif k == "character" and "fantasy" in parts[3]:
                        if len(parts) > 6: parts[6] = str(value)
                        else: parts.insert(6, str(value))
                    elif k == "price":
                        parts[-2] = str(value)
                    elif k == "available":
                        parts[-1] = str(value)

                line = " ".join(parts) + "\n"
            file.write(line)


def Print_Fantasy(author):
    with open("books.txt", "r") as file:
        lines = file.readlines()
        for book in lines:
            parts = book.strip().split(' ')
            if parts[3] == 'fantasy' and parts[1] == author:
                print(book)


def print_Crime(year):
    with open("books.txt", "r") as file:
        lines = file.readlines()
        for book in lines:
            parts = book.strip().split(' ')        
            if len(parts) > 3 and parts[3] == 'crime': 
                try:                                   
                    if int(parts[2]) < int(year):      
                        print(book)                    
                except ValueError:
                    pass


def incoming_profits():
    with open("books.txt", "r") as file:
        lines = file.readlines()
        total = 0.0
        for book in lines:
            parts = book.strip().split(' ')
            if parts[-1].lower() == 'no':             
                total += float(parts[-2])
        return total


def organize():
    folder = "Organized-Library/fantasy"
    os.makedirs(folder, exist_ok=True) 

    with open("books.txt", "r") as file:
        lines = file.readlines()
        for book in lines:
            parts = book.strip().split(' ')
            if len(parts) >= 4 and parts[3] == 'fantasy': 
                with open(f"{folder}/{parts[0]}.txt", "w") as f:
                    f.write(book)
    
    folder = "Organized-Library/crime"
    os.makedirs(folder, exist_ok=True) 

    with open("books.txt", "r") as file:
        lines = file.readlines()
        for book in lines:
            parts = book.strip().split(' ')
            if len(parts) >= 4 and parts[3] == 'crime':
                with open(f"{folder}/{parts[0]}.txt", "w") as f:
                    f.write(book)
    
    folder = "Organized-Library/history"
    os.makedirs(folder, exist_ok=True) 

    with open("books.txt", "r") as file:
        lines = file.readlines()
        for book in lines:
            parts = book.strip().split(' ')
            if len(parts) >= 4 and parts[3] == 'history':
                with open(f"{folder}/{parts[0]}.txt", "w") as f:
                    f.write(book)
    
    folder = "Organized-Library/science"
    os.makedirs(folder, exist_ok=True)

    with open("books.txt", "r") as file:
        lines = file.readlines()
        for book in lines:
            parts = book.strip().split(' ')
            if len(parts) >= 4 and parts[3] == 'science':
                with open(f"{folder}/{parts[0]}.txt", "w") as f:
                    f.write(book)

    folder = "Organized-Library/romantic"
    os.makedirs(folder, exist_ok=True)

    with open("books.txt", "r") as file:
        lines = file.readlines()
        for book in lines:
            parts = book.strip().split(' ')
            if len(parts) >= 4 and parts[3] == 'romantic':
                with open(f"{folder}/{parts[0]}.txt", "w") as f:
                    f.write(book)

    folder = "Organized-Library/math"
    os.makedirs(folder, exist_ok=True)

    with open("books.txt", "r") as file:
        lines = file.readlines()
        for book in lines:
            parts = book.strip().split(' ')
            if len(parts) >= 4 and parts[3] == 'math':
                with open(f"{folder}/{parts[0]}.txt", "w") as f:
                    f.write(book)




class Crime_Book(Book):
    def __init__(self, title, author, year, genre, victim, killer, price, availability):
        super().__init__(title, author, year, genre, price, availability)
        self.victim = victim
        self.killer = killer


class Fantasy_Book(Book):
    def __init__(self, title, author, year, genre, world, time, character, price, availability):
        super().__init__(title, author, year, genre, price, availability)
        self.world = world
        self.time = time
        self.character = character



def main():
    library = instansiate()

    print("Total:", library[0].Num_Books())
    print("Available:", library[0].Num_Available())

    test_title = 'Remy_Easton'


    library[0].title = test_title
    library[0].Update_Availability("no")
    library[0].Update_Availability("yes")

    Edit_Book(test_title, price="49.99", author="Updated_Author", available="no")

    Print_Fantasy("Updated_Author")

    print_Crime(2000)

    print(incoming_profits())

    organize()


    
if __name__ == "__main__":
    main()
