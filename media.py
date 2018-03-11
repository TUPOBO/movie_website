

import webbrowser

""" This class stores movies informations"""


class Movie():
      """This function needs arguments: movie_title, movie_storyline, poster_image, trailer_youtube, movie_director"""
      def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_director):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_url = trailer_youtube
        self.movie_director = movie_director

      def show_trailer(self):
        webbrowser.open(self.trailer_url)
