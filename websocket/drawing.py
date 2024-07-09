from PIL import Image

class Drawing:
    """
    Represents an RGB image. Conceptually the image should be the most recent changes, even with latency and
    network outages (though in practice this isn't necessarily the case as clients have different clocks).
    
    It's a representation of what my computer science professors would've called a Conflict-free Replicated
    Data Type (there's a reason it's always abbreviated CRDT). Really all this means is that there's a way to
    consistenly resolve conflicting updates from multiple clients. In the end, all clients will see the same
    data regardless of the order they receive the updates in. This is a docstring, if this doesn't make sense
    just google CRDTs.
    """

    # TODO make the sizing dynamic
    __image = [0] * 50 * 50 * 3
    __times = [0] * 50 * 50
    __last_user = [0] * 50 * 50

    def change_pixel(self, x, y, color, user, timestamp):
        """
        Tries to change the underlying image. Returns True if the image was changed and False if otherwise.

        The image is only changed if the new timestamps is greater than the timestamp of the last change (or
        if there is a tie it will take the change of the user with the lower user number).
        """
        if timestamp < self.__times[x][y] or self.__times[x][y] == timestamp and user > self.__last_user():
            return False
        
        self.__image[x][y] = color
        self.__times[x][y] = timestamp
        self.__last_user[x][y] = user
        return True
    
    def get_image(self):
        return Image.fromarray(self.__image)
    