import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';


export function BasicPost(props) {
  let postContent = [];
  let postHeader, postFooter;
  props.date ? postHeader = [props.date.toLocaleString()] :
  //TODO: check user is_authenticated
  postFooter = [<Button variant="outline-primary my-1" size='sm'>Comment</Button>]
  postHeader && postContent.push(<Card.Header>{postHeader}</Card.Header>)
  props.title && postContent.push(<Card.Title>{props.title}</Card.Title>);
  props.text && postContent.push(<Card.Text>{props.text}</Card.Text>);
  postFooter && postContent.push(<Card.Footer>{postFooter}</Card.Footer>)

  return (
    <Card className={"newsfeed-post"}>
      <Card.Body>
        {postContent}
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
      fetch('/newsfeed/sendpost', { method: form.method, body: formData });

      // Or you can work with it as a plain object:
      const formJson = Object.fromEntries(formData.entries());
      formJson.date = new Date();
      console.log(formJson);
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
