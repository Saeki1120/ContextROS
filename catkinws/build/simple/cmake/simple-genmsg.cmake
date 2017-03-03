# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "simple: 1 messages, 1 services")

set(MSG_I_FLAGS "-Isimple:/Users/nel/src/ContextROS/catkinws/src/simple/msg;-Istd_msgs:/Users/nel/src/ros_catkin_ws/install_isolated/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(simple_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/Users/nel/src/ContextROS/catkinws/src/simple/msg/Num.msg" NAME_WE)
add_custom_target(_simple_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "simple" "/Users/nel/src/ContextROS/catkinws/src/simple/msg/Num.msg" ""
)

get_filename_component(_filename "/Users/nel/src/ContextROS/catkinws/src/simple/srv/AddTwoInts.srv" NAME_WE)
add_custom_target(_simple_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "simple" "/Users/nel/src/ContextROS/catkinws/src/simple/srv/AddTwoInts.srv" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(simple
  "/Users/nel/src/ContextROS/catkinws/src/simple/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/simple
)

### Generating Services
_generate_srv_cpp(simple
  "/Users/nel/src/ContextROS/catkinws/src/simple/srv/AddTwoInts.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/simple
)

### Generating Module File
_generate_module_cpp(simple
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/simple
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(simple_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(simple_generate_messages simple_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/Users/nel/src/ContextROS/catkinws/src/simple/msg/Num.msg" NAME_WE)
add_dependencies(simple_generate_messages_cpp _simple_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/Users/nel/src/ContextROS/catkinws/src/simple/srv/AddTwoInts.srv" NAME_WE)
add_dependencies(simple_generate_messages_cpp _simple_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(simple_gencpp)
add_dependencies(simple_gencpp simple_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS simple_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(simple
  "/Users/nel/src/ContextROS/catkinws/src/simple/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/simple
)

### Generating Services
_generate_srv_lisp(simple
  "/Users/nel/src/ContextROS/catkinws/src/simple/srv/AddTwoInts.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/simple
)

### Generating Module File
_generate_module_lisp(simple
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/simple
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(simple_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(simple_generate_messages simple_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/Users/nel/src/ContextROS/catkinws/src/simple/msg/Num.msg" NAME_WE)
add_dependencies(simple_generate_messages_lisp _simple_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/Users/nel/src/ContextROS/catkinws/src/simple/srv/AddTwoInts.srv" NAME_WE)
add_dependencies(simple_generate_messages_lisp _simple_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(simple_genlisp)
add_dependencies(simple_genlisp simple_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS simple_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(simple
  "/Users/nel/src/ContextROS/catkinws/src/simple/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/simple
)

### Generating Services
_generate_srv_py(simple
  "/Users/nel/src/ContextROS/catkinws/src/simple/srv/AddTwoInts.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/simple
)

### Generating Module File
_generate_module_py(simple
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/simple
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(simple_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(simple_generate_messages simple_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/Users/nel/src/ContextROS/catkinws/src/simple/msg/Num.msg" NAME_WE)
add_dependencies(simple_generate_messages_py _simple_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/Users/nel/src/ContextROS/catkinws/src/simple/srv/AddTwoInts.srv" NAME_WE)
add_dependencies(simple_generate_messages_py _simple_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(simple_genpy)
add_dependencies(simple_genpy simple_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS simple_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/simple)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/simple
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(simple_generate_messages_cpp std_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/simple)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/simple
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(simple_generate_messages_lisp std_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/simple)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/simple\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/simple
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(simple_generate_messages_py std_msgs_generate_messages_py)
