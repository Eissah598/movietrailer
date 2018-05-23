import webbrowser


# creating mymovie class
class MyMovie():
    # init function to initialize values
    def __init__(self, movie_title,
                 poster_image, trailer):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    # show trailer function to open webpage from webbrowser.open method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
