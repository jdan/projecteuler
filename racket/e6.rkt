#lang racket

;; using the fact that (1 + 2 + 3 + ... + n)^2 = 1^3 + 2^3 + 3^3 + ... + n^3

(define (euler6 n)
  (if (= n 1)
      0
      (+ (- (* n n n) (* n n)) (euler6 (- n 1)))))

(euler6 100)