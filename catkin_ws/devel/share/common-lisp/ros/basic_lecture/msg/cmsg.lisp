; Auto-generated. Do not edit!


(cl:in-package basic_lecture-msg)


;//! \htmlinclude cmsg.msg.html

(cl:defclass <cmsg> (roslisp-msg-protocol:ros-message)
  ((word
    :reader word
    :initarg :word
    :type cl:string
    :initform "")
   (number
    :reader number
    :initarg :number
    :type cl:integer
    :initform 0))
)

(cl:defclass cmsg (<cmsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <cmsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'cmsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name basic_lecture-msg:<cmsg> is deprecated: use basic_lecture-msg:cmsg instead.")))

(cl:ensure-generic-function 'word-val :lambda-list '(m))
(cl:defmethod word-val ((m <cmsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader basic_lecture-msg:word-val is deprecated.  Use basic_lecture-msg:word instead.")
  (word m))

(cl:ensure-generic-function 'number-val :lambda-list '(m))
(cl:defmethod number-val ((m <cmsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader basic_lecture-msg:number-val is deprecated.  Use basic_lecture-msg:number instead.")
  (number m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <cmsg>) ostream)
  "Serializes a message object of type '<cmsg>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'word))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'word))
  (cl:let* ((signed (cl:slot-value msg 'number)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <cmsg>) istream)
  "Deserializes a message object of type '<cmsg>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'word) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'word) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'number) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<cmsg>)))
  "Returns string type for a message object of type '<cmsg>"
  "basic_lecture/cmsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'cmsg)))
  "Returns string type for a message object of type 'cmsg"
  "basic_lecture/cmsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<cmsg>)))
  "Returns md5sum for a message object of type '<cmsg>"
  "f9d86ff4272085f66f41cd72b9cfc49d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'cmsg)))
  "Returns md5sum for a message object of type 'cmsg"
  "f9d86ff4272085f66f41cd72b9cfc49d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<cmsg>)))
  "Returns full string definition for message of type '<cmsg>"
  (cl:format cl:nil "string word~%int32  number~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'cmsg)))
  "Returns full string definition for message of type 'cmsg"
  (cl:format cl:nil "string word~%int32  number~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <cmsg>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'word))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <cmsg>))
  "Converts a ROS message object to a list"
  (cl:list 'cmsg
    (cl:cons ':word (word msg))
    (cl:cons ':number (number msg))
))
