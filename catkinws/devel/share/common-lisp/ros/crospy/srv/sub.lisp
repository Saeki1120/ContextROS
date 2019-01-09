; Auto-generated. Do not edit!


(cl:in-package crospy-srv)


;//! \htmlinclude sub-request.msg.html

(cl:defclass <sub-request> (roslisp-msg-protocol:ros-message)
  ((client
    :reader client
    :initarg :client
    :type cl:string
    :initform ""))
)

(cl:defclass sub-request (<sub-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <sub-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'sub-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name crospy-srv:<sub-request> is deprecated: use crospy-srv:sub-request instead.")))

(cl:ensure-generic-function 'client-val :lambda-list '(m))
(cl:defmethod client-val ((m <sub-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader crospy-srv:client-val is deprecated.  Use crospy-srv:client instead.")
  (client m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <sub-request>) ostream)
  "Serializes a message object of type '<sub-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'client))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'client))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <sub-request>) istream)
  "Deserializes a message object of type '<sub-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'client) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'client) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<sub-request>)))
  "Returns string type for a service object of type '<sub-request>"
  "crospy/subRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'sub-request)))
  "Returns string type for a service object of type 'sub-request"
  "crospy/subRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<sub-request>)))
  "Returns md5sum for a message object of type '<sub-request>"
  "4096e8e9f96b81072bcc1faf81a24d83")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'sub-request)))
  "Returns md5sum for a message object of type 'sub-request"
  "4096e8e9f96b81072bcc1faf81a24d83")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<sub-request>)))
  "Returns full string definition for message of type '<sub-request>"
  (cl:format cl:nil "string client~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'sub-request)))
  "Returns full string definition for message of type 'sub-request"
  (cl:format cl:nil "string client~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <sub-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'client))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <sub-request>))
  "Converts a ROS message object to a list"
  (cl:list 'sub-request
    (cl:cons ':client (client msg))
))
;//! \htmlinclude sub-response.msg.html

(cl:defclass <sub-response> (roslisp-msg-protocol:ros-message)
  ((ret
    :reader ret
    :initarg :ret
    :type cl:integer
    :initform 0))
)

(cl:defclass sub-response (<sub-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <sub-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'sub-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name crospy-srv:<sub-response> is deprecated: use crospy-srv:sub-response instead.")))

(cl:ensure-generic-function 'ret-val :lambda-list '(m))
(cl:defmethod ret-val ((m <sub-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader crospy-srv:ret-val is deprecated.  Use crospy-srv:ret instead.")
  (ret m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <sub-response>) ostream)
  "Serializes a message object of type '<sub-response>"
  (cl:let* ((signed (cl:slot-value msg 'ret)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <sub-response>) istream)
  "Deserializes a message object of type '<sub-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ret) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<sub-response>)))
  "Returns string type for a service object of type '<sub-response>"
  "crospy/subResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'sub-response)))
  "Returns string type for a service object of type 'sub-response"
  "crospy/subResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<sub-response>)))
  "Returns md5sum for a message object of type '<sub-response>"
  "4096e8e9f96b81072bcc1faf81a24d83")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'sub-response)))
  "Returns md5sum for a message object of type 'sub-response"
  "4096e8e9f96b81072bcc1faf81a24d83")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<sub-response>)))
  "Returns full string definition for message of type '<sub-response>"
  (cl:format cl:nil "int64 ret~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'sub-response)))
  "Returns full string definition for message of type 'sub-response"
  (cl:format cl:nil "int64 ret~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <sub-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <sub-response>))
  "Converts a ROS message object to a list"
  (cl:list 'sub-response
    (cl:cons ':ret (ret msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'sub)))
  'sub-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'sub)))
  'sub-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'sub)))
  "Returns string type for a service object of type '<sub>"
  "crospy/sub")