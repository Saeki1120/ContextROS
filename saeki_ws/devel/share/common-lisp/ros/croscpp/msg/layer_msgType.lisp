; Auto-generated. Do not edit!


(cl:in-package croscpp-msg)


;//! \htmlinclude layer_msgType.msg.html

(cl:defclass <layer_msgType> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform ""))
)

(cl:defclass layer_msgType (<layer_msgType>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <layer_msgType>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'layer_msgType)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name croscpp-msg:<layer_msgType> is deprecated: use croscpp-msg:layer_msgType instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <layer_msgType>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader croscpp-msg:name-val is deprecated.  Use croscpp-msg:name instead.")
  (name m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <layer_msgType>) ostream)
  "Serializes a message object of type '<layer_msgType>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <layer_msgType>) istream)
  "Deserializes a message object of type '<layer_msgType>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<layer_msgType>)))
  "Returns string type for a message object of type '<layer_msgType>"
  "croscpp/layer_msgType")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'layer_msgType)))
  "Returns string type for a message object of type 'layer_msgType"
  "croscpp/layer_msgType")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<layer_msgType>)))
  "Returns md5sum for a message object of type '<layer_msgType>"
  "c1f3d28f1b044c871e6eff2e9fc3c667")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'layer_msgType)))
  "Returns md5sum for a message object of type 'layer_msgType"
  "c1f3d28f1b044c871e6eff2e9fc3c667")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<layer_msgType>)))
  "Returns full string definition for message of type '<layer_msgType>"
  (cl:format cl:nil "string name ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'layer_msgType)))
  "Returns full string definition for message of type 'layer_msgType"
  (cl:format cl:nil "string name ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <layer_msgType>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <layer_msgType>))
  "Converts a ROS message object to a list"
  (cl:list 'layer_msgType
    (cl:cons ':name (name msg))
))
