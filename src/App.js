import { createRoot, hydrateRoot } from 'react-dom/client';
import { NewsFeed } from './mainfeed';
import { NewsFeedPostForm } from './postforms';
import { Dropdown } from 'bootstrap';
import './scss/styles.scss'


const postformroot = createRoot(document.getElementById('post-form'))
postformroot.render(<NewsFeedPostForm />)

const root = createRoot(document.getElementById('main-feed'))

var demoposts = [{  //demo feed data!
    key: 0,
    author: 1,
    title: 'HalihóÓ',
    text: 'Ez az első poszt',
  },
  {
    key: 1,
    author: 1,
    title: null,
    text: 'Lorem ipsum',
  },
  {
    key: 2,
    author: 1,
    title: "Lorem",
    text: "Lorem Ipsum is simply dummy <a href='#'>text</a> of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
  },
]

root.render(<NewsFeed posts={ demoposts } />);
 