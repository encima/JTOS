import jtos
import pytest

class TestJTOS:

    sw_obj = {
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

    s_obj = {
        'select': {
            'tables': [
                "users"
            ],
            'fields': [
                "email",
                "id",
                "password"
            ]
        }
    }

    so_obj = {
        'select': {
            'tables': [
                "users"
            ],
            'fields': [
                "email",
                "id",
                "password"
            ],
            'orderBy': {
                'email': 'ASC',
                'id': 'desc'
            }
        }
    }



    def test_creation(self):
        j = jtos.JTOS()
        assert j is not None

    def test_select_where(self):
        j = jtos.JTOS()
        stmt = j.parseObject(TestJTOS.sw_obj)
        print(stmt)
        assert stmt == "SELECT email,id,password FROM users WHERE email LIKE 't@test.com' OR name = 'test';"

    def test_select_order(self):
        j = jtos.JTOS()
        stmt = j.parseObject(TestJTOS.so_obj)
        print(stmt)
        assert stmt == "SELECT email,id,password FROM users ORDER BY email ASC, id DESC;"

    def test_select(self):
        j = jtos.JTOS()
        stmt = j.parseObject(TestJTOS.s_obj)
        print(stmt)
        assert stmt == "SELECT email,id,password FROM users;"

    


