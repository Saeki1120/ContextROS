
(cl:in-package :asdf)

(defsystem "crospy-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "pub" :depends-on ("_package_pub"))
    (:file "_package_pub" :depends-on ("_package"))
    (:file "sub" :depends-on ("_package_sub"))
    (:file "_package_sub" :depends-on ("_package"))
  ))