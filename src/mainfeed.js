import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { NewsFeedPostForm } from './postforms';


export function BasicPost(props) {
  let postContent = [];
  props.title && postContent.push(<Card.Title>{props.title}</Card.Title>);
  props.text && postContent.push(<Card.Text>{props.text}</Card.Text>);
  return (
    <Card className={"newsfeed-post"}>
      <Card.Body>
        {postContent}
        <Button variant="outline-primary my-1">Go somewhere</Button>
      </Card.Body>
    </Card>
  );
}

export function NewsFeed({ postdata }) {

  let [posts, setPosts] = useState(postdata)

  function handleSubmit(e) {
    // Prevent the browser from reloading the page
    e.preventDefault();

    // Read the form data
    const form = e.target;
    const formData = new FormData(form);

    // Passing formData to the API:
    //fetch('/some-api', { method: form.method, body: formData });

    // Or you can work with it as a plain object:
    const formJson = Object.fromEntries(formData.entries());
    console.log(formJson);
    setPosts([formJson])
}

  posts.sort((a, b) => b.key-a.key)
  let renderedContent = [ <NewsFeedPostForm onSubmit={handleSubmit} /> ]
  renderedContent.push(
    posts.map((postProps) => {
      return <BasicPost key={postProps.key} {...postProps} />
    })    
  )
  return renderedContent
}
