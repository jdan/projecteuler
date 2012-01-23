#lang racket

(define (even-fibonacci-sum a b total max)
  (if (> a max)
      total
      (if (= 0 (modulo a 2))
          (even-fibonacci-sum (+ a b) a (+ total a) max)
          (even-fibonacci-sum (+ a b) a total max))))

(define (euler2 max)
  (even-fibonacci-sum 1 1 0 max))

(euler2 4e6)