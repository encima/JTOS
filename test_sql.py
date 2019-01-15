import jtos
import pytest


class TestJTOS:

    sw_obj = {
        "select": {"tables": ["users"], "fields": ["email", "id", "password"]},
        "where": {
            "email": {"op": "l", "val": "t@test.com"},
            "name": {"op": "e", "val": "test", "join": "a"},
            "id": {"op": "e", "val": 3, "join": "o"},
        },
    }

    s_obj = {"select": {"tables": ["users"], "fields": ["email", "id", "password"]}}

    so_obj = {
        "select": {
            "tables": ["users"],
            "fields": ["email", "id", "password"],
            "orderBy": {"email": "ASC", "id": "desc"},
        }
    }
    jo_obj = {
        'join': {
            'type': 'left',
            'conditions': {
                'from': {
                    'table': 'activities',
                    'field': 'id'
                },
                'to': {
                    'table': 'users',
                    'field': 'id'
                }
            }
        }
    }
    def test_creation(self):
        j = jtos.JTOS()
        assert j is not None

    def test_select_where(self):
        j = jtos.JTOS()
        stmt = j.parse_object(TestJTOS.sw_obj)
        print(stmt)
        assert (
            stmt
            == "SELECT email,id,password FROM users WHERE email LIKE 't@test.com' AND name = 'test' OR id = 3;"
        )

    def test_select_order(self):
        j = jtos.JTOS()
        stmt = j.parse_object(TestJTOS.so_obj)
        print(stmt)
        assert (
            stmt == "SELECT email,id,password FROM users ORDER BY email ASC, id DESC;"
        )

    def test_join(self):
        j = jtos.JTOS()
        stmt = j.build_join(TestJTOS.jo_obj['join'])
        print(stmt)
        assert stmt == "left JOIN activities ON activities.id = users.id"

    def test_select(self):
        j = jtos.JTOS()
        stmt = j.parse_object(TestJTOS.s_obj)
        print(stmt)
        assert stmt == "SELECT email,id,password FROM users;"
