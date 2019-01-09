
(cl:in-package :asdf)

(defsystem "basic_lecture-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "cmsg" :depends-on ("_package_cmsg"))
    (:file "_package_cmsg" :depends-on ("_package"))
  ))