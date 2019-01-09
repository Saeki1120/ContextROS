// Generated by gencpp from file crospy/subResponse.msg
// DO NOT EDIT!


#ifndef CROSPY_MESSAGE_SUBRESPONSE_H
#define CROSPY_MESSAGE_SUBRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace crospy
{
template <class ContainerAllocator>
struct subResponse_
{
  typedef subResponse_<ContainerAllocator> Type;

  subResponse_()
    : ret(0)  {
    }
  subResponse_(const ContainerAllocator& _alloc)
    : ret(0)  {
  (void)_alloc;
    }



   typedef int64_t _ret_type;
  _ret_type ret;





  typedef boost::shared_ptr< ::crospy::subResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::crospy::subResponse_<ContainerAllocator> const> ConstPtr;

}; // struct subResponse_

typedef ::crospy::subResponse_<std::allocator<void> > subResponse;

typedef boost::shared_ptr< ::crospy::subResponse > subResponsePtr;
typedef boost::shared_ptr< ::crospy::subResponse const> subResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::crospy::subResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::crospy::subResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace crospy

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::crospy::subResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::crospy::subResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::crospy::subResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::crospy::subResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::crospy::subResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::crospy::subResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::crospy::subResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2522e220fa06fe7901e82fcde5a0bb66";
  }

  static const char* value(const ::crospy::subResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2522e220fa06fe79ULL;
  static const uint64_t static_value2 = 0x01e82fcde5a0bb66ULL;
};

template<class ContainerAllocator>
struct DataType< ::crospy::subResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "crospy/subResponse";
  }

  static const char* value(const ::crospy::subResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::crospy::subResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 ret\n\
\n\
";
  }

  static const char* value(const ::crospy::subResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::crospy::subResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.ret);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct subResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::crospy::subResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::crospy::subResponse_<ContainerAllocator>& v)
  {
    s << indent << "ret: ";
    Printer<int64_t>::stream(s, indent + "  ", v.ret);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CROSPY_MESSAGE_SUBRESPONSE_H
