#lang racket

(define (is-prime? n)
  (ip-helper n 2))

(define (ip-helper n curr)
  (if (> (* curr curr) n)
      #t
      (if (= 0 (modulo n curr))
          #f
          (ip-helper n (+ curr 1)))))

(define (godel n)
  (g-helper n 2))

(define (g-helper n p)
  (if (= n 1)
      '()
      (if (is-prime? p)
        (cons (divides-into n p) 
              (g-helper (/ n 
                           (expt p (divides-into n p))) 
                        (+ p 1)))
        (g-helper n (+ p 1)))))
          
(define (divides-into n d)
  (if (> (modulo n d) 0)
      0
      (+ (divides-into (/ n d) d) 
         1)))

(define (num-divisors n)
  (nd-helper (godel n)))

(define (nd-helper pfs)
  (if (null? pfs)
      1
      (* (+ (car pfs) 1)
         (nd-helper (cdr pfs)))))

(define (triangle-number n)
  (/ (* n (+ n 1)) 2))

(define (euler12 n max)
  (if (> (num-divisors (triangle-number n)) max)
      (triangle-number n)
      (euler12 (+ n 1) max)))

(euler12 1 500)