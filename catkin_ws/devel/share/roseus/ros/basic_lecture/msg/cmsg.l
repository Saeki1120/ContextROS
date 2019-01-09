;; Auto-generated. Do not edit!


(when (boundp 'basic_lecture::cmsg)
  (if (not (find-package "BASIC_LECTURE"))
    (make-package "BASIC_LECTURE"))
  (shadow 'cmsg (find-package "BASIC_LECTURE")))
(unless (find-package "BASIC_LECTURE::CMSG")
  (make-package "BASIC_LECTURE::CMSG"))

(in-package "ROS")
;;//! \htmlinclude cmsg.msg.html


(defclass basic_lecture::cmsg
  :super ros::object
  :slots (_word _number ))

(defmethod basic_lecture::cmsg
  (:init
   (&key
    ((:word __word) "")
    ((:number __number) 0)
    )
   (send-super :init)
   (setq _word (string __word))
   (setq _number (round __number))
   self)
  (:word
   (&optional __word)
   (if __word (setq _word __word)) _word)
  (:number
   (&optional __number)
   (if __number (setq _number __number)) _number)
  (:serialization-length
   ()
   (+
    ;; string _word
    4 (length _word)
    ;; int32 _number
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _word
       (write-long (length _word) s) (princ _word s)
     ;; int32 _number
       (write-long _number s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _word
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _word (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int32 _number
     (setq _number (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get basic_lecture::cmsg :md5sum-) "f9d86ff4272085f66f41cd72b9cfc49d")
(setf (get basic_lecture::cmsg :datatype-) "basic_lecture/cmsg")
(setf (get basic_lecture::cmsg :definition-)
      "string word
int32  number

")



(provide :basic_lecture/cmsg "f9d86ff4272085f66f41cd72b9cfc49d")


