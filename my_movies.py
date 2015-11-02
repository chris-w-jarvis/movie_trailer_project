import media
import fresh_tomatoes

blood_diamond = media.Movie('Blood Diamond',
	'https://upload.wikimedia.org/wikipedia/en/5/5a/Blooddiamondposter.jpg',
	'https://youtu.be/yknIZsvQjG4')
interstellar = media.Movie('Interstellar',
	'https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg',
	'https://youtu.be/2LqzF5WauAw')
nacho_libre = media.Movie('Nacho Libre',
	'https://upload.wikimedia.org/wikipedia/en/3/35/Nachopost.jpg',
	'https://youtu.be/ElVSw6xpQ70')
man_on_fire = media.Movie('Man on Fire',
	'https://upload.wikimedia.org/wikipedia/en/e/e8/Man_on_fireposter.jpg'
	'https://youtu.be/g4kLizDXLY0')
act_of_killing = media.Movie('The Act of Killing',
	'https://upload.wikimedia.org/wikipedia/en/c/ca/The_Act_of_Killing_%282012_film%29.jpg',
	'https://youtu.be/SD5oMxbMcHM')
casino_royale = media.Movie('Casino Royale',
	'https://upload.wikimedia.org/wikipedia/en/1/15/Casino_Royale_2_-_UK_cinema_poster.jpg'
	'https://youtu.be/fl5WHj0bZ2Q')

movies_list = [blood_diamond,interstellar,nacho_libre,man_on_fire,act_of_killing,casino_royale]

fresh_tomatoes.open_movies_page(movies_list)


