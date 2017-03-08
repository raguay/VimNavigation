from fman import DirectoryPaneCommand, show_alert
from os.path import isdir, realpath
from os import listdir

class OpenDirectory(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		if file_under_cursor and isdir(file_under_cursor):
			self.pane.set_path(realpath(file_under_cursor))
