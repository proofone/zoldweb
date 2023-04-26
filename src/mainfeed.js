import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';


export function BasicPost() {
  return (
    <Card style={{  }}>
      <Card.Body>
        <Card.Title>Hello wrld'</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
        <Button variant="outline-primary">Go somewhere</Button>
      </Card.Body>
    </Card>
  );
}
