#lang racket

(define (is-prime? n)
  (ip-helper n 2))

(define (ip-helper n curr)
  (if (> (* curr curr) n)
      #t
      (if (= 0 (modulo n curr))
          #f
          (ip-helper n (+ curr 1)))))

(define (nth-prime n)
  (np-helper (+ n 1) 1 2))

(define (np-helper n primes curr)
  (if (= primes n)
      (- curr 1)
      (if (is-prime? curr)
          (np-helper n (+ primes 1) (+ curr 1))
          (np-helper n primes (+ curr 1)))))

(define (euler7)
  (nth-prime 10001))

(euler7)

