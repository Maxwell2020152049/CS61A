(define (over-or-under num1 num2) 
    (cond
        ((< num1 num2) -1) 
        ((= num1 num2) 0) 
        (else 1)
    )
)


; ;; Tests
(over-or-under 1 2)

; expect -1
(over-or-under 2 1)

; expect 1
(over-or-under 1 1)

; expect 0
(define (make-adder num) 
    (lambda (inc)
        (+ num inc)
    )
)

; ;; Tests
(define adder (make-adder 5))

(adder 8)

; expect 13
(define (composed f g) 
    (lambda (x)
        (f (g x))
    )
)

; (define (neq item)
;     (lambda (x)
;         (not (= item x))
;     )
; )

; (define (remove item lst) 
;     (filter (neq item) lst)
; )

(define (remove item list)
    (cond
        ((eq? list nil) nil)
        ((not (= (car list) item)) (cons (car list) (remove item (cdr list))))
        (else (remove item (cdr list)))
    )
)

; ;; Tests
(remove 3 nil)

; expect ()
(remove 3 '(1 3 5))

; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))

; expect (3 1 4 4)

(define lst 
    (cons 
        (cons 1 nil)
        (cons 2
            (cons
                (cons 3 
                    (cons 4 nil)
                )
                (cons 5 nil)
            )
        )
    )
)

(define (sub-all s olds news)
  'YOUR-CODE-HERE
)