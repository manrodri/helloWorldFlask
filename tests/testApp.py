#!flask/bin/python
import os
import unittest

from config import basedir
from app import app, db
from app.models import User

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_avatar(self):
        u = User(username='john', email='john@example.com')
        avatar = u.avatar(128)
        expected = 'https://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6'
        self.assertEqual(avatar[0:len(expected)], expected)
        #assert avatar[0:len(expected)] == expected

    #todo write tests for User model
    @unittest.skip
    def test_make_unique_nickname(self):
        u = User(username='john', email='john@example.com')
        db.session.add(u)
        db.session.commit()
        nickname = User.make_unique_nickname('john')
        self.assertNotEqual(nickname, 'john')
        #assert nickname != 'john'
        u = User(nickname=nickname, email='susan@example.com')
        db.session.add(u)
        db.session.commit()
        nickname2 = User.make_unique_nickname('john')
        self.assertNotEqual(nickname2, 'john')
        self.assertNotEqual(nickname2, nickname)
        #assert nickname2 != 'john'
        #assert nickname2 != nickname

if __name__ == '__main__':
    unittest.main()
