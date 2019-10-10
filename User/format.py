import sublime
import sublime_plugin


class FormatCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		syntax = self.view.settings().get('syntax')

		fore_end = [
			'Packages/HTML/HTML.sublime-syntax',
			'Packages/JavaScript/JavaScript.sublime-syntax',
			'Packages/CSS/CSS.sublime-syntax'
		]

		if syntax in fore_end:
			self.view.run_command('htmlprettify')
			return None

		if syntax == 'Packages/PHP/PHP.sublime-syntax':
			self.view.run_command('code_formatter')
			return None
		
		
