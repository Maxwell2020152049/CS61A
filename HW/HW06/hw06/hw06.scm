(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (sign val)
  (cond 
    ((> val 0) 1)
    ((< val 0) -1)
    (else      0)))

(define (square x) (* x x))

(define (pow base exp)
  (cond 
    ((= exp 0)
     1)
    ((odd? exp)
     (* base (pow (square base) (quotient exp 2))))
    (else
     (* 1 (pow (square base) (quotient exp 2))))))

(define (reverse L)
  (if (null? L)
      nil
      (append (reverse (cdr L)) (cons (car L) nil))))

(define lst '(1 2 3 4))
