import media
import fresh_tomatoes

#this is where all my movies and their information is stored, using the Movie class
#structure from the media.py file

blood_diamond = media.Movie('Blood Diamond',
	'https://upload.wikimedia.org/wikipedia/en/5/5a/Blooddiamondposter.jpg',
	'https://youtu.be/yknIZsvQjG4',
	'2006')
interstellar = media.Movie('Interstellar',
	'https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg',
	'https://youtu.be/2LqzF5WauAw',
	'2014')
nacho_libre = media.Movie('Nacho Libre',
	'https://upload.wikimedia.org/wikipedia/en/3/35/Nachopost.jpg',
	'https://youtu.be/ElVSw6xpQ70',
	'2006')
man_on_fire = media.Movie('Man on Fire',
	'https://upload.wikimedia.org/wikipedia/en/e/e8/Man_on_fireposter.jpg',
	'https://youtube/g4kLizDXLY0',
	'2004')
act_of_killing = media.Movie('The Act of Killing',
	'https://upload.wikimedia.org/wikipedia/en/c/ca/The_Act_of_Killing_%282012_film%29.jpg',
	'https://youtu.be/SD5oMxbMcHM',
	'2013')
casino_royale = media.Movie('Casino Royale',
	'https://upload.wikimedia.org/wikipedia/en/1/15/Casino_Royale_2_-_UK_cinema_poster.jpg',
	'https://youtu.be/fl5WHj0bZ2Q',
	'2006')

#put movies in list to use with fresh tomatoes method

movies_list = [blood_diamond,interstellar,nacho_libre,man_on_fire,act_of_killing,casino_royale]

#create website using fresh tomatoes module and my list of movies

fresh_tomatoes.open_movies_page(movies_list)


