import { createRoot } from 'react-dom/client';
import { NewsFeed } from './mainfeed';
import './scss/styles.scss';


let errorlog = []
const debugInfoBox = document.querySelector("#debug-info")

const root = createRoot(document.getElementById('main-feed'))
const demodata = require('../../tests/newsfeed_test_data')
const posts = demodata.posts || []
root.render(<NewsFeed postdata={ posts } />);

let idb
const request = window.indexedDB.open("NewsFeedDatabase", 1);

request.onerror = (event) => {
    console.error(`Error creating IndexedDB: ${event}`)
    errorlog.push(event)
    // keep errorlog length under 100
    errorlog.length > 100 && errorlog.shift() 
};

request.onsuccess = (event) => {
    idb = event.target.result
    console.log("IDB Success!")
    debugInfoBox ? debugInfoBox.innerHTML = "IDB init successful" :

    idb.onerror = (event) => {
        // Generic error handler for all errors targeted at IndexedDB requests
        console.error(`IndexedDB error: ${event.target.errorCode}`);
    };
};
