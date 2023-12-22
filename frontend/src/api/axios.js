import axios from 'axios';
import { BACKEND_API } from '../constants';

export const axiosFile = axios.create({
  baseUrl: `http://${BACKEND_API}/`,
  headers: {
    'Content-Type': 'multipart/form-data',
  },
});

export const axiosClient = axios.create({
  baseUrl: `http://${BACKEND_API}/`,
  headers: {
    'Content-Type': 'application/json',
  },
});
