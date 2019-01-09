
(cl:in-package :asdf)

(defsystem "croscpp-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "layer_msgType" :depends-on ("_package_layer_msgType"))
    (:file "_package_layer_msgType" :depends-on ("_package"))
  ))