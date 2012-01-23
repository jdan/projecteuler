#lang racket

(define (prime-factorization n)
  (pf-helper 2 n))

(define (pf-helper curr n)
  (if (= n 1)
      '()
      (if (= 0 (modulo n curr))
          (cons curr (pf-helper 2 (/ n curr)))
          (pf-helper (+ curr 1) n))))

(define (euler3 n)
  (car (reverse (prime-factorization n))))

(euler3 600851475143)