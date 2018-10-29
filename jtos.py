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
        return query_string

    def buildWhere(self, where_object):
        where = ","
        clauses = []
        for w, v in where_object.items():
            if len(clauses) > 
            clauses.append("{0} {1} {2} {3}".format(v['join'], w, JTOS.mappings[v['op']], v['cmp']))
        return "WHERE " + where.join(clauses)

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