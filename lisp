1.FACTORIAL OF A NUMBER

(defun factorial(number)
(if (= number 0)1
(* number (factorial(- number 1)))))


2. nth element in list
(defun m(n li)
(if (zerop n)
(first li)
(m (- n 1)(rest li))))
