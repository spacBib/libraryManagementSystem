from fakerData.fake_item_factory.fake_user_factory import FakeUserFactory

factory = FakeUserFactory()

book = factory.create(0)

book.print()
