import './env';
import L from './logger';

const port = process.env.PORT;

L.info(`port is :: ${port}`);
