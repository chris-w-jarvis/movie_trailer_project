import webbrowser
class Movie():
	'''allows movie information to be stored for each movie'''
	def __init__(self, movie_title, poster_image_url, trailer_youtube_url, year):
		self.title = movie_title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.year = year

	def open_trailer():
		webbrowser.open(self.trailer)
