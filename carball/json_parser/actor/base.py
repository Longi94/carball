COMPONENT_REPLICATED_ACTIVE_KEY = 'TAGame.CarComponent_TA:ReplicatedActive'
REPLICATED_RB_STATE_KEY = 'TAGame.RBActor_TA:ReplicatedRBState'
COMPONENT_ACTIVE_KEY = 'TAGame.CarComponent_TA:Active'


class BaseActorHandler(object):
    """
    Base class for actor handlers.

    If can_handle is not overridden, it will check the type_name attribute. The priority attribute determines the order
    of the handlers. Lower number means higher priority. If the priority is the same, the order will depend on the order
    of actors int he replay.
    """
    type_name = None
    priority = 1000

    @classmethod
    def can_handle(cls, actor: dict) -> bool:
        """
        :param actor: the actor from the json frame
        :return: True if the the class can handle the actor
        """
        return cls.type_name is not None and cls.type_name == actor['TypeName']

    def __init__(self, parser: object):
        """
        :param parser: The FrameParser object
        """
        self.parser = parser

    def update(self, actor: dict, frame_number: int, time: float, delta: float) -> None:
        """
        Called for each frame the actor of this handler is alive for.

        :param actor: the actor of this handler
        :param frame_number: the number of the frame
        :param time: frame time
        :param delta: frame time delta
        """
        pass