// Auto-generated. Do not edit!

// (in-package crospy.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class subRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.client = null;
    }
    else {
      if (initObj.hasOwnProperty('client')) {
        this.client = initObj.client
      }
      else {
        this.client = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type subRequest
    // Serialize message field [client]
    bufferOffset = _serializer.string(obj.client, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type subRequest
    let len;
    let data = new subRequest(null);
    // Deserialize message field [client]
    data.client = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.client.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'crospy/subRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a3397efab4a31b69099037ec38e22ec9';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string client
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new subRequest(null);
    if (msg.client !== undefined) {
      resolved.client = msg.client;
    }
    else {
      resolved.client = ''
    }

    return resolved;
    }
};

class subResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ret = null;
    }
    else {
      if (initObj.hasOwnProperty('ret')) {
        this.ret = initObj.ret
      }
      else {
        this.ret = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type subResponse
    // Serialize message field [ret]
    bufferOffset = _serializer.int64(obj.ret, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type subResponse
    let len;
    let data = new subResponse(null);
    // Deserialize message field [ret]
    data.ret = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'crospy/subResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2522e220fa06fe7901e82fcde5a0bb66';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 ret
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new subResponse(null);
    if (msg.ret !== undefined) {
      resolved.ret = msg.ret;
    }
    else {
      resolved.ret = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: subRequest,
  Response: subResponse,
  md5sum() { return '4096e8e9f96b81072bcc1faf81a24d83'; },
  datatype() { return 'crospy/sub'; }
};
