import webbrowser

class Movie():
    """This provides movie information
       
       Attributes:
       class variables about the movie ratings

    """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
	"""
	    constructor of the movie instance 
	    with movie title, storyline, image, and youtube
	    returns nothing.
	"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
	"""
	    this method shows nothing but takes you 
	    to the url link which opens the youtube for trailer
	"""
        webbrowser.open(self.trailer_youtube_url)
