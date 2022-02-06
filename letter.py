class Letter():
    ''' 
    This class serves as a simple letter object. These letters hold information about any verified values for the character (in the case of the game any letter
    that popped up as green) as well as any characters that were yellow within this characters position meaning they were verified to exist elswhere within the
    word.
    '''
    def __init__(self):
        self.verified_value = ''
        self.verified_elsewhere = []
