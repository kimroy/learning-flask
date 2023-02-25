# Learning Flask 

## app1
- Basic page which redirects using `redirect` and `url_for`
- Implements and shows function decoration with `app.route()`

## app2
- Basic page redirects using `redirect`, `url_for`, `render_template()`
- Used to render a seperate templates/*.html on return
- index2.html also includes python code within to perform certain functionality

## app3
- Basic page redirects using `redirect`, `url_for`, `render_template()`
- Utilizes a base.html which index3.html extends
- Introduces the idea of blocks in flask

## app4
- Basic page redirects using `redirect`, `url_for`, `render_template()`, and implements `request` functionality
- Introduces forms and `routes()` with `POST` and `GET` methods
- Passes the name variable based on user input and updates the webpage dynamically

## app5
- Basic page redirects using `redirect`, `url_for`, `render_template()`, and implements `request` with persistent `session` functionality
- Implements a app secret key and a session lifetime
- This application will retain user login session for `x` days until the session is closed
- Introduces logout functionality as well which ends the current users session and prompts the login page

## app6
- Basic page redirects using `redirect`, `url_for`, `render_template()`, and implements `request` with persistent `session`, `flash` functionality
- Implements `flash()` which will render a prompt based on login success, already logged in, and user logouts

## app7
- Basic page redirects using `redirect`, `url_for`, `render_template()`, `request`  `session`, `flash`, `sqlalchemy`
- Creates a users db with sqlite3

## app8
- Basic page redirects using `redirect`, `url_for`, `render_template()`, `request`  `session`, `flash`, `sqlalchemy`
- Creates a users db with sqlite3 which stores the users name and email

## app9
- Basic page with `render_template()` functionality
- Implemented static css and images

## app10 / app10_2
- Basic page with `render_template()`, `Blueprint` functionality
- Renders app10_2 from app10 using `Blueprint` with `app.register_blueprint(app10_2, url_prefix='/admin')` in the main application app10