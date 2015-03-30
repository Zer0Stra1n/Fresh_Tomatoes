class Movie():

    #define the initialize function taking in the title, storyline, poster_image, and trailer
    def __init__(self, movie_title, movie_storyline, poster_image, trailer, imdb_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
        self.movie_rating = imdb_rating
