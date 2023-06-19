import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

export function NewsFeedPostForm() {
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
        console.log(formJson);
    }

    return (
        <Form id='newsfeedpostform' className="my-2" onSubmit={handleSubmit}>
            <Form.Label visuallyHidden="true">Posztod szövege</Form.Label>
            <Form.Control name="text" id="posttext" as="textarea" placeholder="Posztod szövege">
            </Form.Control>
            <input type="hidden" name="author" />

        <Button variant="primary" type="submit">
            Submit
        </Button>
        </Form>
    );
}

