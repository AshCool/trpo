from abc import ABCMeta, abstractmethod


# Observer interface
class AbstractFollower(metaclass=ABCMeta):

    def __init__(self, _name: str):
        self.name = _name


# Observable interface
class Followable(metaclass=ABCMeta):

    def __init__(self):

        self.followers = []

    @abstractmethod
    def notify_followers(self, status: str):

        pass

    @abstractmethod
    def add_follower(self, follower: AbstractFollower):
        pass


# Observable's implementation
class Source(Followable):

    def __init__(self, _name: str):

        super().__init__()
        self.name = _name

    def notify_followers(self, status: str):

        for follower in self.followers:
            follower.get_update(self, status)

    def add_follower(self, follower: AbstractFollower):

        self.followers.append(follower)


# Observer's implementation
class Follower(AbstractFollower):

    def subscribe(self, source: Followable):

        source.add_follower(self)

    def get_update(self, source: Source, status: str):

        print(self.name + " got updated. New " + source.name + "'s status is " + status)


if __name__ == "__main__":

    content_king = Source("Content King")
    # thus adding followers to the Observable's Observers list
    Follower("Jake").subscribe(content_king)
    Follower("Tom").subscribe(content_king)
    Follower("Alex").subscribe(content_king)
    # well, notifying all the followers
    content_king.notify_followers("The king around content")
