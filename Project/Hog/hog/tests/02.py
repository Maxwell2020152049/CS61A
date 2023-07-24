test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> piggy_points(4)
          edcbd82ba98a8122be244fa325c62071
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> piggy_points(10)
          16e2cf37e8254529473d9e0a36b75fcb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> piggy_points(94)
          327b19ffebddf93982e1ad2a4a6486f4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> piggy_points(0)
          16e2cf37e8254529473d9e0a36b75fcb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> a = piggy_points(24)
          >>> a # check that the value is being returned, not printed
          2aef307e1e3d3bb468f74013a49eb977
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> piggy_points(13)
          4
          >>> # ban indexing
          >>> test.check('hog.py', 'piggy_points', ['Slice', 'List', 'ListComp', 'Index', 'Subscript', 'For'])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(64)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(12)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(72)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(3)
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(439)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(61)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(99)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(25)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(54)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(15)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(80)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(74)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(12)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(12)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(69)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(15)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(69)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(98)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(15)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(56)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(44)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(40)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(192)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(90)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(72)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(34)
          4
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
