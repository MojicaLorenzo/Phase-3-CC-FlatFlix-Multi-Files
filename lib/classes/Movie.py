class Movie:
    def __init__(self, title):
        self.title = title

        self._reviews = []
        self._viewers = []
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title

    def reviews(self):
        return self._reviews

    def reviewers(self):
        return list(set(self._viewers))

    def average_rating(self):
        if self._reviews:
            avg = sum([review.rating for review in self._reviews]) / len(self._reviews)

            rounded_avg = round(avg, 1)
            return rounded_avg
        else:
            return None