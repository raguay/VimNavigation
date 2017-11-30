from fman import DirectoryPaneCommand
from fman.url import as_human_readable
from fman.url import as_url
from os.path import isdir, realpath


class OpenDirectory(DirectoryPaneCommand):
    def __call__(self, url=None):
        file_under_cursor = as_human_readable(self.pane.get_file_under_cursor())
        if url is None:
            if file_under_cursor and isdir(file_under_cursor):
                self.pane.set_path(as_url(realpath(file_under_cursor)))
        else:
            self.pane.set_path(url)
