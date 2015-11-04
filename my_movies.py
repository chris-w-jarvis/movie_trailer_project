import media
import fresh_tomatoes

# this is where all my movies and their information is stored, using the Movie
# class structure from the media.py file

# Movies

blood_diamond = media.Movie(
    'Blood Diamond',
	'https://upload.wikimedia.org/wikipedia/en/5/5a/Blooddiamondposter.jpg',
	'A mercenary helps a man find his family in the midst of diamond fueled'
	' civil war',
	'2006',
	'https://youtu.be/yknIZsvQjG4',
	'Leonardo Dicaprio, Djimon Honsou, Jennifer Connelly')
interstellar = media.Movie(
    'Interstellar',
	'https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg', #noqa
	'A man leaves his family in a desperate attempt to find another planet'
	' suitable for life',
	'2014',
	'https://youtu.be/2LqzF5WauAw',
	'Matthew McConaughey, Anne Hatheway, Matt Damon')
nacho_libre = media.Movie(
    'Nacho Libre',
	'https://upload.wikimedia.org/wikipedia/en/3/35/Nachopost.jpg',
	'A lowly monk chases his dream of fighting in the ring',
	'2006',
	'https://youtu.be/ElVSw6xpQ70',
	'Jack Black, Ana de la Reguera')
man_on_fire = media.Movie(
    'Man on Fire',
	'https://upload.wikimedia.org/wikipedia/en/e/e8/Man_on_fireposter.jpg',
	'A broken former CIA operative becomes a bodyguard',
	'2004',
	'https://youtube/g4kLizDXLY0',
	'Denzel Washington, Dakota Fanning, Christopher Walken')
casino_royale = media.Movie(
    'Casino Royale',
	'https://upload.wikimedia.org/wikipedia/en/1/15/Casino_Royale_2_-_UK_cinema_poster.jpg', #noqa
	'James Bond battles villain Le Chiffre in a high-stakes poker game',
	'2006',
	'https://youtu.be/fl5WHj0bZ2Q',
	'Daniel Craig, Judi Dench, Eva Green')

# TV Shows

ray_donovan = media.Television(
	'Ray Donovan',
	'http://www.gstatic.com/tv/thumb/tvbanners/9311951/p9311951_b_v7_ae.jpg',
	'Ray Donovan fixes problems for LA\'s wealthy elite but no amount'
	' of money and power is enough to hide from his troubled past',
	'2013',
	'Leiv Schreiber, John Voight, Stephen Bauer',
	'Showtime')
bored_to_death = media.Television(
	'Bored to Death',
	'http://www.gstatic.com/tv/thumb/tvbanners/3621786/p3621786_b_v7_ab.jpg',
	'A bumbling writer decides to change his life and moonlight as'
	'as a private detective',
	'2009',
	'Jason Schwartzman, Ted Danson, Zach Galifinakis',
	'HBO')

# Books

blood_meridian = media.Book(
	'Blood Meridian',
	'http://t3.gstatic.com/images?q=tbn:ANd9GcQU9dyQxn4l6kSpYw47jOueuC-3Kn0ZI9FBOfLGpyDhvfEnClOz', #noqa
	'A teenager stumbles into the violent events surrounding the Texas'
	'-Mexico border in the 1850\'s',
	'1985',
	'Cormac McCarthy')
fountainhead = media.Book(
	'The Fountainhead',
	'http://t3.gstatic.com/images?q=tbn:ANd9GcQ6L-0cbVEE7XRuAHIL1INcj74VUMKK63JRb_zFZcWgzCP9m9Jm', #noqa
	'A philophical fictional story asking the question \'Can man\'s ego'
	' be the fountainhead for human progress?\'',
	'1943',
	'Ayn Rand')
# put movies in list to use with fresh tomatoes method

movie_list = [blood_diamond,interstellar,nacho_libre,man_on_fire,
casino_royale]

tv_list = [ray_donovan, bored_to_death]

book_list = [blood_meridian, fountainhead]

# create website using fresh tomatoes module and my list of movies

fresh_tomatoes.open_movies_page(movie_list)


