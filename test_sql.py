import jtos
import pytest

class TestJTOS:

    obj = {
        'select': {
            'tables': [
                "users"
            ],
            'fields': [
                "email",
                "id",
                "password"
            ]
        },
        'where': {
            'email': {
                'op': 'l',
                'cmp': 't@test.com'
            },
            'name': {
                'op': 'e',
                'cmp': 'test',
                'join': 'o'
            }
        }
    }

    def test_creation(self):
        j = jtos.JTOS()
        assert j is not None

    def test_output(self):
        j = jtos.JTOS()
        stmt = j.parseObject(TestJTOS.obj)
        print(stmt)
        assert stmt == "SELECT email,id,password FROM users WHERE email LIKE 't@test.com' OR name = 'test'"

    


