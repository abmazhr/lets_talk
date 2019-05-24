enum MessageType {
  TEXT
}

interface Message {
  message: string;
  messageType: MessageType;
  fromSocketId: string;
  toSocketId: string;
}

export { Message, MessageType };
