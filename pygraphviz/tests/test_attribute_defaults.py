# -*- coding: utf-8 -*-
from nose.tools import *
import pygraphviz as pgv

def test_default_attributes():
    A = pgv.AGraph()
    A.graph_attr['label'] = 'test'
    A.graph_attr['spam'] = 'eggs'
    assert_true('label' in A.graph_attr)
    assert_equal(A.graph_attr['label'], u'test')
    assert_equal(A.graph_attr.keys(), [u'label', u'spam'])
    assert_equal(sorted(list(A.graph_attr.iteritems())),
                 [(u'label', u'test'), (u'spam', u'eggs')])
    assert_equal(A.string().expandtabs(2),
"""strict graph {
  graph [label=test,
    spam=eggs
  ];
}
""")

    A.graph_attr['label'] = ''
    A.graph_attr['spam'] = ''

    assert_equal(A.string().expandtabs(2),
"""strict graph {
}
""")

    A.graph_attr['label'] = 'test'
    del A.graph_attr['label']
    assert_equal(A.string().expandtabs(2),
"""strict graph {
}
"""
)
def test_graph_defaults():
    A = pgv. AGraph(rankdir='LR',pack='true')
    assert_equal(A.string().expandtabs(2),
"""strict graph {
  graph [pack=true,
    rankdir=LR
  ];
}
""")


def test_node_defaults():
    A = pgv.AGraph()
    A.node_attr['label']='test'
    assert_true('label' in A.node_attr)
    assert_equal(A.node_attr['label'], u'test')
    assert_equal(A.node_attr.keys(), [u'label'])
    assert_equal(A.node_attr, {u'label': u'test'})
    assert_equal(list(A.node_attr.iteritems()), [(u'label', u'test')])
    assert_equal(A.string().expandtabs(2),
"""strict graph {
  node [label=test];
}
"""
)
    A.node_attr['label'] = ''
    assert_true(A.string().expandtabs(2),
"""strict graph {
}
"""
)

    A.node_attr['label'] = 'test'
    del A.node_attr['label']
    assert_true(A.string().expandtabs(2),
"""strict graph {
}
"""
)
    A.graph_attr['fontname'] = 'graph font'
    A.node_attr['fontname'] = 'node font'
    A.edge_attr['fontname'] = 'edge font'
    assert_equal(A.string().expandtabs(2),
"""strict graph {
  graph [fontname="graph font"];
  node [fontname="node font"];
  edge [fontname="edge font"];
}
"""
)

def test_edge_defaults():
    A = pgv.AGraph()
    A.edge_attr['label'] = 'test'
    assert_true('label' in A.edge_attr)
    assert_equal(A.edge_attr['label'], u'test')
    assert_equal(A.edge_attr.keys(), [u'label'])
    assert_equal(A.edge_attr, {u'label': u'test'})
    assert_equal(list(A.edge_attr.iteritems()), [(u'label', u'test')])
    assert_equal(A.string().expandtabs(2),
"""strict graph {
  edge [label=test];
}
"""
)
    A.edge_attr['label'] = ''
    assert_equal(A.string().expandtabs(2),
"""strict graph {
}
"""
)
    A.edge_attr['label'] = 'test'
    del A.edge_attr['label']
    assert_true(A.string().expandtabs(2),
"""strict graph {
}
""")
