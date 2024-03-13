from userInterface.user_action_factory import UserActionFactory

factory = UserActionFactory()

_list = factory.create_list_of_all()

for _action in _list:
    print(_action.name)