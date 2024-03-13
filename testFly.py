from fakerData.fake_item_factory import FakeUserFactory

from userInterface.user_action_factory import UserActionFactory
from userInterface.user_choice_selector import UserChoiceSelector

from userInterface import UserInteraction

_userFactory = FakeUserFactory()
_user = _userFactory.create(47)

_user_interaction = UserInteraction(_user)
_user_interaction.start_user_interaction()