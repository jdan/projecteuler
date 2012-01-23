#lang racket

(define (prime-factorization n)
  (pf-helper 2 n))

(define (pf-helper curr n)
  (if (= n 1)
      '()
      (if (= 0 (modulo n curr))
          (cons curr (pf-helper 2 (/ n curr)))
          (pf-helper (+ curr 1) n))))

(define (multiply-down n curr)
  (if (< n 1)
      curr
      (multiply-down (- n 1) (md-helper (prime-factorization n) curr curr))))

(define (md-helper factors n run)
  (if (null? factors)
      run
      (if (= 0 (modulo n (car factors)))
          (md-helper (cdr factors) (/ n (car factors)) run)
          (md-helper (cdr factors) n (* run (car factors))))))

(define (euler5)
  (multiply-down 20 1))

(euler5)