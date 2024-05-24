(define (count predicate L)
    (cond ((null? L) 0)
          ((predicate (car L))
           (+ 1 (count predicate (cdr L))))
          (else (count predicate (cdr L))))
)
(count odd? '(1 12 13 19 4 6 9))
(count odd? '())

(define (reverse L)
    (define (reverse1 so-far L)
        (if (null? L) so-far
            (reverse1 (cons (car L) so-far) (cdr L))))
    (reverse1 '() L))

(reverse '(1 2 3))

(define (map fn L)
    (define (loop list-so-far L)
        (if (null? L) list-so-far
            (loop (append list-so-far (list (fn (car L)))) (cdr L))))
    (loop '() L))

(map - '(1 2 3))

(define (tree label children) (cons label children))
(define (label tr) (car tr))
(define (children tr) (cdr tr))
(define (is-leaf tr) (null? (cdr tr)))

(define (double tr)
     ; Return TREE but with all labels doubled.
     (tree (* (label tr) 2) (map double (children tr)))
)

(define aTree (tree 6
                    (list (tree 3 (list (tree 1 '())))
                          (tree 5 '())
                          (tree 7 (list (tree 8 '()) (tree 9 '()))))))

aTree
(double aTree)
