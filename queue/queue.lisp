;; queue class definition with
;; respective methods


(defclass queue ()
  ((list :initform nil)
   (tail :initform nil)))

(defmethod print-object ((queue queue) stream)
  (print-unreadable-object (queue stream :type t)
    (with-slots (list tail) queue
      (cond ((cddddr list)
	     ;; if at least 5 elements, print ellipsis
	     (format stream "(~{~S ~}... ~S)"
		     (subseq list 0 3) (first tail)))
	     ;; otherwise print whole list 
	    (t (format stream "~:S" list))))))

(defmethod dequeue ((queue queue))
  (with-slots (list) queue
    (pop list)))

(defmethod enqueue (new-item (queue queue))
  (with-slots (list tail) queue
    (let ((new-tail (list new-item)))
      (cond ((null list) (setf list new-tail))
	    (t (setf (cdr tail) new-tail)))
      (setf tail new-tail)))
  queue)

 
;; instantiating queue class and calling methods

(defparameter *q* (make-instance 'queue))
(print *q*)

(enqueue '(beej joregensen) *q*)
(print *q*)

(enqueue '(brady fukamoto) *q*)
(print *q*)

(enqueue '(sean chen) *q*)
(print *q*)

(dotimes (i 5 *q*)
  (enqueue i *q*))
(print *q*)


(dequeue *q*)
(print *q*)

(dequeue *q*)
(print *q*)

(dequeue *q*)
(print *q*)

(dequeue *q*)
(print *q*)

(dequeue *q*)
(print *q*)

(dequeue *q*)
(print *q*)

(dequeue *q*)
(print *q*)

(dequeue *q*)
(print *q*)



