import fresh_tomatoes
import media

underworld5 = media.Movie("underworld_bloodwars",
                          "A story of werewolves and vampires",
                          "http://cdn1-www.comingsoon.net/assets/uploads/gallery/underworld-blood-wars/underworldbwposter.jpg",
                          "https://www.youtube.com/watch?v=rKHL5PyAPzs"
                          )

source_code = media.Movie("source code",
                          "time travel by programming",
                          "https://upload.wikimedia.org/wikipedia/en/e/e5/Source_Code_Poster.jpg",
                          "https://www.youtube.com/watch?v=DiBVUulE_wo"
                          )


Moana = media.Movie("Moana",
                    "A story of indian supernatural",
                    "https://lumiere-a.akamaihd.net/v1/images/open-uri20160812-3094-p8x4dd_05e53f81.jpeg?region=0%2C0%2C1536%2C664",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI"
                    )

walter_mitty = media.Movie("secret life of walter mitty",
                           "Daydreamer's unexpected short adventure for responsibility",
                           "http://lifeteen.com/wp-content/uploads/2013/12/2013-12_LT-WalterMitty1.jpg",
                           "https://www.youtube.com/watch?v=HddkucqSzSM"
                           )

fifty_first_date = media.Movie("50 first dates",
                            "How to get an Amnesia girl",
                            "http://cdn2-www.craveonline.com/assets/uploads/2014/02/50-First-Dates-10-Years-Later.jpg",
                            "https://www.youtube.com/watch?v=ErjP5xMTc8I"
                            )

edge_of_tomorrow = media.Movie("Edge of Tomorrow",
                               "time traveler winning a war against aliens",
                               "https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
                               "https://www.youtube.com/watch?v=yUmSVcttXnI"
                               )



movies = [underworld5, source_code, Moana, walter_mitty, fifty_first_date, edge_of_tomorrow]
fresh_tomatoes.open_movies_page(movies)

#print(Moana.storyline)
#toy_story.show_trailer()
