#lang racket

(define (one-to-n n)
  (/ (+ (* n n) n) 2))

(define (euler1 max)
  (- (+ (* 3 (one-to-n (floor (/ (- max 1) 3)))) 
        (* 5 (one-to-n (floor (/ (- max 1) 5))))) 
     (* 15 (one-to-n (floor (/ (- max 1) 15))))))

(euler1 1000)