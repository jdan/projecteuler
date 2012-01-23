#lang racket

(define (get-abc n)
  (append (list (modulo n 10))
          (list (modulo (floor (/ n 10)) 10))
          (list (modulo (floor (/ n 100)) 10))))

(define (construct ls)
  (* 11 (+ (* 9091 (car ls))
           (* 910  (cadr ls))
           (* 100  (caddr ls)))))

(define (palindrone? n)
  (= n (construct (get-abc n))))

(define (find-n x y)
  (if (< y 10)
      (find-n (- x 1) 990)
      (if (palindrone? (* x y))
          (* x y)
          (find-n x (- y 11)))))

(define (euler4)
  (find-n 999 (* 11 (floor (/ 999 11)))))

(euler4)