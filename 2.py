import sqlite3

with open("stephen_king_adaptations.txt", "r") as file:
    stephen_king_adaptations_list = file.readlines()

conn = sqlite3.connect("stephen_king_adaptations.db")
cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE stephen_kind_adaptations_table (movieID TEXT, movieName TEXT, movieYear INT, imdbRating REAL)")

for line in stephen_king_adaptations_list:
    data = line.strip().split(",")
    cursor.execute("INSERT INTO stephen_kind_adaptations_table VALUES (?, ?, ?, ?)",
                   (data[0], data[1], int(data[2]), float(data[3])))

conn.commit()

while True:
    print("\nEnter the search parameter:")
    print("1. Movie name")
    print("2. Movie year")
    print("3. Movie rating")
    print("4. STOP")

    option = int(input("Enter the option number: "))

    if option == 1:  # Search by movie name
        movie_name = input("Enter the movie name: ")
        cursor.execute("SELECT * FROM stephen_kind_adaptations_table WHERE movieName LIKE ?", (f"%{movie_name}%",))
        movies = cursor.fetchall()

        if movies:
            print("\nMovie Details:")
            for movie in movies:
                print(f"Name: {movie[1]}, Year: {movie[2]}, Rating: {movie[3]}")
        else:
            print("No such movie exists in our database")

    elif option == 2:  # Search by movie year
        movie_year = int(input("Enter the year: "))
        cursor.execute("SELECT * FROM stephen_kind_adaptations_table WHERE movieYear = ?", (movie_year,))
        movies = cursor.fetchall()

        if movies:
            print("\nMovie Details:")
            for movie in movies:
                print(f"Name: {movie[1]}, Year: {movie[2]}, Rating: {movie[3]}")
        else:
            print("No movies were found for that year in our database.")

    elif option == 3:  # Search by movie rating
        rating_threshold = float(input("Enter the rating threshold: "))
        cursor.execute("SELECT * FROM stephen_kind_adaptations_table WHERE imdbRating >= ?", (rating_threshold,))
        movies = cursor.fetchall()

        if movies:
            print("\nMovie Details:")
            for movie in movies:
                print(f"Name: {movie[1]}, Year: {movie[2]}, Rating: {movie[3]}")
        else:
            print("No movies at or above that rating were found in the database.")

    elif option == 4:  # Stop option
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please enter a valid option number.")
