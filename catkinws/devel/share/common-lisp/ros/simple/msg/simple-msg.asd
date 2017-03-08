
(cl:in-package :asdf)

(defsystem "simple-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Layer" :depends-on ("_package_Layer"))
    (:file "_package_Layer" :depends-on ("_package"))
    (:file "Num" :depends-on ("_package_Num"))
    (:file "_package_Num" :depends-on ("_package"))
  ))