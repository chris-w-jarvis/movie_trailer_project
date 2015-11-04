import webbrowser
class Media():
	'''store basic information for general medium type'''
	def __init__(self, title, image_url, description, year):
		self.title = title
		self.art = image_url
		self.description = description
		self.year = year

class Movie(Media):
	'''film inherits from Media, adding a trailer, cast and a method;
	cast should be the three main actors'''
	def __init__(self,title, image_url, description, year, trailer_url, 
	cast):
		Media.__init__(self, title, image_url, description, year)
		self.trailer = trailer_url
		self.cast = cast

	def open_trailer():
		webbrowser.open(self.trailer)

class Television(Media, Movie):
	'''inherits from Media and the trailer attribute from Movie, adds
	a network attribute'''
	def __init__(self, title, image_url, description, year, cast, network):
		Media.__init__(self, title, image_url, description, year)
		self.cast = cast
		self.network = network

class Book(Media):
	def __init__(self, title, image_url, description, year, author):
		Media.__init__(self, title, image_url, description, year)
		self.author = author


