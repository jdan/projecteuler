#lang racket

(define (digit-sum n)
  (if (zero? n)
      0
      (+ (modulo n 10) (digit-sum (floor (/ n 10))))))

(define (euler16)
  (digit-sum (expt 2 1000)))

(euler16)