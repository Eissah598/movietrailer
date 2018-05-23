import webbrowser


class MyMovie():

    def __init__(self, movie_title,
                 poster_image, trailer):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
