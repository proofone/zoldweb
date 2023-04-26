import { createRoot } from 'react-dom/client';
import { BasicPost } from './mainfeed';
import React from "react";
//import ReactDOM from 'react-dom';
//const bootstrap = require('bootstrap');

const root = createRoot(document.getElementById('main-feed'))

root.render(<BasicPost />);
