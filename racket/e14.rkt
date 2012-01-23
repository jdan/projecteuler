#lang racket

(define (len-collatz n)
  (if (= n 1)
      0
      (if (= 0 (modulo n 2))
          (+ 1 (len-collatz (/ n 2)))
          (+ 1 (len-collatz (+ (* 3 n) 1))))))

(define (longest-chain limit)
  (lc-helper limit 1 1 1))

(define (lc-helper limit n max max-n)
  (if (= n limit)
      max-n
      (let ((len (len-collatz n)))
        (if (> len max)
            (lc-helper limit (+ n 1) len n)
            (lc-helper limit (+ n 1) max max-n)))))

(define (euler14 limit)
  (longest-chain limit))

(euler14 1e6)