import { createRoot } from 'react-dom/client';
import { NewsFeed } from './mainfeed';
import './scss/styles.scss';


//const postformroot = createRoot(document.getElementById('post-form'))
//postformroot.render(<NewsFeedPostForm />)

const root = createRoot(document.getElementById('main-feed'))
const demodata = require('../tests/newsfeed_test_data')
const demoposts = demodata.posts || []
root.render(<NewsFeed postdata={ demoposts } />);
 