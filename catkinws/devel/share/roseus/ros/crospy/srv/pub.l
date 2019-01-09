;; Auto-generated. Do not edit!


(when (boundp 'crospy::pub)
  (if (not (find-package "CROSPY"))
    (make-package "CROSPY"))
  (shadow 'pub (find-package "CROSPY")))
(unless (find-package "CROSPY::PUB")
  (make-package "CROSPY::PUB"))
(unless (find-package "CROSPY::PUBREQUEST")
  (make-package "CROSPY::PUBREQUEST"))
(unless (find-package "CROSPY::PUBRESPONSE")
  (make-package "CROSPY::PUBRESPONSE"))

(in-package "ROS")





(defclass crospy::pubRequest
  :super ros::object
  :slots (_type _layer ))

(defmethod crospy::pubRequest
  (:init
   (&key
    ((:type __type) "")
    ((:layer __layer) "")
    )
   (send-super :init)
   (setq _type (string __type))
   (setq _layer (string __layer))
   self)
  (:type
   (&optional __type)
   (if __type (setq _type __type)) _type)
  (:layer
   (&optional __layer)
   (if __layer (setq _layer __layer)) _layer)
  (:serialization-length
   ()
   (+
    ;; string _type
    4 (length _type)
    ;; string _layer
    4 (length _layer)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _type
       (write-long (length _type) s) (princ _type s)
     ;; string _layer
       (write-long (length _layer) s) (princ _layer s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _type
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _type (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _layer
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _layer (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass crospy::pubResponse
  :super ros::object
  :slots (_ret ))

(defmethod crospy::pubResponse
  (:init
   (&key
    ((:ret __ret) 0)
    )
   (send-super :init)
   (setq _ret (round __ret))
   self)
  (:ret
   (&optional __ret)
   (if __ret (setq _ret __ret)) _ret)
  (:serialization-length
   ()
   (+
    ;; int64 _ret
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _ret
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _ret (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _ret) (= (length (_ret . bv)) 2)) ;; bignum
              (write-long (ash (elt (_ret . bv) 0) 0) s)
              (write-long (ash (elt (_ret . bv) 1) -1) s))
             ((and (class _ret) (= (length (_ret . bv)) 1)) ;; big1
              (write-long (elt (_ret . bv) 0) s)
              (write-long (if (>= _ret 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _ret s)(write-long (if (>= _ret 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _ret
#+(or :alpha :irix6 :x86_64)
      (setf _ret (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _ret (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass crospy::pub
  :super ros::object
  :slots ())

(setf (get crospy::pub :md5sum-) "f9f9aa5fef081d148fcc68ac90f825a1")
(setf (get crospy::pub :datatype-) "crospy/pub")
(setf (get crospy::pub :request) crospy::pubRequest)
(setf (get crospy::pub :response) crospy::pubResponse)

(defmethod crospy::pubRequest
  (:response () (instance crospy::pubResponse :init)))

(setf (get crospy::pubRequest :md5sum-) "f9f9aa5fef081d148fcc68ac90f825a1")
(setf (get crospy::pubRequest :datatype-) "crospy/pubRequest")
(setf (get crospy::pubRequest :definition-)
      "string type
string layer
---
int64 ret

")

(setf (get crospy::pubResponse :md5sum-) "f9f9aa5fef081d148fcc68ac90f825a1")
(setf (get crospy::pubResponse :datatype-) "crospy/pubResponse")
(setf (get crospy::pubResponse :definition-)
      "string type
string layer
---
int64 ret

")



(provide :crospy/pub "f9f9aa5fef081d148fcc68ac90f825a1")


