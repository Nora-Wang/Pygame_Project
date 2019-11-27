import constants


class PlayRest(object):
    """ account the result """
    __score = 0     # total score
    __life = 1      # times
    __blood = 1000  # life value

    @property
    def score(self):
        """ score of one time game """
        return self.__score

    @score.setter
    def score(self, value):
        """ set the score """
        if value < 0:
            return None
        self.__score = value

    def set_history(self):
        """ recored the highest """
        if int(self.get_max_core()) < self.score:
            with open(constants.PLAY_RESULT_STORE_FILE, 'w') as f:
                f.write('{0}'.format(self.score))

    def get_max_core(self):
        """ read the highest """
        rest = 0
        with open(constants.PLAY_RESULT_STORE_FILE, 'r') as f:
            r = f.read()
            if r:
                rest = r
        return rest
