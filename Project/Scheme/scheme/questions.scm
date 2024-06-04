(define (caar x) (car (car x)))

(define (cadr x) (car (cdr x)))

(define (cdar x) (cdr (car x)))

(define (cddr x) (cdr (cdr x)))

; ; Problem 15
; ; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (func i lst)
    (cond 
      ((null? lst)
       nil)
      (else
       (cons (cons i (cons (car lst) nil))
             (func (+ i 1) (cdr lst))))))
  (func 0 s))

; END PROBLEM 15
; ; Problem 16
; ; Merge two lists LIST1 and LIST2 according to ORDERED? and return
; ; the merged lists.
(define (merge ordered? list1 list2)
  ; BEGIN PROBLEM 16
  (cond 
    ((null? list1)
     list2)
    ((null? list2)
     list1)
    (else
     (append (cond 
               ((ordered? (car list1) (car list2))
                (list (car list1) (car list2)))
               (else
                (list (car list2) (car list1))))
             (merge ordered? (cdr list1) (cdr list2))))))

; END PROBLEM 16
; ; Optional Problem
; ; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))

(define define? (check-special 'define))

(define quoted? (check-special 'quote))

(define let? (check-special 'let))

; ; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond 
    ((atom? expr)
     ; BEGIN OPTIONAL PROBLEM
     'replace-this-line
     ; END OPTIONAL PROBLEM
    )
    ((quoted? expr)
     ; BEGIN OPTIONAL PROBLEM
     'replace-this-line
     ; END OPTIONAL PROBLEM
    )
    ((or (lambda? expr) (define? expr))
     (let ((form (car expr))
           (params (cadr expr))
           (body (cddr expr)))
       ; BEGIN OPTIONAL PROBLEM
       'replace-this-line
       ; END OPTIONAL PROBLEM
     ))
    ((let? expr)
     (let ((values (cadr expr))
           (body (cddr expr)))
       ; BEGIN OPTIONAL PROBLEM
       'replace-this-line
       ; END OPTIONAL PROBLEM
     ))
    (else
     ; BEGIN OPTIONAL PROBLEM
     'replace-this-line
     ; END OPTIONAL PROBLEM
    )))

; Some utility functions that you may find useful to implement for let-to-lambda
(define (zip pairs) 'replace-this-line)
