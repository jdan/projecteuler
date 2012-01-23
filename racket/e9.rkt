#lang racket

;; a = m^2 - n^2
;; b = 2mn
;; c = m^2 + n^2
;;
;; m^2 - n^2 + 2mn + m^2 + n^2 = 1000
;; 2m^2 + 2mn = 1000
;; m(m+n) = 500
;; 500/m - m = n
;;
;; find integer n such that m > n

(define (find-mn limit)
  (fmn-helper (/ limit 2) 1))

(define (fmn-helper limit m)
  (if (> (* m m) limit)
      (cons m '(0))
      (let ((n (- (/ limit m) m)))
        (if (and (int? n) (> m n))
            (cons m (cons n '()))
            (fmn-helper limit (+ m 1))))))
      
(define (int? n)
  (= (floor n) n))

(define (euler9 limit)
  (let ((mn (find-mn limit)))
    (* (- (* (car mn) (car mn)) (* (cadr mn) (cadr mn)))
       (* 2 (car mn) (cadr mn))
       (+ (* (car mn) (car mn)) (* (cadr mn) (cadr mn))))))

(euler9 1000)