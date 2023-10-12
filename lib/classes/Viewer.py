class Viewer:

    all = []

    def __init__(self, username):
        self.username = username

        self._reviews = []
        self._movies = []
        Viewer.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 6 <= len(username) <=16 :
            self._username = username

    def reviews(self):
        return self._reviews

    def reviewed_movies(self):
        return list(set(self._movies))

    def has_reviewed_movie(self, movie):
        return movie in self._movies

    def add_review(self, movie, rating):
        from classes.Review import Review
        new_review = Review(self, movie, rating)
        return new_review
