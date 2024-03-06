<img src="https://miro.medium.com/v2/resize:fit:2400/1*E1LonYGC5Fx4QLY4W5SaVA.jpeg" width="100" alt="Udacity logo">
<h1 align="center" style="color:#FC642D">AirBnB Clone Project</h1>

<img src="assets/airbnb.png">

## OverView
This project aims to replicate the fundamental features of the AirBnB platform for educational purposes. Spanning the duration of our first year, it presents a hands-on opportunity to apply higher-level programming concepts in a real-world application. Our AirBnB clone will be a simplified version, focusing on essential functionalities to understand the core aspects of web development and data management.


## Objectives
The primary goal is to create a web application that mimics the AirBnB website, including:
- A command interpreter for data manipulation without a GUI, akin to a Shell environment. This serves both development and debugging purposes.
- A dynamic website to showcase the final product, featuring both static and dynamic content.
- A storage solution (database or files) for persisting data.
- An API for facilitating communication between the front-end and the stored data, enabling CRUD operations.

## Technical Specifications
- **Programming Languages:** `Python`, `HTML`, `CSS`, `JavaScript`
- **Frameworks and Libraries:** `Flask` (`Python` Web Framework), `SQLAlchemy` (ORM), `JQuery`
- **Database:** `MySQL`
- **Data Formats:** `JSON` for serialization/deserialization

## Project Structure
- `models/`: Contains all class definitions for the project's data models.
- `tests/`: Houses unit tests ensuring functionality and reliability.
- `console.py`: The entry point for the command interpreter.
- `models/base_model.py`: The base class for all models, including common attributes and methods.
- `models/engine/`: Storage classes, initially featuring file_storage.py for JSON-based object persistence.
- `web_static/`: Static HTML and CSS files for the web interface.
- `api/`: RESTful API components for object manipulation and retrieval.

## Concepts Covered
- `Unittest` for comprehensive testing.
- `Python packages` for modular code organization.
- `Serialization/Deserialization` for object persistence.
- Use of `*args` and `**kwargs` for flexible function arguments.
- `datetime` for time-based attributes.
- Dynamic web content with `Flask` and `JQuery`.

## Development Steps
The project is structured in incremental steps, each focusing on specific functionalities:

#### 1. The Console
The first step involves setting up a command interpreter to manage our data models and simulate a storage system. This system abstracts the details of how objects are stored, whether in files or databases, allowing us to focus on functionality without worrying about the underlying storage mechanism.

#### 2. Web Static
Learning HTML/CSS to create the front-end templates, laying the groundwork for our web interface.

#### 3. Database Storage
Transitioning from file storage to a database system, using an ORM to map models to database tables.

#### 4. Web Framework and Templating
Setting up a Python web server and utilizing templates to render dynamic content based on stored data.

#### 5. RESTful API
Developing an API to expose stored data through JSON, enabling CRUD operations via HTTP requests.

#### 6. Web Dynamic
Integrating JavaScript and JQuery to enhance the web interface with dynamic content loading using the API.

## TODO
- [ ] add get-started
