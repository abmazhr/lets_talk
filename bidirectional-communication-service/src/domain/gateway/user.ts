import { UserCredentials } from '../entity/user_creds';
import { Success } from '../entity/success';
import { Error } from '../entity/error';

interface CheckUserCredentials {
  execute(userCreds: UserCredentials): Error | Success;
}
