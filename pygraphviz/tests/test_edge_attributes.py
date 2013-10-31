# -*- coding: utf-8 -*-
from nose.tools import *
import pygraphviz as pgv

def test_edge_attributes():
    A = pgv.AGraph()
    A.add_edge(1,2,label='test',spam='eggs')
    assert_equal(A.string().expandtabs(2),
"""strict graph {
  1 -- 2   [label=test,
    spam=eggs];
}
"""
)

def test_edge_attributes2():
    A = pgv.AGraph()
    A.add_edge(1,2)
    one = A.get_edge(1,2)
    one.attr['label'] = 'test'
    one.attr['spam'] = 'eggs'
    assert_true('label' in one.attr)
    assert_equal(one.attr['label'], u'test')
    assert_equal(sorted(one.attr.keys()), [u'label', u'spam'])
    assert_equal(A.string().expandtabs(2),
"""strict graph {
  1 -- 2   [label=test,
    spam=eggs];
}
"""
)
    one.attr['label'] = ''
    one.attr['spam'] = ''
    assert_equal(A.string().expandtabs(2),
"""strict graph {
  1 -- 2;
}
"""
)
    one.attr['label'] = 'test'
    del one.attr['label']
    assert_equal(A.string().expandtabs(2),
"""strict graph {
  1 -- 2;
}
"""
)

def test_anonymous_edges():
    """graph test {\n a -- b [label="edge1"];\n a -- b [label="edge2"];\n }"""
    pass
    #FIXME
# >>> import os,tempfile
# >>> (fd,fname)=tempfile.mkstemp()
# >>> fh=open(fname,'w')
# >>> fh.write(d)
# >>> fh.close()
    # A = AGraph(fname)

#    assert_equal(print A.string().expandtabs(2),
# """graph test {
#   a -- b   [label=edge1];
#   a -- b   [label=edge2];
# }
#""")
