class JTOS:

    mappings = {
        'gt': '>',
        'lt': '<',
        'gte': '>=',
        'lte': '<=',
        'e': '=',
        'l': 'LIKE',
        'nl': 'NOT LIKE',
        'a': 'AND',
        'o': 'OR'
    }

    def __init__(self):
        pass

    def set_object(self):
        pass

    def parseObject(self, obj):
        query_string = ""
        if 'select' in obj:
            query_string += self.buildSelect(obj['select'])
        if 'where' in obj:
            query_string += self.buildWhere(obj['where'])
        return query_string.replace("  ", " ")

    def buildWhere(self, where_object):
        clauses = []
        for w, v in where_object.items():
            join = None
            if len(clauses) > 0:
                join = 'AND' if not 'join' in v else v['join']
            clauses.append(" {0} {1} {2} '{3}'".format(JTOS.mappings[join] if join in JTOS.mappings else "", w, JTOS.mappings[v['op']], v['cmp']))
        return "WHERE" + "".join(clauses)

    def buildSelect(self, select_object):
        f = ",".join(select_object['fields'])
        t = ",".join(select_object['tables'])
        select = "SELECT {0} FROM {1} ".format(f,t)
        # TODO handle Joins
        return select

    def buildInsert(self, insert_object):
        pass

    def buildDelete(self, delete_object):
        pass

    def buildUpdate(self, update_object):
        pass

    def buildCreate(self, create_object):
        pass

# TODO auth against existing models to prevent malicious intent


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