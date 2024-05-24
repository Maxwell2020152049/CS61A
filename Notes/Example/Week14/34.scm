;; list-tail

(define (list-tail lst k)
  (if (zero? k)
      lst
      (list-tail (cdr lst) (- k 1))))

;; list-ref

(define (list-ref lst k)
  (car (list-tail lst (- k 1))))

;; Array Trees: Primitive Representation

; Accessors for the Array data structure.  Each node has the structure
;   (ELEMENT-INDEX ELEMENT-VALUE SMALLER-INDICES LARGER-INDICES)
(define (arr-index arr) (car arr))
(define (arr-value arr) (car (cdr arr)))
(define (arr-left arr) (car (cdr (cdr arr))))
(define (arr-right arr) (car (cdr (cdr (cdr arr)))))
(define (arr-make index value left right)
  (list index value left right))
(define arr-empty nil)
  

;; Array Trees: Accessing

; Returns element with index K in ARR. 
(define (get arr k)
  (cond ((eq? arr arr-empty) arr-empty)
        ((< k (arr-index arr)) (get (arr-left arr) k))
        ((> k (car arr)) (get (arr-right arr) k))
        (else (arr-value arr))))

;; Array Trees: Building

(define (list-to-array lst)
  (define (part-list-to-array L N k)
    (cond ((= N 0) arr-empty)
          ((= N 1) (arr-make k (car L) arr-empty arr-empty))
          (else (let ((N2 (quotient N 2))
                      (mid (list-tail L (quotient N 2))))
                  (arr-make (+ k N2) (car mid)
                            (part-list-to-array L N2 k)
                            (part-list-to-array
                             (cdr mid) (- N N2 1) (+ k N2 1)))))))
  (part-list-to-array lst (length lst) 0))


;; Encapsulating an Array Tree as a Function.

(define (make-array-tree L)
  (let ((data (list-to-array L)))
    (define (A k) (get data k))
    A))


;; let* macro

(define-macro (let* clauses body)
  (define (make-let C)
    (if (null? C) body
        `(let (,(car C)) ,(make-let (cdr C)))))
  (make-let clauses))





