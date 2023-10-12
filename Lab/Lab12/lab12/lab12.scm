(define (tail-replicate x n)
  (define (tail-replicate1 x lst n)
    (cond 
      ((= n 0)
       nil
      )
      ((= n 1)
       lst
      )
      ((= (modulo n 2) 1)
       (append lst
               (tail-replicate1 x
                                (append lst lst)
                                (quotient n 2)
               )
       )
      )
      (else
       (tail-replicate1 x
                        (append lst lst)
                        (quotient n 2)
       )
      )
    )
  )
  (tail-replicate1 x (cons x nil) n)
)

(define-macro (def func args body)
  `(define (,func ,@args) ,body)
)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x))
           )
        (* y y y)
      )
  )
)
