

class JTOS:

    mappings = {
        'gt': '>',
        'lt': '<',
        'gte': '>=',
        'lte': '<=',
        'e': '=',
        'l': 'LIKE',
        'nl': 'NOT LIKE'
    }

    def __init__(self, query):
        self.q = query
        self.query_string = ""
        if 'select' in self.q:
            self.query_string += self.buildSelect(self.q['select'])
        if 'where' in self.q:
            self.query_string += self.buildWhere(self.q['where'])

    def buildWhere(self, where_object):
        where = ","
        clauses = []
        for w, v in where_object.items():
            clauses.append("{0} {1} {2}".format(w, JTOS.mappings[v['op']], v['cmp']))
        return "WHERE " + where.join(clauses)



    def buildSelect(self, select_object):
        f = ",".join(select_object['fields'])
        t = ",".join(select_object['tables'])
        select = "SELECT {0} FROM {1} ".format(f,t)
        return select

    def buildInsert(self, insert_object):
        pass

    def buildDelete(self, delete_object):
        pass

    def buildUpdate(self, update_object):
        pass

    def buildCreate(self, create_object):
        pass

if __name__ == "__main__":
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
            }
        }
    }
    j = JTOS(obj)
    print(j.query_string)


# {
#     select: {
#         tables: [
#             "",
#             ""
#         ],
#         fields: [
#             "",
#             ""
#         ],
#         orderBy: [
#         ]
#     }
#     where: {
#         field: {
#             op: gt | lt | nl,
#             cmp: 0
#             join: 'AND'
#         }
#     }
# }