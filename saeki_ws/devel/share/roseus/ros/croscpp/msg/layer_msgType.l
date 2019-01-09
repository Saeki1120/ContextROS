;; Auto-generated. Do not edit!


(when (boundp 'croscpp::layer_msgType)
  (if (not (find-package "CROSCPP"))
    (make-package "CROSCPP"))
  (shadow 'layer_msgType (find-package "CROSCPP")))
(unless (find-package "CROSCPP::LAYER_MSGTYPE")
  (make-package "CROSCPP::LAYER_MSGTYPE"))

(in-package "ROS")
;;//! \htmlinclude layer_msgType.msg.html


(defclass croscpp::layer_msgType
  :super ros::object
  :slots (_name ))

(defmethod croscpp::layer_msgType
  (:init
   (&key
    ((:name __name) "")
    )
   (send-super :init)
   (setq _name (string __name))
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get croscpp::layer_msgType :md5sum-) "c1f3d28f1b044c871e6eff2e9fc3c667")
(setf (get croscpp::layer_msgType :datatype-) "croscpp/layer_msgType")
(setf (get croscpp::layer_msgType :definition-)
      "string name 

")



(provide :croscpp/layer_msgType "c1f3d28f1b044c871e6eff2e9fc3c667")


