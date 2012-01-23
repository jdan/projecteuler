#lang racket

(define (is-prime? n)
  (ip-helper n 2))

(define (ip-helper n curr)
  (if (> (* curr curr) n)
      #t
      (if (= 0 (modulo n curr))
          #f
          (ip-helper n (+ curr 1)))))

(define (sum-of-primes max)
  (sop-helper max 3 0))

(define (sop-helper max n total)
  (if (>= n max)
      total
      (if (is-prime? n)
          (sop-helper max (+ n 2) (+ total n))
          (sop-helper max (+ n 2) total))))

(define (euler10)
  (+ (sum-of-primes 2e6) 2))

(euler10)