import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A Story of a boy and his toys.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=NBepTulmSMw")
#print(toy_story.storyline)
#print(toy_story.poster_image_url)

avatar = media.Movie ("Avatar", "A marine on an alien planet",
                      "http://images2.fanpop.com/image/photos/10800000/Avatar-avatar-10806310-1280-960.jpg",
                      "https://www.youtube.com/watch?v=-ceBgWV8io")
#print(avatar.storyline)
#avatar.show_trailer()

justice_league = media.Movie ("Justice League", "A superhero Movie",
                      "https://upload.wikimedia.org/wikipedia/commons/8/8b/Justice_League_2017_film_logo.jpg",
                      "https://www.youtube.com/watch?v=RWCQ22JyCL4")
#justice_league.show_trailer()

movies = [toy_story, avatar, justice_league]

fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
print(media.__name__)
print(__name__)
print(__module__)
