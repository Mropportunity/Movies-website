import fresh_tomatoes
import media
#my movies with all variables
How_High = media.Movie("How High",
                      "two regular guys who smoke something magical,"
                       "ace their college entrance exams and wind up at Harvard.",
                      "https://i.jeded.com/i/how-high.26187.jpg",
                      "https://www.youtube.com/watch?v=cvQFpF7N-DA")

#print (How_High.storyline)

Half_Baked = media.Movie("Half Baked",
                         "The story of three not so bright men who come up with a series"
                         "of crazy schemes to get a friend out of jail.",
                         "http://mtv.mtvnimages.com/shared/media/images/acovers/standard/dra900/a947/a94730mhefu.jpg",
                         "https://www.youtube.com/watch?v=JgkE3xoSHLU")
#print (Half_Baked.storyline)
#Half_Baked.show_trailer()
#How_High.show_trailer()

The_night_before = media.Movie("The Night Before",
                               "Lifelong buddies celebrate christmas eve, but now the tradition"
                               "is coming to an end,so they make it memorable",
                               "http://www.trespassmag.com/wp-content/uploads/2015/12/thenightbefore-poster.jpg",
                               "https://www.youtube.com/watch?v=kOBdxkhJvHQ")

Coach_Carter = media.Movie("Coach Carter",
                           "inspiring true story of controversial high school basketball coach"
                           "to teach his players the importance of education.",
                           "https://upload.wikimedia.org/wikipedia/en/c/c3/Coach_Carter_poster.JPG",
                           "https://www.youtube.com/watch?v=znyAnWUYf2g")

White_Chicks = media.Movie("White Chicks",
                          "Two fbi agents accidentally foiled a drug bust and are forced to escort"
                           "a pair of socialites to the Hamptons",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY3OTg2OTM3OV5BMl5"
                           "BanBnXkFtZTYwNzY5OTA3._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                          "https://www.youtube.com/watch?v=xebjMIYduxQ")

Peeples = media.Movie("Peeples",
                      "After a year of living with girlfriend Grace, Wade Walker is eager to propose"
                      "to her, but she's still reluctant to introduce him to her snobbish family.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQwODU0MDM4Ml5BMl5BanBnX"
                      "kFtZTcwMTA5MDkzOQ@@._V1_UY1200_CR82,0,630,1200_AL_.jpg",
                      "https://www.youtube.com/watch?v=_vv3TRQMtgY")

#movies array
movies = {How_High, Half_Baked,The_night_before,Coach_Carter,White_Chicks,Peeples}
fresh_tomatoes.open_movies_page(movies)
