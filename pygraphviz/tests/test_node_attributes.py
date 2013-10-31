# -*- coding: utf-8 -*-
from nose.tools import *
import pygraphviz as pgv

def test_node_attribute():
    A = pgv.AGraph()
    A.add_node(1,label='test',spam='eggs')
    assert_equal(A.string().expandtabs(2),
"""strict graph {
  node [label="\N"];
  1  [label=test,
    spam=eggs];
}
""")

def test_node_attributes2():
    A = pgv.AGraph()
    A.add_node(1)
    one = A.get_node(1)
    one.attr['label'] = 'test'
    one.attr['spam'] = 'eggs'
    assert_true('label' in one.attr)
    assert_equal(one.attr['label'],u'test')
    assert_equal(sorted(one.attr.keys()), [u'label', u'spam'])
    assert_equal(A.string().expandtabs(2),
"""strict graph {
  node [label="\N"];
  1  [label=test,
    spam=eggs];
}
"""
)
    one.attr['label'] = ''
    one.attr['spam'] = ''
    assert_equal(A.string().expandtabs(2),
"""strict graph {
  node [label="\N"];
  1  [label=""];
}
""")
    one.attr['label'] = 'test'
    del one.attr['label']
    assert_equal(A.string().expandtabs(2),
"""strict graph {
  node [label="\N"];
  1  [label=""];
}
""")
