class Viewer:
    
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if(type(username) == str and (len(username) >5 and len(username) < 17)):
            self._username = username
        else:
            raise Exception('username must be 5 characters or less.')

    def reviewed_movie(self, movie):
        pass

    def rate_movie(self, movie, rating):
        pass


def unique_string(string):
    """function iterates over a string and tests if any character equals each other in sequence """
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if(string[i] == str[j]):
                return False
    return True

