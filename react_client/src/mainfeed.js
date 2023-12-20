import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';


export function BasicPost(props) {
  let postContent = [];
  let postHeader, postFooter;
  props.date ? postHeader = [props.date.toLocaleString()] : null
  //TODO: check user is_authenticated
  const postButtons = [<Button variant="outline-primary my-1" size='sm'>Comment</Button>]
  props.title && postContent.push(<Card.Title>{props.title}</Card.Title>);
  props.text && postContent.push(<Card.Text>{props.text}</Card.Text>);
  postFooter = <Card.Footer>{postButtons}</Card.Footer>

  return (
    <Card className={"newsfeed-post"}>
      <Card.Header>{postHeader}</Card.Header>
      <Card.Body>
        {postContent}
      </Card.Body>
      {postFooter}
    </Card>
  );
}

export function NewsFeed({ postdata }) {

  let [posts, setPosts] = useState(postdata)

  function handleSubmit(e) {
      // Prevent the browser from reloading the page
      e.preventDefault();

      // Read the form data
      const formData = new FormData(e.target);
      formData.append('created_date', new Date());
      const formJson = Object.fromEntries(formData.entries());

      // Passing formData to the API
      fetch('/newsfeed/sendpost', { method: e.target.method, body: formData });

      // Pushing new post to feed
      setPosts([formJson, ...posts])
  }

  function NewsFeedPostForm() {
    return (
      <Form id='newsfeedpostform' className="my-2" onSubmit={handleSubmit} method='POST'>
        <Form.Label visuallyHidden="true">Posztod szövege</Form.Label>
        <Form.Control name="text" id="posttext" as="textarea" placeholder="Posztod szövege">
        </Form.Control>
        <input type="hidden" name="author" id="post-author"/>

        <Button variant="primary" type="submit">Submit</Button>
      </Form>
    );
  }

  posts.sort((a, b) => b.key-a.key)

  let renderedContent = [ <NewsFeedPostForm /> ]
  renderedContent.push(
    posts.map((postProps) => {
      return <BasicPost key={postProps.key} {...postProps} />
    })    
  )

  return renderedContent
}
