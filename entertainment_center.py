import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        """A cowboy doll is profoundly threatened and jealous when a new 
                        spaceman figure supplants him as top toy in a boy's room.""",
                        "https://mydailyboost.files.wordpress.com/2012/06/toystory.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "John Lasseter",
                        "Tom Hanks, Tim Allen",
                        95,
                        "http://www.imdb.com/title/tt0114709/?ref_=nv_sr_1")

avatar = media.Movie("Avatar",
                     """A paraplegic marine dispatched to the moon Pandora on a unique 
                     mission becomes torn between following his orders and protecting 
                     the world he feels is his home.""",
                     "https://www.cinematerial.com/media/posters/md/sw/sw4mfbcw.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "James Cameron",
                     "Sam Worthington, Zoe Saldana, Sigourney Weaver",
                     83,
                     "http://www.imdb.com/title/tt0499549/?ref_=nv_sr_1")


fight_club = media.Movie("Fight Club",
                         """An insomniac office worker, looking for a way to change his life, 
                         crosses paths with a devil-may-care soap maker, forming an underground 
                         fight club that evolves into something much, much more.""",
                         "http://orig13.deviantart.net/a237/f/2015/251/a/0/fight_club_32_pom_by_p_lukaszewski-d98v3f3.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                         "David Fincher",
                         "Brad Pitt, Edward Norton, Helena Bonham Carter",
                         66,
                         "http://www.imdb.com/title/tt0137523/?ref_=nv_sr_1")


heat = media.Movie("Heat",
                    """A group of professional bank robbers start to feel the heat from 
                    police when they unknowingly leave a clue at their latest heist""",
                    "http://www.impawards.com/1995/posters/heat.jpg",
                    "https://www.youtube.com/watch?v=0xbBLJ1WGwQ",
                    "Michael Mann",
                    "Robert de Niro, Al Pacino, Val Kilmer",
                    76,
                    "http://www.imdb.com/title/tt0113277/?ref_=fn_al_tt_1")


casino = media.Movie("Casino",
                    """Greed, deception, money, power, and murder occur between two best 
                    friends: a mafia underboss and a casino owner""",
                    "http://www.impawards.com/1995/posters/casino_ver1.jpg",
                    "https://www.youtube.com/watch?v=EJXDMwGWhoA",
                    "Martin Scorsese",
                    "Robert de Niro, Joe Pesci",
                    73,
                    "http://www.imdb.com/title/tt0112641/?ref_=nv_sr_2")


scarface = media.Movie("Scarface",
                    """In Miami in 1980, a determined Cuban immigrant takes over a drug 
                    cartel and succumbs to greed.""",
                    "http://www.impawards.com/1983/posters/scarface_ver2.jpg",
                    "https://www.youtube.com/watch?v=7pQQHnqBa2E",
                    "Brian de Palma",
                    "Al Pacino",
                    65,
                    "http://www.imdb.com/title/tt0086250/?ref_=nv_sr_1")

goodfellas = media.Movie("Goodfellas",
                    """The story of Henry Hill and his life through the teen years into 
                    the years of mafia, covering his relationship with wife Karen Hill and his Mob partners""",
                    "http://www.impawards.com/1990/posters/goodfellas.jpg",
                    "https://www.youtube.com/watch?v=qo5jJpHtI1Y",
                    "Martin Scorcese",
                    "Robert de Niro, Ray Liotta, Joe Pesci",
                    89,
                    "http://www.imdb.com/title/tt0099685/?ref_=nv_sr_1")

dexter = media.Show("Dexter",
                    """Dexter Morgan is a Forensics Expert, but that's what he seems to be, as that's not what he really is. 
                    Dexter is a serial killer that hunts the bad.""",
                    "https://secureimg2.allposters.com/6/LRG/62/6228/XH93100Z.jpg",
                    "https://www.youtube.com/watch?v=YQeUmSD1c3g",
                    "James Manos Jr.",
                    "Michael C. Hall, Jennifer Carpenter",
                    96,
                    "http://www.imdb.com/title/tt0773262/?ref_=fn_al_tt_1",
                    8,
                    "2006",
                    "2013")

game_thrones = media.Show("Game of Thrones",
                    """Nine noble families fight for control over the mythical lands of Westeros, 
                    while a forgotten race returns after being dormant for thousands of years.""",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE3NTQ1NDg1Ml5BMl5BanBnXkFtZTgwNzY2NDA0MjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=gcTkNV5Vg1E",
                    "David Benioff",
                    "Emilia Clarke, Peter Dinklage",
                    100,
                    "http://www.imdb.com/title/tt0944947/?ref_=nv_sr_1",
                    8,
                    "2011",
                    "-")

westworld = media.Show("Westworld",
                    """Set at the intersection of the near future and the reimagined past, 
                    explore a world in which every human appetite, no matter how noble or depraved, 
                    can be indulged without consequence.""",
                    "https://i.redd.it/w9xwv38tnyix.jpg",
                    "https://www.youtube.com/watch?v=0zZcBv0gPK0",
                    "Tammi Sutton",
                    "Ed Harris, Evan Rachel Wood, Jeffrey Wright",
                    90,
                    "http://www.imdb.com/title/tt0475784/?ref_=nv_sr_1",
                    1,
                    "2016",
                    "-")

mr_robot = media.Show("Mr.Robot",
                    """Follows Elliot, a young programmer working as a cyber-security engineer by day, 
                    and a vigilante hacker by night.""",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYzMDE2MzI4MF5BMl5BanBnXkFtZTgwNTkxODgxOTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=xIBiJ_SzJTA",
                    "Tammi Sutton",
                    "Rami Malek",
                    86,
                    "http://www.imdb.com/title/tt4158110/?ref_=nv_sr_1",
                    2,
                    "2015",
                    "-")

house_of_cards = media.Show("House of Cards",
                    """A Congressman works with his equally conniving wife to exact revenge on the people who betrayed him.""",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM3ODMyMjc3MV5BMl5BanBnXkFtZTgwNDgzNDc5NzE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=ULwUzF1q5w4",
                    "Beau Willimon",
                    "Kevin Spacey, Robin Wright, Michael Gill",
                    90,
                    "http://www.imdb.com/title/tt4158110/?ref_=nv_sr_1",
                    5,
                    "2013",
                    "-")

narcos = media.Show("Narcos",
                    """A chronicled look at the criminal exploits of Colombian drug lord Pablo Escobar, as well as the many other drug dealers who plagued the country through the years.""",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU0ODQ4NDg2OF5BMl5BanBnXkFtZTgwNzczNTE4OTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=U7elNhHwgBU",
                    "Carlo Bernard",
                    "Pedro Pascal, Wagner Moura, Boyd Holbrook",
                    89,
                    "http://www.imdb.com/title/tt2707408/?ref_=nv_sr_1",
                    3,
                    "2015",
                    "-")

movies = [toy_story, avatar, fight_club, heat, casino, scarface, goodfellas]

shows = [dexter, game_thrones, westworld, mr_robot, house_of_cards, narcos]

fresh_tomatoes.open_movies_page(movies,shows)
#fresh_tomatoes.open_movies_page(shows)

