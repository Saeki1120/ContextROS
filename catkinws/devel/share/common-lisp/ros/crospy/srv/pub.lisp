; Auto-generated. Do not edit!


(cl:in-package crospy-srv)


;//! \htmlinclude pub-request.msg.html

(cl:defclass <pub-request> (roslisp-msg-protocol:ros-message)
  ((type
    :reader type
    :initarg :type
    :type cl:string
    :initform "")
   (layer
    :reader layer
    :initarg :layer
    :type cl:string
    :initform ""))
)

(cl:defclass pub-request (<pub-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <pub-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'pub-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name crospy-srv:<pub-request> is deprecated: use crospy-srv:pub-request instead.")))

(cl:ensure-generic-function 'type-val :lambda-list '(m))
(cl:defmethod type-val ((m <pub-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader crospy-srv:type-val is deprecated.  Use crospy-srv:type instead.")
  (type m))

(cl:ensure-generic-function 'layer-val :lambda-list '(m))
(cl:defmethod layer-val ((m <pub-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader crospy-srv:layer-val is deprecated.  Use crospy-srv:layer instead.")
  (layer m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <pub-request>) ostream)
  "Serializes a message object of type '<pub-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'type))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'type))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'layer))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'layer))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <pub-request>) istream)
  "Deserializes a message object of type '<pub-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'type) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'type) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'layer) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'layer) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<pub-request>)))
  "Returns string type for a service object of type '<pub-request>"
  "crospy/pubRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pub-request)))
  "Returns string type for a service object of type 'pub-request"
  "crospy/pubRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<pub-request>)))
  "Returns md5sum for a message object of type '<pub-request>"
  "f9f9aa5fef081d148fcc68ac90f825a1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'pub-request)))
  "Returns md5sum for a message object of type 'pub-request"
  "f9f9aa5fef081d148fcc68ac90f825a1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<pub-request>)))
  "Returns full string definition for message of type '<pub-request>"
  (cl:format cl:nil "string type~%string layer~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'pub-request)))
  "Returns full string definition for message of type 'pub-request"
  (cl:format cl:nil "string type~%string layer~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <pub-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'type))
     4 (cl:length (cl:slot-value msg 'layer))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <pub-request>))
  "Converts a ROS message object to a list"
  (cl:list 'pub-request
    (cl:cons ':type (type msg))
    (cl:cons ':layer (layer msg))
))
;//! \htmlinclude pub-response.msg.html

(cl:defclass <pub-response> (roslisp-msg-protocol:ros-message)
  ((ret
    :reader ret
    :initarg :ret
    :type cl:integer
    :initform 0))
)

(cl:defclass pub-response (<pub-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <pub-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'pub-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name crospy-srv:<pub-response> is deprecated: use crospy-srv:pub-response instead.")))

(cl:ensure-generic-function 'ret-val :lambda-list '(m))
(cl:defmethod ret-val ((m <pub-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader crospy-srv:ret-val is deprecated.  Use crospy-srv:ret instead.")
  (ret m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <pub-response>) ostream)
  "Serializes a message object of type '<pub-response>"
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <pub-response>) istream)
  "Deserializes a message object of type '<pub-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<pub-response>)))
  "Returns string type for a service object of type '<pub-response>"
  "crospy/pubResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pub-response)))
  "Returns string type for a service object of type 'pub-response"
  "crospy/pubResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<pub-response>)))
  "Returns md5sum for a message object of type '<pub-response>"
  "f9f9aa5fef081d148fcc68ac90f825a1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'pub-response)))
  "Returns md5sum for a message object of type 'pub-response"
  "f9f9aa5fef081d148fcc68ac90f825a1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<pub-response>)))
  "Returns full string definition for message of type '<pub-response>"
  (cl:format cl:nil "int64 ret~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'pub-response)))
  "Returns full string definition for message of type 'pub-response"
  (cl:format cl:nil "int64 ret~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <pub-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <pub-response>))
  "Converts a ROS message object to a list"
  (cl:list 'pub-response
    (cl:cons ':ret (ret msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'pub)))
  'pub-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'pub)))
  'pub-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pub)))
  "Returns string type for a service object of type '<pub>"
  "crospy/pub")