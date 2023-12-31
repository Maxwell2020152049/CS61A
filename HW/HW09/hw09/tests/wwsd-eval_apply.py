test = {
  'name': 'eval-calls',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '6',
          'choices': [
            '1',
            '2',
            '5',
            '6',
            '7',
            '8'
          ],
          'hidden': False,
          'locked': False,
          'question': 'How many calls are made to scheme_eval to evaluate the expression: (+ 2 4 6 8) ?'
        },
        {
          'answer': '1',
          'choices': [
            '1',
            '2',
            '5',
            '6',
            '7',
            '8'
          ],
          'hidden': False,
          'locked': False,
          'question': 'How many calls are made to scheme_apply: (+ 2 4 6 8) ?'
        },
        {
          'answer': '10',
          'choices': [
            '3',
            '7',
            '8',
            '9',
            '10',
            '13'
          ],
          'hidden': False,
          'locked': False,
          'question': 'How many calls are made to scheme_eval: (+ 2 (* 4 (- 6 8))) ?'
        },
        {
          'answer': '3',
          'choices': [
            '3',
            '7',
            '8',
            '9',
            '10',
            '13'
          ],
          'hidden': False,
          'locked': False,
          'question': 'How many calls are made to scheme_apply: (+ 2 (* 4 (- 6 8))) ?'
        },
        {
          'answer': '6',
          'choices': [
            '1',
            '2',
            '4',
            '6',
            '8',
            '10'
          ],
          'hidden': False,
          'locked': False,
          'question': 'How many calls are made to scheme_eval: (if #f (+ 2 3) (+ 1 2)) ?'
        },
        {
          'answer': '1',
          'choices': [
            '1',
            '2',
            '4',
            '6',
            '8',
            '10'
          ],
          'hidden': False,
          'locked': False,
          'question': 'How many calls are made to scheme_apply: (if #f (+ 2 3) (+ 1 2)) ?'
        },
        {
          'answer': '1',
          'choices': [
            '0',
            '1',
            '3',
            '7',
            '8',
            '9'
          ],
          'hidden': False,
          'locked': False,
          'question': 'How many calls are made to scheme_eval: (define (cube a) (* a a a)) ?'
        },
        {
          'answer': '023f53b43f605b7580be5aa5c3e5ee7e',
          'choices': [
            '0',
            '1',
            '3',
            '7',
            '8',
            '9'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How many calls are made to scheme_apply: (define (cube a) (* a a a)) ?'
        },
        {
          'answer': '5ccd251f8efaf1413d8d9a6429728bd6',
          'choices': [
            '2',
            '3',
            '7',
            '8',
            '9',
            '11'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How many calls are made to scheme_eval: (cube 3) ?'
        },
        {
          'answer': '3940351fe1ecdc23ea60a8fdad9aa11d',
          'choices': [
            '2',
            '3',
            '7',
            '8',
            '9',
            '11'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How many calls are made to scheme_apply: (cube 3) ?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
