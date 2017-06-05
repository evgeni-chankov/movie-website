import webbrowser

class Movie():
    """ This class provides an opportunity to store movies information """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,director,main_star,metascore,more_info):
        self.title                  = movie_title
        self.storyline              = movie_storyline
        self.poster_image_url       = poster_image
        self.trailer_youtube_url    = trailer_youtube
        self.director               = director
        self.main_star              = main_star
        self.metascore              = metascore
        self.more_info              = more_info

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
'''
class Show(Movie):
    """ Inherits from the Movie class and allows displaying additional information for shows """
'''


class Show():
    """ This class provides information for displaying shows """
    def __init__(self,show_title,show_storyline,show_poster,trailer_youtube,director,main_star,metascore,more_info,number_seasons,starting_year,ending_year):
        self.title                  = show_title
        self.storyline              = show_storyline
        self.poster_image_url       = show_poster
        self.trailer_youtube_url    = trailer_youtube
        self.director               = director
        self.main_star              = main_star
        self.metascore              = metascore
        self.more_info              = more_info
        self.number_seasons         = number_seasons
        self.starting_year          = starting_year
        self.ending_year            = ending_year

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
