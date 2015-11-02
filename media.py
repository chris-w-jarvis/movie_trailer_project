import webbrowser
class Movie():
	'''allows movie information to be stored for each movie'''
	def __init__(self, movie_title, box_art_url, youtube_trailer_link):
		self.title = movie_title
		self.art = box_art_url
		self.trailer = youtube_trailer_link

	def open_trailer():
		webbrowser.open(self.trailer)