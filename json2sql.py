from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'sqlJsonGenerator', u'colors', u'sqlString'])
var.put(u'colors', var.get(u'require')(Js(u'colors')))
var.put(u'sqlString', var.get(u'require')(Js(u'sqlstring')))
@Js
def PyJs_anonymous_0_(options, this, arguments, var=var):
    var = Scope({u'this':this, u'options':options, u'arguments':arguments}, var)
    var.registers([u'escaping', u'joinBuilder', u'options', u'whereBuilder', u'selectBuilder', u'enclosure'])
    if var.get(u'options').neg():
        PyJs_Object_1_ = Js({})
        var.put(u'options', PyJs_Object_1_)
    @Js
    def PyJs_anonymous_2_(data, this, arguments, var=var):
        var = Scope({u'this':this, u'data':data, u'arguments':arguments}, var)
        var.registers([u'data'])
        if (PyJsStrictEq(var.get(u'data',throw=False).typeof(),Js(u'string')) and var.get(u'options').get(u'escaped')):
            return var.get(u'sqlString').callprop(u'escape', var.get(u'data'))
        else:
            if (PyJsStrictNeq(var.get(u'data',throw=False).typeof(),Js(u'string')) and var.get(u'options').get(u'prestoDB')):
                return var.get(u'data')
            else:
                return ((Js(u"'")+var.get(u'data'))+Js(u"'"))
    PyJs_anonymous_2_._set_name(u'anonymous')
    var.put(u'escaping', PyJs_anonymous_2_)
    @Js
    def PyJs_anonymous_3_(param, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'param':param}, var)
        var.registers([u'param'])
        if (var.get(u'options').get(u'pgSQL') or var.get(u'options').get(u'prestoDB')):
            return var.get(u'param')
        else:
            return ((Js(u'`')+var.get(u'param'))+Js(u'`'))
    PyJs_anonymous_3_._set_name(u'anonymous')
    var.put(u'enclosure', PyJs_anonymous_3_)
    @Js
    def PyJs_anonymous_4_(conditions, parentKey, inheritedTable, this, arguments, var=var):
        var = Scope({u'this':this, u'parentKey':parentKey, u'conditions':conditions, u'inheritedTable':inheritedTable, u'arguments':arguments}, var)
        var.registers([u'inheritedTable', u'parentKey', u'inBuilder', u'operatorSQL', u'conditionBuilder', u'operator', u'inCondition', u'result', u'whereKeys', u'currentTable', u'whereArray', u'conditions', u'andArray'])
        var.put(u'whereKeys', var.get(u'Object').callprop(u'keys', var.get(u'conditions')))
        var.put(u'whereArray', Js([]))
        @Js
        def PyJs_anonymous_5_(column, table, operador, condition, this, arguments, var=var):
            var = Scope({u'operador':operador, u'arguments':arguments, u'column':column, u'table':table, u'this':this, u'condition':condition}, var)
            var.registers([u'column', u'table', u'operador', u'condition'])
            return (((((((var.get(u'enclosure')(var.get(u'table'))+Js(u'.')) if var.get(u'table') else Js(u''))+var.get(u'enclosure')(var.get(u'column')))+Js(u' '))+var.get(u'operador'))+Js(u' '))+var.get(u'escaping')(var.get(u'condition')))
        PyJs_anonymous_5_._set_name(u'anonymous')
        var.put(u'conditionBuilder', PyJs_anonymous_5_)
        @Js
        def PyJs_anonymous_6_(column, table, operador, condition, this, arguments, var=var):
            var = Scope({u'operador':operador, u'arguments':arguments, u'column':column, u'table':table, u'this':this, u'condition':condition}, var)
            var.registers([u'column', u'table', u'operador', u'condition'])
            return (((((((var.get(u'enclosure')(var.get(u'table'))+Js(u'.')) if var.get(u'table') else Js(u''))+var.get(u'enclosure')(var.get(u'column')))+Js(u' '))+var.get(u'operador'))+Js(u' '))+var.get(u'condition'))
        PyJs_anonymous_6_._set_name(u'anonymous')
        var.put(u'inBuilder', PyJs_anonymous_6_)
        if var.get(u'options').get(u'debug'):
            var.get(u'console').callprop(u'log', Js(u''))
            var.get(u'console').callprop(u'log', Js(u'whereBuilder').get(u'green'))
            var.get(u'console').callprop(u'log', Js(u'  conditions: '), var.get(u'conditions'))
            var.get(u'console').callprop(u'log', Js(u'  parentKey: '), var.get(u'parentKey'))
            var.get(u'console').callprop(u'log', Js(u'  inheritedTable: '), var.get(u'inheritedTable'))
        if (var.get(u'Array').callprop(u'isArray', var.get(u'conditions')) and (var.get(u'conditions').get(u'length')>Js(0.0))):
            if var.get(u'options').get(u'debug'):
                var.get(u'console').callprop(u'log', Js(u'    splitting conditions').get(u'cyan'))
            @Js
            def PyJs_anonymous_7_(condition, this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments, u'condition':condition}, var)
                var.registers([u'whereExpression', u'condition'])
                var.put(u'whereExpression', var.get(u'whereBuilder')(var.get(u'condition'), var.get(u'parentKey'), var.get(u'inheritedTable')))
                if var.get(u'whereExpression'):
                    var.get(u'whereArray').callprop(u'push', var.get(u'whereExpression'))
            PyJs_anonymous_7_._set_name(u'anonymous')
            var.get(u'conditions').callprop(u'forEach', PyJs_anonymous_7_)
            return var.get(u'whereArray').callprop(u'join', Js(u' AND '))
        if (var.get(u'conditions',throw=False).typeof()!=Js(u'object')):
            if var.get(u'options').get(u'debug'):
                var.get(u'console').callprop(u'log', Js(u'    wrong condition format').get(u'red'))
            return var.get(u"null")
        if var.get(u'conditions').get(u'$raw'):
            return var.get(u'conditions').get(u'$raw')
        if (var.get(u'conditions').get(u'$or') or var.get(u'conditions').get(u'$and')):
            pass
            pass
            if var.get(u'conditions').get(u'$or'):
                var.put(u'operator', Js(u'$or'))
                var.put(u'operatorSQL', Js(u' OR '))
            else:
                if var.get(u'conditions').get(u'$and'):
                    var.put(u'operator', Js(u'$and'))
                    var.put(u'operatorSQL', Js(u' AND '))
            if var.get(u'options').get(u'debug'):
                var.get(u'console').callprop(u'log', var.get(u'colors').callprop(u'cyan', Js(u'    logical operator %s')), var.get(u'operator'))
            var.put(u'andArray', Js([]))
            @Js
            def PyJs_anonymous_8_(element, this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments, u'element':element}, var)
                var.registers([u'element'])
                var.get(u'andArray').callprop(u'push', var.get(u'whereBuilder')(var.get(u'element'), var.get(u"null"), var.get(u'inheritedTable')))
            PyJs_anonymous_8_._set_name(u'anonymous')
            var.get(u'conditions').get(var.get(u'operator')).callprop(u'forEach', PyJs_anonymous_8_)
            return ((Js(u'(')+var.get(u'andArray').callprop(u'join', var.get(u'operatorSQL')))+Js(u')'))
        if var.get(u'conditions').get(u'$field'):
            if var.get(u'options').get(u'debug'):
                var.get(u'console').callprop(u'log', Js(u'    full field comparaison').get(u'cyan'))
            var.put(u'currentTable', (var.get(u'conditions').get(u'$table') if var.get(u'conditions').get(u'$table') else var.get(u'inheritedTable')))
            if PyJsStrictNeq(var.get(u'conditions').get(u'$gt').typeof(),Js(u'undefined')):
                return var.get(u'conditionBuilder')(var.get(u'conditions').get(u'$field'), var.get(u'currentTable'), Js(u'>'), var.get(u'conditions').get(u'$gt'))
            else:
                if PyJsStrictNeq(var.get(u'conditions').get(u'$gte').typeof(),Js(u'undefined')):
                    return var.get(u'conditionBuilder')(var.get(u'conditions').get(u'$field'), var.get(u'currentTable'), Js(u'>='), var.get(u'conditions').get(u'$gte'))
                else:
                    if PyJsStrictNeq(var.get(u'conditions').get(u'$lt').typeof(),Js(u'undefined')):
                        return var.get(u'conditionBuilder')(var.get(u'conditions').get(u'$field'), var.get(u'currentTable'), Js(u'<'), var.get(u'conditions').get(u'$lt'))
                    else:
                        if PyJsStrictNeq(var.get(u'conditions').get(u'$lte').typeof(),Js(u'undefined')):
                            return var.get(u'conditionBuilder')(var.get(u'conditions').get(u'$field'), var.get(u'currentTable'), Js(u'<='), var.get(u'conditions').get(u'$lte'))
                        else:
                            if PyJsStrictNeq(var.get(u'conditions').get(u'$eq').typeof(),Js(u'undefined')):
                                return var.get(u'conditionBuilder')(var.get(u'conditions').get(u'$field'), var.get(u'currentTable'), Js(u'='), var.get(u'conditions').get(u'$eq'))
                            else:
                                if PyJsStrictNeq(var.get(u'conditions').get(u'$ne').typeof(),Js(u'undefined')):
                                    return var.get(u'conditionBuilder')(var.get(u'conditions').get(u'$field'), var.get(u'currentTable'), Js(u'<>'), var.get(u'conditions').get(u'$ne'))
                                else:
                                    if PyJsStrictNeq(var.get(u'conditions').get(u'$like').typeof(),Js(u'undefined')):
                                        return var.get(u'conditionBuilder')(var.get(u'conditions').get(u'$field'), var.get(u'currentTable'), Js(u'LIKE'), var.get(u'conditions').get(u'$like'))
                                    else:
                                        if PyJsStrictNeq(var.get(u'conditions').get(u'$in').typeof(),Js(u'undefined')):
                                            if var.get(u'options').get(u'debug'):
                                                var.get(u'console').callprop(u'log', Js(u'      $in').get(u'cyan'))
                                            if (var.get(u'Array').callprop(u'isArray', var.get(u'conditions').get(u'$in')) and (var.get(u'conditions').get(u'$in').get(u'length')>Js(0.0))):
                                                @Js
                                                def PyJs_anonymous_9_(condition, idx, this, arguments, var=var):
                                                    var = Scope({u'this':this, u'idx':idx, u'condition':condition, u'arguments':arguments}, var)
                                                    var.registers([u'idx', u'condition'])
                                                    var.get(u'conditions').get(u'$in').put(var.get(u'idx'), var.get(u'escaping')(var.get(u'condition')))
                                                PyJs_anonymous_9_._set_name(u'anonymous')
                                                var.get(u'conditions').get(u'$in').callprop(u'forEach', PyJs_anonymous_9_)
                                                var.put(u'inCondition', ((Js(u'(')+var.get(u'conditions').get(u'$in').callprop(u'join', Js(u',')))+Js(u')')))
                                                return var.get(u'inBuilder')(var.get(u'conditions').get(u'$field'), var.get(u'currentTable'), Js(u'IN'), var.get(u'inCondition'))
                                            else:
                                                return var.get(u"null")
        if (var.get(u'whereKeys').get(u'length')==Js(1.0)):
            var.put(u'result', var.get(u'conditionBuilder')(var.get(u'whereKeys').get(u'0'), var.get(u'inheritedTable'), Js(u'='), var.get(u'conditions').get(var.get(u'whereKeys').get(u'0'))))
            if var.get(u'options').get(u'debug'):
                var.get(u'console').callprop(u'log', Js(u'    simple columns equality shortcut').get(u'cyan'))
                var.get(u'console').callprop(u'log', var.get(u'colors').callprop(u'yellow', Js(u'      result: %s')), var.get(u'result'))
            return var.get(u'result')
        return var.get(u"null")
    PyJs_anonymous_4_._set_name(u'anonymous')
    var.put(u'whereBuilder', PyJs_anonymous_4_)
    @Js
    def PyJs_anonymous_10_(joinData, curentTable, inheritedTable, this, arguments, var=var):
        var = Scope({u'joinData':joinData, u'curentTable':curentTable, u'this':this, u'inheritedTable':inheritedTable, u'arguments':arguments}, var)
        var.registers([u'curentTable', u'sqlJoin', u'joinKeys', u'tempArray', u'joinData', u'inheritedTable'])
        if var.get(u'options').get(u'debug'):
            var.get(u'console').callprop(u'log', Js(u''))
            var.get(u'console').callprop(u'log', Js(u'joinBuilder').get(u'green'))
            var.get(u'console').callprop(u'log', Js(u'  curentTable: '), var.get(u'curentTable'))
            var.get(u'console').callprop(u'log', Js(u'  inheritedTable: '), var.get(u'inheritedTable'))
            var.get(u'console').callprop(u'log', Js(u'  joinData: '), var.get(u'joinData'))
        var.put(u'sqlJoin', Js(u''))
        var.put(u'joinKeys', var.get(u'Object').callprop(u'keys', var.get(u'joinData')))
        if (var.get(u'joinKeys').callprop(u'indexOf', Js(u'$inner'))>=Js(0.0)):
            var.put(u'sqlJoin', ((Js(u'INNER JOIN ')+var.get(u'enclosure')(var.get(u'joinData').get(u'$inner')))+Js(u' ')), u'+')
        else:
            if (var.get(u'joinKeys').callprop(u'indexOf', Js(u'$left'))>=Js(0.0)):
                var.put(u'sqlJoin', ((Js(u'LEFT JOIN ')+var.get(u'enclosure')(var.get(u'joinData').get(u'$left')))+Js(u' ')), u'+')
            else:
                if (var.get(u'joinKeys').callprop(u'indexOf', Js(u'$right'))>=Js(0.0)):
                    var.put(u'sqlJoin', ((Js(u'RIGHT JOIN ')+var.get(u'enclosure')(var.get(u'joinData').get(u'$right')))+Js(u' ')), u'+')
                else:
                    if (var.get(u'joinKeys').callprop(u'indexOf', Js(u'$full'))>=Js(0.0)):
                        var.put(u'sqlJoin', ((Js(u'FULL JOIN ')+var.get(u'enclosure')(var.get(u'joinData').get(u'$full')))+Js(u' ')), u'+')
        if (var.get(u'joinKeys').callprop(u'indexOf', Js(u'$using'))>=Js(0.0)):
            var.put(u'sqlJoin', ((Js(u'USING(')+var.get(u'enclosure')(var.get(u'joinData').get(u'$using')))+Js(u')')), u'+')
            return var.get(u'sqlJoin')
        else:
            if (var.get(u'joinKeys').callprop(u'indexOf', Js(u'$on'))>=Js(0.0)):
                if var.get(u'Array').callprop(u'isArray', var.get(u'joinData').get(u'$on')):
                    var.put(u'tempArray', Js([]))
                    @Js
                    def PyJs_anonymous_11_(item, this, arguments, var=var):
                        var = Scope({u'this':this, u'item':item, u'arguments':arguments}, var)
                        var.registers([u'item'])
                        if (var.get(u'item').get(u'$parent') and var.get(u'item').get(u'$child')):
                            var.get(u'tempArray').callprop(u'push', ((((((var.get(u'enclosure')(var.get(u'inheritedTable'))+Js(u'.'))+var.get(u'enclosure')(var.get(u'item').get(u'$parent')))+Js(u' = '))+var.get(u'enclosure')(var.get(u'curentTable')))+Js(u'.'))+var.get(u'enclosure')(var.get(u'item').get(u'$child'))))
                    PyJs_anonymous_11_._set_name(u'anonymous')
                    var.get(u'joinData').get(u'$on').callprop(u'forEach', PyJs_anonymous_11_)
                    var.put(u'sqlJoin', ((Js(u'ON (')+var.get(u'tempArray').callprop(u'join', Js(u' AND ')))+Js(u' )')), u'+')
                else:
                    if (var.get(u'joinData').get(u'$on').get(u'$parent').neg() and var.get(u'joinData').get(u'$on').get(u'$child').neg()):
                        return var.get(u"null")
                    var.put(u'sqlJoin', (((((((Js(u'ON ')+var.get(u'enclosure')(var.get(u'inheritedTable')))+Js(u'.'))+var.get(u'enclosure')(var.get(u'joinData').get(u'$on').get(u'$parent')))+Js(u' = '))+var.get(u'enclosure')(var.get(u'curentTable')))+Js(u'.'))+var.get(u'enclosure')(var.get(u'joinData').get(u'$on').get(u'$child'))), u'+')
                return var.get(u'sqlJoin')
            else:
                return var.get(u"null")
    PyJs_anonymous_10_._set_name(u'anonymous')
    var.put(u'joinBuilder', PyJs_anonymous_10_)
    @Js
    def PyJs_anonymous_12_(conditions, inheritedTable, this, arguments, var=var):
        var = Scope({u'this':this, u'inheritedTable':inheritedTable, u'conditions':conditions, u'arguments':arguments}, var)
        var.registers([u'inheritedTable', u'byGroupOrOrder', u'selectObject', u'selectKeys', u'currentTable', u'whereObject', u'conditions'])
        if var.get(u'options').get(u'debug'):
            var.get(u'console').callprop(u'log', Js(u''))
            var.get(u'console').callprop(u'log', Js(u'selectBuilder').get(u'green'))
            var.get(u'console').callprop(u'log', Js(u'  conditions: '), var.get(u'conditions'))
            var.get(u'console').callprop(u'log', Js(u'  inheritedTable: '), var.get(u'inheritedTable'))
        @Js
        def PyJs_anonymous_13_(conditions, selectObject, currentTable, this, arguments, var=var):
            var = Scope({u'this':this, u'selectObject':selectObject, u'conditions':conditions, u'arguments':arguments, u'currentTable':currentTable}, var)
            var.registers([u'selectObject', u'aliasesList', u'conditions', u'resultArray', u'currentTable'])
            @Js
            def PyJs_anonymous_14_(x, this, arguments, var=var):
                var = Scope({u'this':this, u'x':x, u'arguments':arguments}, var)
                var.registers([u'x'])
                return var.get(u'x').get(u'$as')
            PyJs_anonymous_14_._set_name(u'anonymous')
            var.put(u'aliasesList', var.get(u'selectObject').get(u'aliases').callprop(u'map', PyJs_anonymous_14_))
            var.put(u'resultArray', Js([]))
            @Js
            def PyJs_anonymous_15_(orderItem, this, arguments, var=var):
                var = Scope({u'this':this, u'orderItem':orderItem, u'arguments':arguments}, var)
                var.registers([u'orderItem', u'currentAliasIdx'])
                if PyJsStrictEq(var.get(u'orderItem',throw=False).typeof(),Js(u'object')):
                    if var.get(u'orderItem').get(u'$field'):
                        var.get(u'resultArray').callprop(u'push', (((var.get(u'enclosure')((var.get(u'orderItem').get(u'$table') if var.get(u'orderItem').get(u'$table') else var.get(u'currentTable')))+Js(u'.'))+var.get(u'enclosure')(var.get(u'orderItem').get(u'$field')))+(Js(u' DESC') if var.get(u'orderItem').get(u'$desc') else Js(u''))))
                    else:
                        if var.get(u'orderItem').get(u'$as'):
                            var.put(u'currentAliasIdx', var.get(u'aliasesList').callprop(u'indexOf', var.get(u'orderItem').get(u'$as')))
                            if (var.get(u'currentAliasIdx')>=Js(0.0)):
                                var.get(u'resultArray').callprop(u'push', (((var.get(u'enclosure')(var.get(u'selectObject').get(u'aliases').get(var.get(u'currentAliasIdx')).get(u'$table'))+Js(u'.'))+var.get(u'enclosure')(var.get(u'selectObject').get(u'aliases').get(var.get(u'currentAliasIdx')).get(u'$field')))+(Js(u' DESC') if var.get(u'orderItem').get(u'$desc') else Js(u''))))
                        else:
                            if var.get(u'orderItem').get(u'$raw'):
                                var.get(u'resultArray').callprop(u'push', var.get(u'orderItem').get(u'$raw'))
                else:
                    var.put(u'currentAliasIdx', var.get(u'aliasesList').callprop(u'indexOf', var.get(u'orderItem')))
                    if (var.get(u'currentAliasIdx')>=Js(0.0)):
                        var.get(u'resultArray').callprop(u'push', ((var.get(u'enclosure')(var.get(u'selectObject').get(u'aliases').get(var.get(u'currentAliasIdx')).get(u'$table'))+Js(u'.'))+var.get(u'enclosure')(var.get(u'selectObject').get(u'aliases').get(var.get(u'currentAliasIdx')).get(u'$field'))))
                    else:
                        var.get(u'resultArray').callprop(u'push', ((var.get(u'enclosure')(var.get(u'currentTable'))+Js(u'.'))+var.get(u'enclosure')(var.get(u'orderItem'))))
            PyJs_anonymous_15_._set_name(u'anonymous')
            var.get(u'conditions').callprop(u'forEach', PyJs_anonymous_15_)
            return var.get(u'resultArray')
        PyJs_anonymous_13_._set_name(u'anonymous')
        var.put(u'byGroupOrOrder', PyJs_anonymous_13_)
        pass
        var.put(u'selectKeys', var.get(u'Object').callprop(u'keys', var.get(u'conditions')))
        PyJs_Object_16_ = Js({u'select':Js([]),u'from':Js([]),u'aliases':Js([]),u'groupBy':Js([]),u'orderBy':Js([]),u'having':Js([])})
        var.put(u'selectObject', PyJs_Object_16_)
        if (var.get(u'selectKeys').callprop(u'indexOf', Js(u'$from'))>=Js(0.0)):
            var.put(u'currentTable', var.get(u'conditions').get(u'$from'))
            var.get(u'selectObject').get(u'from').callprop(u'push', (Js(u'FROM ')+var.get(u'enclosure')(var.get(u'currentTable'))))
        if (var.get(u'selectKeys').callprop(u'indexOf', Js(u'$inner'))>=Js(0.0)):
            var.put(u'currentTable', var.get(u'conditions').get(u'$inner'))
            var.get(u'selectObject').get(u'from').callprop(u'push', var.get(u'joinBuilder')(var.get(u'conditions'), var.get(u'currentTable'), var.get(u'inheritedTable')))
        else:
            if (var.get(u'selectKeys').callprop(u'indexOf', Js(u'$left'))>=Js(0.0)):
                var.put(u'currentTable', var.get(u'conditions').get(u'$left'))
                var.get(u'selectObject').get(u'from').callprop(u'push', var.get(u'joinBuilder')(var.get(u'conditions'), var.get(u'currentTable'), var.get(u'inheritedTable')))
            else:
                if (var.get(u'selectKeys').callprop(u'indexOf', Js(u'$right'))>=Js(0.0)):
                    var.put(u'currentTable', var.get(u'conditions').get(u'$right'))
                    var.get(u'selectObject').get(u'from').callprop(u'push', var.get(u'joinBuilder')(var.get(u'conditions'), var.get(u'currentTable'), var.get(u'inheritedTable')))
                else:
                    if (var.get(u'selectKeys').callprop(u'indexOf', Js(u'$full'))>=Js(0.0)):
                        var.put(u'currentTable', var.get(u'conditions').get(u'$full'))
                        var.get(u'selectObject').get(u'from').callprop(u'push', var.get(u'joinBuilder')(var.get(u'conditions'), var.get(u'currentTable'), var.get(u'inheritedTable')))
        if (var.get(u'selectKeys').callprop(u'indexOf', Js(u'$where'))>=Js(0.0)):
            if (var.get(u'Object').callprop(u'keys', var.get(u'conditions').get(u'$where')).get(u'length')>Js(0.0)):
                var.put(u'whereObject', var.get(u'whereBuilder')(var.get(u'conditions').get(u'$where'), var.get(u"null"), var.get(u'currentTable')))
                if var.get(u'whereObject'):
                    var.get(u'selectObject').put(u'where', var.get(u'whereObject'))
        if (var.get(u'selectKeys').callprop(u'indexOf', Js(u'$having'))>=Js(0.0)):
            if (var.get(u'Object').callprop(u'keys', var.get(u'conditions').get(u'$having')).get(u'length')>Js(0.0)):
                var.put(u'whereObject', var.get(u'whereBuilder')(var.get(u'conditions').get(u'$having'), var.get(u"null"), var.get(u'currentTable')))
                if var.get(u'whereObject'):
                    var.get(u'selectObject').put(u'having', var.get(u'whereObject'))
        if (var.get(u'conditions').get(u'$fields') and (var.get(u'conditions').get(u'$fields').get(u'length')>Js(0.0))):
            @Js
            def PyJs_anonymous_17_(field, this, arguments, var=var):
                var = Scope({u'this':this, u'field':field, u'arguments':arguments}, var)
                var.registers([u'fieldKeys', u'recursiveSelectObject', u'field', u'currentField'])
                if PyJsStrictEq(var.get(u'field',throw=False).typeof(),Js(u'object')):
                    var.put(u'fieldKeys', var.get(u'Object').callprop(u'keys', var.get(u'field')))
                    if ((((var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$inner'))>=Js(0.0)) or (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$left'))>=Js(0.0))) or (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$right'))>=Js(0.0))) or (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$full'))>=Js(0.0))):
                        var.put(u'recursiveSelectObject', var.get(u'selectBuilder')(var.get(u'field'), var.get(u'currentTable')))
                        @Js
                        def PyJs_anonymous_18_(item, this, arguments, var=var):
                            var = Scope({u'this':this, u'item':item, u'arguments':arguments}, var)
                            var.registers([u'item'])
                            var.get(u'selectObject').get(u'select').callprop(u'push', var.get(u'item'))
                        PyJs_anonymous_18_._set_name(u'anonymous')
                        var.get(u'recursiveSelectObject').get(u'select').callprop(u'forEach', PyJs_anonymous_18_)
                        @Js
                        def PyJs_anonymous_19_(item, this, arguments, var=var):
                            var = Scope({u'this':this, u'item':item, u'arguments':arguments}, var)
                            var.registers([u'item'])
                            var.get(u'selectObject').get(u'from').callprop(u'push', var.get(u'item'))
                        PyJs_anonymous_19_._set_name(u'anonymous')
                        var.get(u'recursiveSelectObject').get(u'from').callprop(u'forEach', PyJs_anonymous_19_)
                        if var.get(u'recursiveSelectObject').get(u'where'):
                            if var.get(u'selectObject').get(u'where'):
                                var.get(u'selectObject').put(u'where', (Js(u' AND ')+var.get(u'recursiveSelectObject').get(u'where')), u'+')
                            else:
                                var.get(u'selectObject').put(u'where', var.get(u'recursiveSelectObject').get(u'where'))
                        @Js
                        def PyJs_anonymous_20_(item, this, arguments, var=var):
                            var = Scope({u'this':this, u'item':item, u'arguments':arguments}, var)
                            var.registers([u'item'])
                            var.get(u'selectObject').get(u'aliases').callprop(u'push', var.get(u'item'))
                        PyJs_anonymous_20_._set_name(u'anonymous')
                        var.get(u'recursiveSelectObject').get(u'aliases').callprop(u'forEach', PyJs_anonymous_20_)
                    else:
                        if (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$field'))>=Js(0.0)):
                            PyJs_Object_21_ = Js({})
                            var.put(u'currentField', PyJs_Object_21_)
                            if (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$table'))>=Js(0.0)):
                                var.get(u'currentField').put(u'sql', ((var.get(u'enclosure')(var.get(u'field').get(u'$table'))+Js(u'.'))+var.get(u'enclosure')(var.get(u'field').get(u'$field'))))
                            else:
                                var.get(u'currentField').put(u'sql', ((var.get(u'enclosure')(var.get(u'currentTable'))+Js(u'.'))+var.get(u'enclosure')(var.get(u'field').get(u'$field'))))
                            if (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$avg'))>=Js(0.0)):
                                var.get(u'currentField').put(u'sql', ((Js(u'AVG(')+var.get(u'currentField').get(u'sql'))+Js(u')')))
                            else:
                                if (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$count'))>=Js(0.0)):
                                    var.get(u'currentField').put(u'sql', ((Js(u'COUNT(')+var.get(u'currentField').get(u'sql'))+Js(u')')))
                                else:
                                    if (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$dateFormat'))>=Js(0.0)):
                                        var.get(u'currentField').put(u'sql', ((((Js(u'DATE_FORMAT(')+var.get(u'currentField').get(u'sql'))+Js(u",'"))+var.get(u'field').get(u'$dateFormat'))+Js(u"')")))
                                    else:
                                        if (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$groupConcat'))>=Js(0.0)):
                                            var.get(u'currentField').put(u'sql', ((Js(u'GROUP_CONCAT(')+var.get(u'currentField').get(u'sql'))+Js(u')')))
                                        else:
                                            if (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$lower'))>=Js(0.0)):
                                                var.get(u'currentField').put(u'sql', ((Js(u'LOWER(')+var.get(u'currentField').get(u'sql'))+Js(u')')))
                                            else:
                                                if (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$max'))>=Js(0.0)):
                                                    var.get(u'currentField').put(u'sql', ((Js(u'MAX(')+var.get(u'currentField').get(u'sql'))+Js(u')')))
                                                else:
                                                    if (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$min'))>=Js(0.0)):
                                                        var.get(u'currentField').put(u'sql', ((Js(u'MIN(')+var.get(u'currentField').get(u'sql'))+Js(u')')))
                                                    else:
                                                        if (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$sum'))>=Js(0.0)):
                                                            var.get(u'currentField').put(u'sql', ((Js(u'SUM(')+var.get(u'currentField').get(u'sql'))+Js(u')')))
                                                        else:
                                                            if (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$upper'))>=Js(0.0)):
                                                                var.get(u'currentField').put(u'sql', ((Js(u'UPPER(')+var.get(u'currentField').get(u'sql'))+Js(u')')))
                            if (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$function'))>=Js(0.0)):
                                if ((var.get(u'field').get(u'$function').typeof()==Js(u'string')) and (var.get(u'field').get(u'$function').get(u'length')>Js(0.0))):
                                    var.get(u'currentField').put(u'function', var.get(u'field').get(u'$function').callprop(u'toUpperCase'))
                                    var.get(u'currentField').put(u'sql', (((var.get(u'currentField').get(u'function')+Js(u'('))+var.get(u'currentField').get(u'sql'))+Js(u')')))
                            if (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$as'))>=Js(0.0)):
                                var.get(u'currentField').put(u'as', var.get(u'field').get(u'$as'))
                                var.get(u'currentField').put(u'sql', ((var.get(u'currentField').get(u'sql')+Js(u' AS '))+var.get(u'currentField').get(u'as')))
                                PyJs_Object_22_ = Js({u'$table':var.get(u'currentTable'),u'$field':var.get(u'field').get(u'$field'),u'$as':var.get(u'field').get(u'$as')})
                                var.get(u'selectObject').get(u'aliases').callprop(u'push', PyJs_Object_22_)
                            var.get(u'selectObject').get(u'select').callprop(u'push', var.get(u'currentField').get(u'sql'))
                        else:
                            if (var.get(u'fieldKeys').callprop(u'indexOf', Js(u'$raw'))>=Js(0.0)):
                                var.get(u'selectObject').get(u'select').callprop(u'push', var.get(u'field').get(u'$raw'))
                else:
                    var.get(u'selectObject').get(u'select').callprop(u'push', ((var.get(u'enclosure')(var.get(u'currentTable'))+Js(u'.'))+var.get(u'enclosure')(var.get(u'field'))))
            PyJs_anonymous_17_._set_name(u'anonymous')
            var.get(u'conditions').get(u'$fields').callprop(u'forEach', PyJs_anonymous_17_)
        if (var.get(u'selectKeys').callprop(u'indexOf', Js(u'$limit'))>=Js(0.0)):
            if ((var.get(u'conditions').get(u'$limit').get(u'$offset')>=Js(0.0)) and (var.get(u'conditions').get(u'$limit').get(u'$rows')>=Js(0.0))):
                if var.get(u'options').get(u'pgSQL'):
                    var.get(u'selectObject').put(u'limit', (((Js(u' LIMIT ')+var.get(u'conditions').get(u'$limit').get(u'$rows'))+Js(u' OFFSET '))+var.get(u'conditions').get(u'$limit').get(u'$offset')))
                else:
                    if var.get(u'options').get(u'prestoDB'):
                        var.get(u'selectObject').put(u'limit', (Js(u' LIMIT ')+var.get(u'conditions').get(u'$limit').get(u'$rows')))
                    else:
                        var.get(u'selectObject').put(u'limit', (((Js(u' LIMIT ')+var.get(u'conditions').get(u'$limit').get(u'$offset'))+Js(u','))+var.get(u'conditions').get(u'$limit').get(u'$rows')))
        if (var.get(u'selectKeys').callprop(u'indexOf', Js(u'$group'))>=Js(0.0)):
            var.get(u'selectObject').put(u'groupBy', var.get(u'byGroupOrOrder')(var.get(u'conditions').get(u'$group'), var.get(u'selectObject'), var.get(u'currentTable')))
        if (var.get(u'selectKeys').callprop(u'indexOf', Js(u'$order'))>=Js(0.0)):
            var.get(u'selectObject').put(u'orderBy', var.get(u'byGroupOrOrder')(var.get(u'conditions').get(u'$order'), var.get(u'selectObject'), var.get(u'currentTable')))
        return var.get(u'selectObject')
    PyJs_anonymous_12_._set_name(u'anonymous')
    var.put(u'selectBuilder', PyJs_anonymous_12_)
    @Js
    def PyJs_anonymous_23_(queryParams, this, arguments, var=var):
        var = Scope({u'this':this, u'queryParams':queryParams, u'arguments':arguments}, var)
        var.registers([u'setKeys', u'queryParams', u'setArray', u'sql'])
        if ((var.get(u'queryParams').neg() or var.get(u'queryParams').get(u'$update').neg()) or var.get(u'queryParams').get(u'$set').neg()):
            return var.get(u"null")
        var.put(u'sql', (Js(u'UPDATE ')+var.get(u'enclosure')(var.get(u'queryParams').get(u'$update'))))
        var.put(u'setKeys', var.get(u'Object').callprop(u'keys', var.get(u'queryParams').get(u'$set')))
        var.put(u'setArray', Js([]))
        @Js
        def PyJs_anonymous_24_(key, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'key':key}, var)
            var.registers([u'key'])
            var.get(u'setArray').callprop(u'push', ((var.get(u'enclosure')(var.get(u'key'))+Js(u' = '))+var.get(u'escaping')(var.get(u'queryParams').get(u'$set').get(var.get(u'key')))))
        PyJs_anonymous_24_._set_name(u'anonymous')
        var.get(u'setKeys').callprop(u'forEach', PyJs_anonymous_24_)
        var.put(u'sql', (Js(u' SET ')+var.get(u'setArray').callprop(u'join', Js(u','))), u'+')
        if var.get(u'queryParams').get(u'$where'):
            var.put(u'sql', (Js(u' WHERE ')+var.get(u'whereBuilder')(var.get(u'queryParams').get(u'$where'), var.get(u"null"))), u'+')
        if (var.get(u'options').get(u'debug') or var.get(u'options').get(u'showSQL')):
            var.get(u'console').callprop(u'log', var.get(u'colors').callprop(u'cyan', Js(u'%s')), var.get(u'sql'))
        return var.get(u'sql')
    PyJs_anonymous_23_._set_name(u'anonymous')
    var.get(u"this").put(u'update', PyJs_anonymous_23_)
    @Js
    def PyJs_anonymous_25_(queryParams, this, arguments, var=var):
        var = Scope({u'this':this, u'queryParams':queryParams, u'arguments':arguments}, var)
        var.registers([u'keysArray', u'setKeys', u'queryParams', u'valuesArray', u'sql'])
        if ((var.get(u'queryParams').neg() or var.get(u'queryParams').get(u'$insert').neg()) or var.get(u'queryParams').get(u'$values').neg()):
            return var.get(u"null")
        var.put(u'sql', (Js(u'INSERT INTO ')+var.get(u'enclosure')(var.get(u'queryParams').get(u'$insert'))))
        var.put(u'setKeys', var.get(u'Object').callprop(u'keys', var.get(u'queryParams').get(u'$values')))
        var.put(u'keysArray', Js([]))
        @Js
        def PyJs_anonymous_26_(key, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'key':key}, var)
            var.registers([u'key'])
            var.get(u'keysArray').callprop(u'push', var.get(u'enclosure')(var.get(u'key')))
        PyJs_anonymous_26_._set_name(u'anonymous')
        var.get(u'setKeys').callprop(u'forEach', PyJs_anonymous_26_)
        var.put(u'sql', ((Js(u' (')+var.get(u'keysArray').callprop(u'join', Js(u',')))+Js(u')')), u'+')
        var.put(u'valuesArray', Js([]))
        @Js
        def PyJs_anonymous_27_(key, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'key':key}, var)
            var.registers([u'key'])
            var.get(u'valuesArray').callprop(u'push', var.get(u'escaping')(var.get(u'queryParams').get(u'$values').get(var.get(u'key'))))
        PyJs_anonymous_27_._set_name(u'anonymous')
        var.get(u'setKeys').callprop(u'forEach', PyJs_anonymous_27_)
        var.put(u'sql', ((Js(u' VALUES (')+var.get(u'valuesArray').callprop(u'join', Js(u',')))+Js(u')')), u'+')
        if (var.get(u'options').get(u'debug') or var.get(u'options').get(u'showSQL')):
            var.get(u'console').callprop(u'log', Js(u' '))
            var.get(u'console').callprop(u'log', var.get(u'colors').callprop(u'cyan', Js(u'%s')), var.get(u'sql'))
        return var.get(u'sql')
    PyJs_anonymous_25_._set_name(u'anonymous')
    var.get(u"this").put(u'insert', PyJs_anonymous_25_)
    @Js
    def PyJs_anonymous_28_(queryParams, this, arguments, var=var):
        var = Scope({u'this':this, u'queryParams':queryParams, u'arguments':arguments}, var)
        var.registers([u'queryParams', u'sql'])
        if (var.get(u'queryParams').neg() or var.get(u'queryParams').get(u'$delete').neg()):
            return var.get(u"null")
        var.put(u'sql', (Js(u'DELETE FROM ')+var.get(u'enclosure')(var.get(u'queryParams').get(u'$delete'))))
        if var.get(u'queryParams').get(u'$where'):
            var.put(u'sql', (Js(u' WHERE ')+var.get(u'whereBuilder')(var.get(u'queryParams').get(u'$where'), var.get(u"null"))), u'+')
        if (var.get(u'options').get(u'debug') or var.get(u'options').get(u'showSQL')):
            var.get(u'console').callprop(u'log', Js(u' '))
            var.get(u'console').callprop(u'log', var.get(u'colors').callprop(u'cyan', Js(u'%s')), var.get(u'sql'))
        return var.get(u'sql')
    PyJs_anonymous_28_._set_name(u'anonymous')
    var.get(u"this").put(u'delete', PyJs_anonymous_28_)
    @Js
    def PyJs_anonymous_29_(queryParams, this, arguments, var=var):
        var = Scope({u'this':this, u'queryParams':queryParams, u'arguments':arguments}, var)
        var.registers([u'selectObject', u'queryParams', u'sql'])
        if (var.get(u'queryParams').neg() or var.get(u'queryParams').get(u'$from').neg()):
            return var.get(u"null")
        var.put(u'sql', Js(u''))
        var.put(u'selectObject', var.get(u'selectBuilder')(var.get(u'queryParams'), var.get(u"null")))
        if ((var.get(u'selectObject').get(u'select').get(u'length')==Js(0.0)) or (var.get(u'selectObject').get(u'from').get(u'length')==Js(0.0))):
            return var.get(u"null")
        var.put(u'sql', Js(u'SELECT'), u'+')
        if (var.get(u'queryParams').get(u'$sqlCalcFoundRows') and var.get(u'queryParams').get(u'$limit')):
            var.put(u'sql', Js(u' SQL_CALC_FOUND_ROWS'), u'+')
        if (var.get(u'selectObject').get(u'select').get(u'length')>Js(0.0)):
            var.put(u'sql', (Js(u' ')+var.get(u'selectObject').get(u'select').callprop(u'join', Js(u', '))), u'+')
        if (var.get(u'selectObject').get(u'from').get(u'length')>Js(0.0)):
            var.put(u'sql', (Js(u' ')+var.get(u'selectObject').get(u'from').callprop(u'join', Js(u' '))), u'+')
        if var.get(u'selectObject').get(u'where'):
            var.put(u'sql', (Js(u' WHERE ')+var.get(u'selectObject').get(u'where')), u'+')
        if (var.get(u'selectObject').get(u'groupBy').get(u'length')>Js(0.0)):
            var.put(u'sql', (Js(u' GROUP BY ')+var.get(u'selectObject').get(u'groupBy').callprop(u'join', Js(u' ,'))), u'+')
        if (var.get(u'selectObject').get(u'orderBy').get(u'length')>Js(0.0)):
            var.put(u'sql', (Js(u' ORDER BY ')+var.get(u'selectObject').get(u'orderBy').callprop(u'join', Js(u' ,'))), u'+')
        if (var.get(u'selectObject').get(u'having').get(u'length')>Js(0.0)):
            var.put(u'sql', (Js(u' HAVING ')+var.get(u'selectObject').get(u'having')), u'+')
        if var.get(u'selectObject').get(u'limit'):
            var.put(u'sql', var.get(u'selectObject').get(u'limit'), u'+')
        if (var.get(u'options').get(u'debug') or var.get(u'options').get(u'showSQL')):
            var.get(u'console').callprop(u'log', Js(u' '))
            var.get(u'console').callprop(u'log', var.get(u'colors').callprop(u'cyan', Js(u'%s')), var.get(u'sql'))
        return var.get(u'sql')
    PyJs_anonymous_29_._set_name(u'anonymous')
    var.get(u"this").put(u'select', PyJs_anonymous_29_)
PyJs_anonymous_0_._set_name(u'anonymous')
var.put(u'sqlJsonGenerator', PyJs_anonymous_0_)
var.get(u'module').put(u'exports', var.get(u'sqlJsonGenerator'))
pass
