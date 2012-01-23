#lang racket

(define (integers start end)
  (if (> start end)
      '()
      (cons start (integers (+ start 1) end))))

(define (first ls n)
  (if (= n 0)
      '()
      (cons (car ls) (first (cdr ls) (- n 1)))))

(define (last ls n)
  (reverse (first (reverse ls) n)))

(define (multiply-at n ls i)
  (if (null? ls)
      '()
      (if (= i 0)
          (cons (* n (car ls)) 
                (cdr ls))
          (cons (car ls) 
                (multiply-at n (cdr ls) (- i 1))))))

(define (index ls i)
  (if (null? ls)
      -1
      (if (= i 0)
          (car ls)
          (index (cdr ls) (- i 1)))))

; sending i = 2 will multiply index 2, 4, 6, etc.
(define (multiply-interval n ls i)
  (if (= (index ls i) i)
      (mi-helper n ls i i)
      ls))

(define (mi-helper n ls i k)
  (if (> k (length ls))
      ls
      (mi-helper n (multiply-at n ls k) i (+ k i)))) 
  
(define (sum ls)
  (if (null? ls)
      0
      (+ (car ls) (sum (cdr ls)))))

(define (totient-list n)
  (tl-helper (integers 0 n) 2))

(define (tl-helper ls n)
  (if (> n (length ls))
      ls
      (tl-helper (multiply-interval (- 1 (/ 1 n)) ls n) (+ n 1))))

(define (euler72 limit)
  (- (sum (totient-list limit)) 1))

(euler72 1e6)