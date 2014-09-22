from django.test import TestCase

import mongoengine


class MongoTestCase(TestCase):
    DB_NAME = 'unit-test'

    def __init__(self, method_name='runtest'):
        self.connection = mongoengine.connect(self.DB_NAME)
        super(MongoTestCase, self).__init__(method_name)

    def _post_teardown(self):
        connection = mongoengine.connection.get_connection()
        connection.drop_database(self.DB_NAME)
        connection.disconnect()
        super(MongoTestCase, self)._post_teardown()

    def _fixture_setup(self):
        return

    def _fixture_teardown(self):
        return