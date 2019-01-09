;; Auto-generated. Do not edit!


(when (boundp 'crospy::sub)
  (if (not (find-package "CROSPY"))
    (make-package "CROSPY"))
  (shadow 'sub (find-package "CROSPY")))
(unless (find-package "CROSPY::SUB")
  (make-package "CROSPY::SUB"))
(unless (find-package "CROSPY::SUBREQUEST")
  (make-package "CROSPY::SUBREQUEST"))
(unless (find-package "CROSPY::SUBRESPONSE")
  (make-package "CROSPY::SUBRESPONSE"))

(in-package "ROS")





(defclass crospy::subRequest
  :super ros::object
  :slots (_client ))

(defmethod crospy::subRequest
  (:init
   (&key
    ((:client __client) "")
    )
   (send-super :init)
   (setq _client (string __client))
   self)
  (:client
   (&optional __client)
   (if __client (setq _client __client)) _client)
  (:serialization-length
   ()
   (+
    ;; string _client
    4 (length _client)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _client
       (write-long (length _client) s) (princ _client s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _client
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _client (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass crospy::subResponse
  :super ros::object
  :slots (_ret ))

(defmethod crospy::subResponse
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

(defclass crospy::sub
  :super ros::object
  :slots ())

(setf (get crospy::sub :md5sum-) "4096e8e9f96b81072bcc1faf81a24d83")
(setf (get crospy::sub :datatype-) "crospy/sub")
(setf (get crospy::sub :request) crospy::subRequest)
(setf (get crospy::sub :response) crospy::subResponse)

(defmethod crospy::subRequest
  (:response () (instance crospy::subResponse :init)))

(setf (get crospy::subRequest :md5sum-) "4096e8e9f96b81072bcc1faf81a24d83")
(setf (get crospy::subRequest :datatype-) "crospy/subRequest")
(setf (get crospy::subRequest :definition-)
      "string client
---
int64 ret

")

(setf (get crospy::subResponse :md5sum-) "4096e8e9f96b81072bcc1faf81a24d83")
(setf (get crospy::subResponse :datatype-) "crospy/subResponse")
(setf (get crospy::subResponse :definition-)
      "string client
---
int64 ret

")



(provide :crospy/sub "4096e8e9f96b81072bcc1faf81a24d83")


