// Auto-generated. Do not edit!

// (in-package basic_lecture.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class cmsg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.word = null;
      this.number = null;
    }
    else {
      if (initObj.hasOwnProperty('word')) {
        this.word = initObj.word
      }
      else {
        this.word = '';
      }
      if (initObj.hasOwnProperty('number')) {
        this.number = initObj.number
      }
      else {
        this.number = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type cmsg
    // Serialize message field [word]
    bufferOffset = _serializer.string(obj.word, buffer, bufferOffset);
    // Serialize message field [number]
    bufferOffset = _serializer.int32(obj.number, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type cmsg
    let len;
    let data = new cmsg(null);
    // Deserialize message field [word]
    data.word = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [number]
    data.number = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.word.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'basic_lecture/cmsg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f9d86ff4272085f66f41cd72b9cfc49d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string word
    int32  number
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new cmsg(null);
    if (msg.word !== undefined) {
      resolved.word = msg.word;
    }
    else {
      resolved.word = ''
    }

    if (msg.number !== undefined) {
      resolved.number = msg.number;
    }
    else {
      resolved.number = 0
    }

    return resolved;
    }
};

module.exports = cmsg;
