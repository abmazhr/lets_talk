import { Message } from '../entity/message';
import { Success } from '../entity/success';
import { Error } from '../entity/error';

interface SendMessage {
  execute(message: Message): Error | Success;
}
