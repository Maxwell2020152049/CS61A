;; Quasiquote
(list 'a 'b (+ 2 3) 'd)       ;; which produces (a b 5 d)
`(a b ,(+ 2 3) d)

(define values (list (+ 2 3) (- 2 1)))
(append '(a b) values '(d))   ;; which produces (a b 5 1 d)
`(a b ,@values d)
`(a b ,@(list (+ 2 3) (- 2 1)) d)

;; unless
(define-macro (unless cond body)
  `(if (not ,cond) ,body))
(define x 3)
(unless (list? x) (displayln x))
(unless (number? x) (displayln x))


;; for-list macro
(define-macro (for-list var expr lst)
    `(map (lambda (,var) ,expr) ,lst))
(for-list x (* x x) '(1 2 3 4 5))
(map (lambda (x) (* x x)) '(1 2 3 4 5))

;; for-range macro
(define-macro (for-range control-var low high body)
    `(let (($low$ ,low))
       (define ($loop$ $so-far$ ,control-var)
           (if (< ,control-var $low$) $so-far$
              ($loop$ (cons ,body $so-far$) (- ,control-var 1))))
       ($loop$ '() ,high)))
(for-range x 1 5 (* x x))  ;; Like [ x*x for x in range(1, 6) ]

; Expansion of (for-range x 1 5 (* x x))
(let (($low$ 1))
    (define ($loop$ $so-far$ x)
        (if (< x $low$) $so-far$
           ($loop$ (cons (* x x) $so-far$) (- x 1))))
    ($loop$ '() 5))

;; for macro
(define-macro (for list-spec body)
    (let ((control-var (car list-spec))
          (opnds (cdr list-spec)))
       (if (= (length opnds) 1)
        `(for-list ,control-var ,body ,(car opnds))
        `(for-range ,control-var ,(car opnds) ,(car (cdr opnds)) ,body))))
(for (x (list 1 2 3 4 5)) (* x x))
;(1 4 9 16 25)
(for (x 1 5) (* x x))
;(1 4 9 16 25)

;; Example of name clash
(define $low$ 15)
(for-range x 1 5 (* $low$ x))
;(1 2 3 4 5)    ;; WRONG!!

