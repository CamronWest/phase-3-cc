# from classes.Movie import Movie 
# from classes.Viewer import Viewer
## got some awesome errors when I tried to import these classes


class Review:
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer 
        self.movie = movie
        self.rating = rating 
        

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if (type(rating) == int and rating > 0 and rating < 6):
            self._rating = rating
        else:
            raise Exception('rating is int and less than 5 characters') 

    @property
    def viewer(self):
        return self._viewer

    @viewer.setter
    def viewer(self,viewer):
        if isinstance(viewer, Viewer):
            self._viewer = viewer

    @property
    def movie(self):
        return  self._movie
    
    @movie.setter
    def movie(self,movie):
        if isinstance(movie, Movie):
            self._movie = movie
