import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';


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

export function NewsFeed({ posts }) {

  posts.sort((a, b) => b.key-a.key)
  return (
    posts.map((postProps) => {
      return <BasicPost key={postProps.key} {...postProps} />
    })
  )
}
