#Simple Rule Base System: Movie Mood Matcher

# If mood = "Happy" and genre = "Comedy" then movie = "Friends"
# If mood = "Happy" and genre = "Action" then movie = "Guardians of the Galaxy"
# If mood = "Sad" and genre = "Drama" then movie = "The Pursuit of Happyness"
# If mood = "Sad" and genre = "Romance" then movie = "Titanic"
# If mood = "Adventurous" and genre = "Action" then movie = "Avengers: Endgame"
# If mood = "Adventurous" and genre = "Fantasy" then movie = "Jumanji: Welcome to the Jungle"
# If mood = "Adventurous" and genre = "Sci-Fi" then movie = "Interstellar"
# If mood = "Romantic" and genre = "Romance" then movie = "The Notebook"
# If mood = "Romantic" and genre = "Comedy" then movie = "How I Met Your Mother"
# If mood = "Angry" and genre = "Mystery" then movie = "13 Reasons Why"
# If mood = "Eerie" and genre = "Horror" then movie = "The Watcher"
# Else then  "No recommendation found for your input."

from flask import Flask, render_template, request

app = Flask(__name__)

def recommend_movie(mood, genre):

    if mood == "Happy":
        if genre in "Comedy":
            return "Friends"
        elif genre == "Action":
            return "Guardians of the Galaxy"
        else:
            return "No Movie matches your input."
    elif mood == "Sad":
        if genre == "Drama":
            return "The Pursuit of Happyness"
        elif genre == "Romance":
            return "Titanic"
        else:
            return "No Movie matches your input."
    elif mood == "Adventurous":
        if genre == "Action":
            return "Avengers: Endgame"
        elif genre == "Fantasy":
            return "Jumanji: Welcome to the Jungle"
        elif genre == "Sci-Fi":
            return "Interstellar"
        else:
            return "No Movie matches your input."
    elif mood == "Romantic":
        if genre in ["Romance"]:
            return "The Notebook"
        elif genre == "Comedy":
            return "How I Met Your Mother"
        else:
            return "No Movie matches your input."
    elif mood == "Angry" and genre == "Mystery":
        return "13 Reasons Why"
    elif mood == "Eerie" and genre == "Horror":
        return "The Watcher"
    else:
        return "No Movie matches your input." 

@app.route("/", methods=["GET", "POST"])
def home():
    recommendation = None
    if request.method == "POST":
        mood = request.form.get("mood")
        genre = request.form.get("genre")

        mood = mood.strip().title()
        genre = genre.strip().title()

        # Only recommend if both inputs are provided
        if mood.strip() and genre.strip():
            recommendation = recommend_movie(mood, genre)

    return render_template("index.html", recommendation=recommendation)

if __name__ == "__main__":
    app.run(debug=True)
