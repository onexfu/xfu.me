import urllib2, json


class Photo:
	def __init__(self, width=0, url='', view_url=''):
		self.__width = width
		self.__url = url
		self.__view_url = view_url
	
	def getWidth(self):
		return self.__width
	
	def getURL(self):
		return self.__url
	
	def getViewURL(self):
		return self.__view_url


class Gallery:
	def __init__(self, album_name, pic_size):
		# album_name example: "bscarf" or "Bscarf"
		self.album_name = album_name
		self.pic_size = pic_size
		self.gallery = []
		if self.album_name and self.pic_size:
			self._build_url()
	
	def _build_url(self):
		self.album_url = 'http://picasaweb.google.com/data/feed/base/user/103555595427198734694/album/%s?alt=json&imgmax=%sc&v=2.0' % (self.album_name, self.pic_size)
	
	def _getAlbumJSON(self):
		page = urllib2.urlopen(self.album_url)
		album_json = json.loads(page.read())
		page.close()
		return album_json
		

	def build(self):
		
		album_json = self._getAlbumJSON()
		
		for entry in album_json['feed']['entry']:
			self.gallery.append( Photo(width=self.pic_size, url=entry['content']['src'], view_url=entry['link'][1]['href']) )

		return self.gallery