import media 
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life", 
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet", 
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

hitch = media.Movie("Hitch", 
                    "Dating coach Alex Hitchens mentors a bumbling client, Albert, who hopes to win the heart of the glamorous Allegra Cole",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Hitch_poster.JPG/220px-Hitch_poster.JPG",
                    "https://www.youtube.com/watch?v=dMaq_pfxs-0")

school_of_rock = media.Movie("School of Rock", "Teacher uses music to teach kids", 
               "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
               "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "A rat helps a boy cook", 
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris", "A man travels to the past to meet his heroes", 
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")
hunger_games = media.Movie("Hunger Games", "People watch kids fight to the death", 
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", 
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

inception= media.Movie("Inception",
                            "stealing valuable secrets from subconscious during the dream state.",
                            "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                            "https://www.youtube.com/watch?v=YoHD9XEInc0")

interstellar= media.Movie("Interstellar",
                            "future of the earth where humanity is struggling to survive.",
                            "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                            "https://www.youtube.com/watch?v=M-xglYg-TTw")

chappie= media.Movie("Chappie",
                      "Robot, mimics a human mind to the point of feeling emotions and having opinions",
                      "https://upload.wikimedia.org/wikipedia/en/7/71/Chappie_poster.jpg",
                      "https://www.youtube.com/watch?v=l6bmTNadhJE")

now_you_see_me= media.Movie("Now you see Me",
                             "Story of 4 magicians, who steels money",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Now_You_See_Me_Poster.jpg",
                             "https://www.youtube.com/watch?v=4OtM9j2lcUA")

focus= media.Movie("Focus",
                    "never to lose focus when faced with unexpected situations",
                    "https://upload.wikimedia.org/wikipedia/en/b/bf/2015_Focus_film_poster.png",
                    "https://www.youtube.com/watch?v=MxCRgtdAuBo")

the_pursuit_of_happyness= media.Movie("The Pursuit of Happyness",
                                      "salesman invests his entire life savings in portable bone density scanners",
                                      "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
                                      "https://www.youtube.com/watch?v=89Kq8SDyvfg")
baahubali_2_the_conclusion= media.Movie("Baahubali 2 - The Conclusion",
                                        "Empire of Mahishmati, Sivagami, emerges injured from a cave adjoining waterfall",
                                        "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
                                        "https://www.youtube.com/watch?v=G62HrubdD6o")
movies = [avatar, toy_story, hitch, school_of_rock, ratatouille, midnight_in_paris, hunger_games, inception, interstellar, chappie, now_you_see_me, focus, the_pursuit_of_happyness, baahubali_2_the_conclusion]
fresh_tomatoes.open_movies_page(movies)

