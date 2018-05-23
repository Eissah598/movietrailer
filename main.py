import file1
import file2


# rabnebanadijodi title,poster image,urlid
rnbz = file1.MyMovie("Rab Ne Banadi Zodi",
                     "https://bit.ly/2kf6Xhk",
                     "eBi8syxPd14")
# raone title,poster image,urlid
rone = file1.MyMovie("Ra-One",
                     "https://bit.ly/2s6me7x",
                     "d9PlHc_qVKw")
# chennai express title,poster image,urlid
ce = file1.MyMovie("Chennai Express",
                   "https://bit.ly/2s6mh3d",
                   "rARol7Dk2zo")
# zero title,poster image,urlid
zero = file1.MyMovie("Zero",
                     "https://bit.ly/2klHOBL",
                     "RF7DhGIQE1k")
# mohabbatein title,poster image,urlid
mohabbatein = file1.MyMovie("Mohabbatein",
                            "https://bit.ly/2kfl9GS",
                            "OjlZFIY7VHU")
# raees title,poster image,urlid
raees = file1.MyMovie("Raees",
                      "https://bit.ly/2LlsgtO",
                      "J7_1MU3gDk0")

# in every part the Movie class in a1 file is called
movies = [rnbz, rone, ce, zero, mohabbatein, raees]
# the open_module function in a2 file is called
file2.open_module(movies)
