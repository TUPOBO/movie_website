
# render the movie webpage
import fresh_tomatoes
# Movie class that stores movies informations
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio",
                        "John A. Lasseter")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "James Francis Cameron")

hitch = media.Movie("Hitch",
                    "Dating coach Alex Hitchens mentors a bumbling client, Albert, who hopes to win the heart of the glamorous Allegra Cole",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Hitch_poster.JPG/220px-Hitch_poster.JPG",
                    "https://www.youtube.com/watch?v=dMaq_pfxs-0",
                    "Andy Tennant")

school_of_rock = media.Movie("School of Rock", "Teacher uses music to teach kids",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74",
                             "Richard Linklater")

ratatouille = media.Movie("Ratatouille", "A rat helps a boy cook",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                          "poster")
midnight_in_paris = media.Movie("Midnight in Paris", "A man travels to the past to meet his heroes",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY",
                                "Woody Allen")
hunger_games = media.Movie("Hunger Games", "People watch kids fight to the death",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8",
                           "Suzanne Collins")

inception = media.Movie("Inception",
                        "stealing valuable secrets from subconscious during the dream state.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0",
                        "Christopher Nolan")

interstellar = media.Movie("Interstellar",
                           "future of the earth where humanity is struggling to survive.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=M-xglYg-TTw",
                           "Christopher Nolan")


movies = [avatar, toy_story, hitch, school_of_rock, ratatouille, midnight_in_paris, hunger_games, inception,
          interstellar]

# use movies list render webpage
fresh_tomatoes.open_movies_page(movies)
