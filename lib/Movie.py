class Movie:
    
    def __init__(self, title):
        self.title = title
        self.ratings = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        """initializes title and tests an input to be equal to a string and
          checks length is greater than 0 raises error otherwise."""
        
        if type(title) == str and (len(title) > 0):
            self._title = title
        else:
            raise Exception('requires string to be greater than 0')

    def average_rating(self):
        pass
    
    def get_num_ratings(self):
        return len(self.ratings)
    
    @classmethod
    def highest_rated(cls):
        pass
