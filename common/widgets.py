from crispy_forms.layout import HTML



#--------------crispy form widget-----------------
class Link(HTML):
	""" crispy_forms object for html link <a href="#"></a> """

	template = '<a href="%(href)s">%(text)s</a>'
	template_with_class = '<a href="%(href)s" class="%(css_class)s">%(text)s</a>'

	def __init__(self, text, href='', css_class=''):
		self.text = text
		self.href = href or '#'
		self.css_class = css_class
		self.html = None
		self.ctx = None

		self._choose_html()
		self._render_html()

	def _choose_html(self):
		self.ctx = {
			'text': self.text,
			'href': self.href,
			'css_class': self.css_class
		}
		if self.css_class:
			self.html = self.template_with_class
		else:
			self.html = self.template

	def _render_html(self):
		self.html = self.html % self.ctx
