class JTOS:

    mappings = {
        'gt': '>',
        'lt': '<',
        'gte': '>=',
        'lte': '<=',
        'e': '=',
        'ne': '!=',
        'l': 'LIKE',
        'nl': 'NOT LIKE',
        'a': 'AND',
        'o': 'OR'
    }

    def __init__(self):
        pass

    def set_object(self):
        pass

    def parse_object(self, obj):
        query_string = ""
        print(obj['select'])
        if 'select' in obj:
            query_string += JTOS.build_select(obj['select'])
        if 'where' in obj:
            query_string += JTOS.build_where(obj['where'])
        if 'orderBy' in obj['select']:
            query_string += JTOS.build_order(obj['select']['orderBy'])

        return query_string.replace("  ", " ") + ";"

    @staticmethod
    def build_where(where_object):
        clauses = []
        for w, v in where_object.items():
            join = None
            if len(clauses) > 0:
                join = 'AND' if 'join' not in v else v['join']
            val = "'{}'".format(v['val']) if not isinstance(v['val'], int) else v['val'] 
            clauses.append(" {0} {1} {2} {3}".format(JTOS.mappings[join] if join in JTOS.mappings else "", w, JTOS.mappings[v['op']], val))
        return " WHERE" + "".join(clauses)

    @staticmethod
    def build_select(select_object):
        f = ",".join(select_object['fields'])
        t = ",".join(select_object['tables'])
        select = "SELECT {0} FROM {1}".format(f, t)
        # TODO handle Joins
        return select

    @staticmethod
    def build_join(join_object):
        f = join_object['conditions']['from']
        t = join_object['conditions']['to']
        jt = join_object['type']
        join = "{0} JOIN {1} ON {1}.{2} = {3}.{4}".format(jt, f['table'], f['field'], t['table'], t['field'])
        return join

    @staticmethod
    def build_order(order_object):
        fields = []
        for k, v in order_object.items():
            fields.append("{0} {1}".format(k, v.upper()))
        return " ORDER BY " + ", ".join(fields)

    @staticmethod
    def build_insert(insert_object):
        pass

    @staticmethod
    def build_delete(delete_object):
        pass

    @staticmethod
    def build_update(update_object):
        pass

    @staticmethod
    def build_create(create_object):
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
#         orderBy: {
#            "field": "ASC" 
#         }
#     }
#     where: {
#         field: {
#             op: gt | lt | nl,
#             cmp: 0
#             join: 'AND'
#         }
#     }
# }