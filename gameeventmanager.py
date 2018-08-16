def event_fail():
    raise RuntimeError("Game event failure, unregistered event execution was attempted.")


class GameEvent(object):
    """
    Represents a GameEvent with an object key and an event key.

    The object key should be a stored reference to an object added to the GameEventManager using the register_object
    method.  The event key should be a key representing an associated event that can then be linked to an object.

    Usage might look something like:
    events = []
    ....
    for e in pygame.events.get():
        if e.type == pygame.QUIT():
            events.append(GameEvent.create('game', 'quit'))
        ...

    # then hand the events to the manager for callback executions
    GameEventManager.instance().process_events(events)
    """

    def __init__(self, obj_key, event_key):
        self.obj_key = obj_key
        self.event_key = event_key

    @staticmethod
    def create(obj_key, event_key):
        return GameEvent(obj_key, event_key)


class GameEventManager(object):
    """
    GameEventManager

    Callback manager used to register objects and then fire off methods when certain actions occur.

    Example Usage:

    gem = GameEventManager()
    # or you can use static instance with GameEventManager.instance() for cross package use (global if you will)
    gem.register_event('mouse_over_exit_btn')
    gem.register_object('exit_button', btn_object)
    gem.register_callback('exit_button', 'mouse_over_exit_btn', 'highlight')
    # NOTE: the method must exist on the registered object or it will product a runtime error (see event_fail above)

    # during processing, we want to trigger, so say you detect the mouse is over the button in your GUI logic
    # so you can trigger the method by doing something like this:
    ... event is detected
    events.append('mouse_over_exit_btn')  # events being a list

    # then in the "update" logic of your game
    gem.process_events(events)

    # that's it, it will trigger the mouse_over_exit_btn reference which will in turn trigger btn_object.highlight()

    Note that this class is not designed to allow callbacks to functions, only to object methods as it is specifically
    designed to facilitate easy of use with things like GUI's and game objects.
    """

    _INSTANCE = None

    def __init__(self):
        self._obj_registry = {}
        self._callback_registry = {}
        self._obj_lookup = {}

    @staticmethod
    def instance():
        """
        Retrieve the static global instance of GameEventManager
        :return: GameEventManager
        """
        if GameEventManager._INSTANCE is None:
            GameEventManager._INSTANCE = GameEventManager()
        return GameEventManager._INSTANCE

    def register_event(self, event_key: str):
        """
        Register an event lookup key
        :param event_key: string
        """
        if event_key not in self._obj_lookup.keys():
            self._obj_lookup[event_key] = []

    def register_object(self, obj_key: str, obj: object):
        """
        Register an object with a lookup key
        :param obj_key: string
        :param obj: object
        """
        if obj_key not in self._obj_registry.keys():
            self._obj_registry[obj_key] = obj

    def register_callback(self, obj_key: str, event_key: str, callback_method: str):
        """
        Register a callback method to a specific event related to an object
        :param obj_key: string
        :param event_key: string
        :param callback_method: string
        """
        if obj_key in self._obj_registry.keys() and event_key in self._obj_lookup.keys():
            if obj_key not in self._callback_registry.keys():
                self._callback_registry[obj_key] = {}
            if obj_key not in self._obj_lookup[event_key]:
                self._obj_lookup[event_key].append(obj_key)
            self._callback_registry[obj_key][event_key] = callback_method

    def process_events(self, event_list: list):
        """
        Process a list of GameEvents
        :param event_list: list of GameEvent objects
        """
        for game_event in event_list:
            if game_event.obj_key in self._callback_registry.keys():
                if game_event.event_key in self._callback_registry[game_event.obj_key]:
                    callback = getattr(self._obj_registry[game_event.obj_key],
                                       self._callback_registry[game_event.obj_key][game_event.event_key], event_fail)
                    callback()


# Tests
if __name__ == '__main__':

    class Test(object):

        def __init__(self):
            self.count = 0

        def run(self):
            self.count += 1
            print("Ran, count is {}".format(self.count))


    t = Test()
    e = GameEventManager()
    e.register_object('test', t)
    e.register_event('good_call')
    e.register_event('bad_call')
    e.register_callback('test', 'good_call', 'run')
    e.register_callback('test', 'bad_call', 'does_not_exist')
    events = ["good_call", "good_call", "good_call", "bad_call"]
    try:
        e.process_events(events)
    except RuntimeError as e:
        print("Runtime error caught")
