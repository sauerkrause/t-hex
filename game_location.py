class GameLocation(object):
    def __init__(self, coords):
        self._terrain = None
        self._contents = []
        self._coords = coords

    @property
    def terrain(self):
        return self._terrain

    @terrain.setter
    def terrain(self, value):
        self._terrain = value

    @property
    def contents(self):
        return self._contents

    def add_content(self, content):
        self._contents.append(content)
