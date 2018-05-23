import media
import my_movies


''' movie title, posterlink, youtube url id
    is sent to the MyMovie class in 'media' file
'''

rnbz = media.MyMovie("Rab Ne Banadi Zodi",
                     "https://bit.ly/2kf6Xhk",
                     "eBi8syxPd14")
rone = media.MyMovie("Ra-One",
                     "https://bit.ly/2s6me7x",
                     "d9PlHc_qVKw")
ce = media.MyMovie("Chennai Express",
                   "https://bit.ly/2s6mh3d",
                   "rARol7Dk2zo")
zero = media.MyMovie("Zero",
                     "https://bit.ly/2klHOBL",
                     "RF7DhGIQE1k")
mohabbatein = media.MyMovie("Mohabbatein",
                            "https://bit.ly/2kfl9GS",
                            "OjlZFIY7VHU")
raees = media.MyMovie("Raees",
                      "https://bit.ly/2LlsgtO",
                      "J7_1MU3gDk0")

# in every part the Movie class in a1 file is called
movies = [rnbz, rone, ce, zero, mohabbatein, raees]
# the open_module function in a2 file is called
my_movies.open_module(movies)
