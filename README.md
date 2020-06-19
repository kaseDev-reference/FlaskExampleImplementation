# FlaskExampleImplementation
Unit Project demonstrating an implementation of most of the core Flask features through the design of an example website.

## Architecture
The architecture of this project is composed of a single python script that imports flask. Nothing special

## Static Architecture
This project is an implementation of a server and hence returns various web pages when pinged with HTTP requests.
Web pages can be componsed of html, css, and javascript that link to each other in important ways whereby html pages
link to css and javascript files. But with jinja and the concept of html inherentence, html files can even extend other
html files. 

This is a diagram of the dependencies of static files present in this project.

![-- must fix diagram --][static-architecture]

(implementing css was originally a plan but doing so requires no special flask programming and so was not completed. The
file still exists to show that it would need to exist in the "static" folder.

## HTTP Message Web
The web server is designed to take HTTP Requests as inputs and then return HTTP Responses as outputs. This is a diagram
of the which requests will recieve which responses.

![-- must fix diagram --][HTTP-diagram]

[HTTP-diagram]: ./diagrams/http-message-web.png "HTTP Message Web"
[static-architecture]: ./diagrams/static-resource-architecture.png "Static Resource Architecture"
