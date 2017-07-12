# https://github.com/jtauber/Rel
#
# http://jtauber.com/relational_python/
#
# http://jtauber.com/blog/2005/11/09/relational_python/
# http://jtauber.com/blog/2005/11/10/relational_python:_basic_class_for_relations/
# http://jtauber.com/blog/2005/11/11/relational_python:_displaying_relations/
# http://jtauber.com/blog/2005/11/17/relational_python:_projection/
# http://jtauber.com/blog/2005/11/30/relational_python:_restrict/
#
# http://jtauber.com/blog/2005/05/26/finding_dependencies_in_tabular_data/
# http://jtauber.com/blog/2005/05/27/finding_dependencies_in_tabular_data,_part_2/
#
#
# ==================================================================================
# Check also: http://jtauber.com/blog/2008/11/21/relations_with_python_named_tuples/
# ==================================================================================


class Rel:
    def __init__(self, attributes):
        self.attributes_ = tuple(attributes)
        self.tuples_ = set()

    def add(self, tup):
        self.tuples_.add(self._convert_dict(tup))

    def _convert_dict(self, tup):
        return tuple([tup[attribute] for attribute in self.attributes_])

    # Note that Rel.attributes and Rel.tuples return a set of attributes and a generator over dictionaries
    # just as you would expect
    def attributes(self):
        return set(self.attributes_)

    def tuples(self):
        for tup in self.tuples_:
            tupdict = {}
            for col in range(len(self.attributes_)):
                tupdict[self.attributes_[col]] = tup[col]
            yield tupdict

    def display(self):
        columns = range(len(self.attributes_))

        col_width = [len(self.attributes_[col]) for col in columns]

        for tupdict in self.tuples():
            tup = self._convert_dict(tupdict)
            for col in columns:
                col_width[col] = max(col_width[col], len(tup[col]))

        hline = ""
        for col in columns:
            hline += "+-" + ("-" * col_width[col]) + "-"
        hline += "+"

        def line(row):
            l = ""
            for col in columns:
                value = row[col]
                l += "| " + value + (" " * (col_width[col] - len(value))) + " "
            l += "|"
            return l

        print(hline)
        print(line(self.attributes_))
        print(hline)

        for tup in self.tuples():
            print(line(self._convert_dict(tup)))

        print(hline)


# By implementing the handy little helper function:
def d(**args):
    return args


# we can now create a relation and add tuples like so:
rel1 = Rel(["ENO", "ENAME", "DNO", "SALARY"])

rel1.add(d(ENO="E1", ENAME="Lopez", DNO="D1", SALARY="40K"))
rel1.add(d(ENO="E2", ENAME="Cheng", DNO="D1", SALARY="42K"))
rel1.add(d(ENO="E3", ENAME="Finzi", DNO="D2", SALARY="30K"))

# It's a class 'set'
print(rel1.attributes())

# print(next(rel1.tuples()))
for rel in rel1.tuples():
    print(rel['ENAME'])

rel1.display()
