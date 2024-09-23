# bean-scape
Platform Based Programming (PBP) Course --- Tugas Individu 

## Bookmarks
- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)
- [Tugas 4](#tugas-4)

## Tugas 2 <a id="tugas-2"></a>
[beanScape's url](http://rakabima-ghaniendra-beanscape.pbp.cs.ui.ac.id)
- Implementing Checklists
    1. Initialize repository
        * Create a new repository with the project's name `bean-scape`
        * Create a local directory with the same name
        * Link the local directory to the project's repository with `git add remote <repo's url>`
    2. Setup environment (Django)
        * Initialize python virtual environment (venv) with `python -m venv env` and activate with `env\Scripts\activate`
        * Install the requirements/dependencies using `pip install`
    3. Initialize Django project
        * Create a new Django project with `django-admin startproject`
        * Add the following `"localhost", "127.0.0.1"` to `ALLOWED_HOST` in `setting.py`
        * Create new app `main` with `python manage.py startapp main`
        * Add `main` to `INSTALLED_APPS` in `settings.py`
    4. Implement Django MVT (Model-View-Template)
        * Create model in `models.py`. Migrate every change with `python manage.py makemigrations` and `python manage.py migrate`
        * Create view function in `views.py`
        * Create HTMl template in `templates` directory
        * Configure URL routing in `urls.py` to link view with web URL
    5. Testing and deployment
        * Test by running the server with `python manage.py runserver`
        * Deploy app to hosting platform (Ex: Pacil Web Service)

- Diagram for client requests in Django
```mermaid
graph TD
    A[Client] --> B[urls.py]
    B --> C[views.py]
    C --> D[models.py]
    C --> E[Template HTML]
    D --> C
    E --> F[Response HTML]
    F --> A[Client]
    
    subgraph Django MVT Model
      B[urls.py] --> |"Match URL with appropriate view"| C
      C[views.py] --> |"Fetch data from model (Optional)"| D
      C[views.py] --> |"Process and send data to HTML template"| E
      E[Template HTML] --> |"Return a view based on data"| F
    end
```
- Explanation:
    1. **Client**: The client sends an HTTP request to the Django server.
    2. **urls.py**: Django uses urls.py to match the requested URL 3.with the corresponding view function in views.py.
    3. **views.py**: The view function in views.py handles the request. It may need to fetch data from the database using models.py (optional).
    4. **models.py**: If the view requires interaction with the database, it retrieves or updates data through models.py.
    5. **Template HTML**: Once the data is processed, the view sends it to a template (HTML) for rendering.
    6. **Response HTML**: The template generates an HTML response based on the data provided.
    7. **Client**: The rendered HTML is sent back to the client, where it's displayed as a web page.

- Role of `git` in software development
    - **Version control**: Git keeps a detailed history of all changes made to the code, helping developers track progress.
    - **Collaboration**: It allows multiple developers to work on the same project simultaneously without conflicts.
    - **Branching**: Git lets developers create separate branches to work on new features or fixes without affecting the main codebase.
    - **Merging**: Changes from different branches can be combined, even if multiple developers are working on the same files.
    - **Conflict resolution**: Git helps identify and resolve conflicts when two developers make different changes to the same part of the code.
    - **Backup**: It provides a secure, distributed backup of the codebase, ensuring code is not lost.
    - **Rollback**: Developers can revert to previous versions of the project if something goes wrong. 
    - **Code review**: Git facilitates peer reviews through pull requests, improving code quality and collaboration.

- Why Django?
    - **Open Source**: Django is freely available and allows developers to modify the code, promoting flexibility and community collaboration.
    - **Fast**: Its built-in tools and automation features help developers quickly move from concept to deployment.
    - **Fully Loaded**: Django comes with essential features like authentication and content management out of the box, reducing the need for external tools.
    - **Secure**: With built-in protections against common threats, Django ensures high security for web applications.
    - **Scalable**: Django’s architecture supports easy scaling, making it ideal for both small projects and large-scale applications.
    - **Versatile**: Django’s flexibility allows it to be used for various web applications, from CMS to e-commerce platforms.

- Django ORM
    - Django's model is called an **Object-Relational Mapping (ORM)** because it allows developers to interact with the database using Python objects instead of SQL. The ORM maps Python classes (representing database tables) and their attributes (columns) to database records. This abstraction simplifies database operations like querying and updating data, making it more intuitive and efficient for developers to work with relational databases.

## Tugas 3 <a id="tugas-3"></a>
- Importance of data delivery in implementing a platform
    1. **Real-Time Information Availability**: Ensures that data accessed by users is always current and accurate, providing a seamless experience, especially in platforms like e-commerce or financial systems.
    2. **System Integration**: Facilitates smooth communication between different components of the platform, such as databases, front-end applications, and third-party services, ensuring they work together efficiently.
    3. **Data-Driven Decision Making**: Allows for timely delivery of data to analytics or machine learning systems, enabling better insights and more informed decision-making for business strategies.
    4. **Scalability and Reliability**: Supports the platform’s ability to handle growing user demands and large volumes of data without compromising on performance or speed.
    5. **Security and Privacy**: Ensures the safe transmission of sensitive data, such as personal or financial information, by implementing encryption and authentication protocols.
    6. **Efficiency of Resources**: Reduces the time and system resources required for data transfer, optimizing network usage and operational costs, making the platform more cost-effective.

- XML or JSON?
    - XML *Pros*:
        1. **Rich Structure**: XML supports complex data structures with nested hierarchies, making it useful for documents where structure is a priority.
        2. **Metadata with Attributes**: XML allows the use of attributes to store additional information about the data, which can be useful for more detailed data descriptions.
        3. **Standardized Schema Support**: XML has standardized schema languages (e.g., XSD) for defining structure and validating data.
        4. **Extensive Tooling**: There are many mature tools and libraries for processing, transforming (e.g., XSLT), and validating XML, making it valuable for certain legacy systems.
    - JSON *Pros*:
        1. **Simplicity and Readability**: JSON is lightweight, less verbose, and easier to read and write compared to XML. It has a simpler structure (key-value pairs) which reduces complexity.
        2. **Native Support in JavaScript**: JSON integrates seamlessly with JavaScript, making it the default choice for web applications. It is easily parsed and manipulated in JavaScript.
        3. **Faster Parsing**: JSON’s simpler structure makes it faster to parse than XML. Many modern programming languages, including JavaScript, Python, and Go, have native support for handling JSON.
        4. **Compactness**: JSON is less verbose, so it generally results in smaller file sizes, leading to faster transmission over networks.
    - Why is JSON More Popular than XML?
        - While XML is still useful for complex document structures and systems that require schema validation, JSON is preferred for modern web development and data exchange due to its <u>simplicity, efficiency, and tight integration with JavaScript</u>. This ease of use and performance advantage explains why JSON has become more popular in contemporary applications.

- `is_valid()` method in Django
    - Function of `is_valid()`:
        1. **Validation Check**: The primary function of is_valid() is to validate the data submitted through the form. It checks if all fields in the form meet the validation rules specified in the form’s model or custom validations (e.g., required fields, data type constraints, specific format checks).
        2. **Error Handling**: If the data is valid, is_valid() returns True; otherwise, it returns False and stores error messages related to the invalid fields in a form attribute called form.errors. This allows developers to easily display validation errors back to the user.
        3. **Data Cleaning**: In addition to validation, is_valid() also triggers the clean() method, which cleans and normalizes the form data. This ensures that the data is in a usable format before being processed or saved to the database.
    - Why is `is_valid()` necessary:
        1. **Data Integrity**: Using is_valid() ensures that only valid and clean data is processed, which helps maintain data integrity in the application. Invalid or corrupt data can lead to errors, security vulnerabilities, or broken functionality.
        2. **User Feedback**: It allows developers to provide feedback to users when they submit incorrect or incomplete data. The errors generated can be used to highlight issues, helping users correct them before resubmission.
        3. **Prevents Invalid Database Entries**: Without this method, invalid data might be saved to the database, leading to integrity issues. By validating before saving, is_valid() prevents saving incorrect or malformed data.
        4. **Automatic Handling of Validation**: Django provides built-in form validation (such as checking for required fields, data types, etc.), and is_valid() simplifies the process by running all the necessary validation checks with a single method call.

- Importance of `csrf_token`
    - Why do we need `csrf_token` in making a Django form?
    In Django, the csrf_token is necessary to protect against Cross-Site Request Forgery (CSRF) attacks. CSRF occurs when an attacker tricks a logged-in user into submitting a form or performing an action on a website without their knowledge. This could lead to unintended actions, such as changing user settings, transferring funds, or altering important data.

        Importance of csrf_token:
        - CSRF Attack Protection: The csrf_token acts as a unique, secret value that ensures the request comes from a legitimate user who accessed the form through the authorized website. Without this token, malicious websites could send unauthorized requests using the user's session.

        - Prevents Unauthorized Form Submissions: When a form submission does not include the correct csrf_token, Django rejects the request. This prevents attackers from submitting forged forms on behalf of the user.
        
    - What Happens Without csrf_token?
    Without a csrf_token, an attacker could exploit CSRF by crafting a malicious form and tricking a user into submitting it. The form would perform unauthorized actions like changing data or executing commands on behalf of the victim.

    - How Can Attackers Exploit This?
    An attacker can use a **Cross-Site Request Forgery (CSRF)** attack in combination with an **Insecure Direct Object Reference (IDOR)** vulnerability. IDOR occurs when an application allows users to access or modify data based on object IDs in the URL without proper authorization checks.

    - CSRF + IDOR exploit example:
        - Example URL: `http://targetsite.com/update_profile/3/  # Attacker's user ID`
        Since the URL exposes user_id, an attacker can change the user_id parameter to modify other users’ profiles by simply iterating over IDs
        `http://targetsite.com/update_profile/2/  # Changes email for user ID 2 to attacker@example.com`
        - If the form lacks a `csrf_token`, the attacker can trick the victim into  visiting a malicious website or clicking a button that triggers this unauthorized request. This combines the CSRF vulnerability (no `csrf_token`) with the IDOR vulnerability (lack of proper authorization checks), allowing the attacker to modify another user's sensitive information.

- Implementing Checklists
    1. Create Input Form to add Object Model
        a. Create `base.html` inside a new `templates` directory
        ```
        {% load static %}
        <!DOCTYPE html>
        <html lang="en">
            <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            {% block meta %} {% endblock meta %}
            </head>

            <body>
            {% block content %} {% endblock content %}
            </body>
        </html>
        ```
        b. Create `forms.py` in project's directory
        ```
        from django.forms import ModelForm
        from main.models import Product

        class ProductRequestForm(ModelForm):
            class Meta:
                model = Product
                fields = ['name', 'price', 'description', 'category', 'bitterness']
        ```
        c. Create a new view for input form in `views.py`
        ```
        ...
        def create_product_request(request):
            form = ProductRequestForm(request.POST or None)
            
            if form.is_valid() and request.method == "POST":
                form.save()
                return redirect('main:show_main')
            
            context = {'form': form}
            return render(request, "create_product_request.html", context)
        ...
        ```
        d. Add new URL for the form in `urls.py` in app's directory
        ```
        ...
        urlpatterns = [
            path('', show_main, name='show_main'),
            path('create-product-request', create_product_request, name='create_product_request'),
        ]
        ....
        ```
    2. Create 4 view functions to show registered Objects in XML and JSON format in `views.py`
        a. View XML:
        ```
        ...
        def show_xml(request):
            data = ItemEntry.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        ...
        ```
        b. View JSON:
        ```
        ...
        def show_json(request):
            data = ItemEntry.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        ...
        ```
        c. View XML by ID:
        ```
        ...
        def show_xml_by_id(request, id):
            data = ItemEntry.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        ...
        ```
        d. View JSON by ID:
        ```
        ...
        def show_json_by_id(request, id):
            data = ItemEntry.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        ...
        ```
    3. Add URL routing for new view functions in `urls.py` in the app's directory
    ```
    from django.urls import path
    from main.views import show_main, create_product_request, show_json, show_xml, show_json_by_id, show_xml_by_id

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-product-request', create_product_request, name='create_product_request'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id')
    ]
    ```

- Access URLs with Postman
    1. XML
    ![show_xml](images/xml.png)
    2. XML by ID
    ![show_xml_by_id](images/xmlById.png)
    3. JSON
    ![show_json](images/json.png)
    4. JSON by ID
    ![show_json_by_id](images/jsonById.png)

## Tugas 4 <a id="tugas-4"></a>

- `HttpResponseRedirect():` VS `redirect():`
    1. `HttpResponseRedirect():`
        - **Direct Class for Redirection**: This is a class in Django that explicitly creates an HTTP response with status code 302 to indicate a redirection.
        - **Requires Full URL**: You must provide a complete URL path as the argument, which can be static or dynamically generated based on user input or logic.
        - **Control Over URL**: This is useful when you need direct control over the URL or if you're working with external URLs or generating URLs dynamically.
        - **Example**:
        ```
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect('/new-path/')
        ```

    2. `redirect():`
        - **Shortcut Function**: Django provides this helper function that simplifies the redirection process by allowing you to pass a variety of inputs.
        - **Flexible Inputs**: Unlike HttpResponseRedirect(), this function can accept a full URL, a view name (which Django will resolve to a URL), or even a model instance, which Django can use to create the appropriate redirect URL. This flexibility makes it easier to use in most cases.
        - **Simpler and Concise**: This function is especially useful when working with named views or model instances because it reduces boilerplate code.
        - **Example**:
        ```
        from django.shortcuts import redirect
        return redirect('home')  # Redirect to the view named 'home'
        ```
    2. Summary:
        - `HttpResponseRedirect()` gives explicit control and is useful for simple, direct URL handling.
        - `redirect()` is a more convenient and flexible choice because it can handle different types of inputs (URLs, view names, or models) and automatically generates the appropriate redirect URL. It’s widely used in Django projects for its simplicity.
- Steps to connect models (`Product` with `User`)
    1. Importing the `User` Model
        `from django.contrib.auth.models import User`
        This import makes the User model available for use in other models or views, allowing products to be associated with specific users.
    2. Adding a ForeignKey Field in the Product Model
        In the Product model, a ForeignKey field can be added to establish a many-to-one relationship with the User model:
        ```
        # models.py
        class Product(models.Model):
            ...
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            ...
        ```
        Explanation:
        - ForeignKey: Defines a many-to-one relationship where each product is linked to a single user, but a user can have many products.
        - on_delete=models.CASCADE: Ensures that if the related user is deleted, all products associated with that user will also be removed. This behavior helps maintain referential integrity in the database.
    3. Migration Steps
        After adding a new field to the model, the changes must be reflected in the database by creating and applying migrations with:
        `python manage.py ma4kemigrations` then `python manage.py migrate`
    4. Usage in app
        By connecting the `Product` model with the `User` model, the main app can filter products based on the current user, ensuring that only products belonging to that user are displayed.
        ```
        # views.py
        @login_required(login_url='/login')
        def show_main(request):
            product_requests = Product.objects.filter(user=request.user)
        ```
- _Authentication_ VS _Authorization_
    1. **Authentication** is the process of verifying a user's identity, typically through credentials like a username and password.
    2. **Authorization** refers to determining what an authenticated user is allowed to do, such as accessing specific resources or performing certain actions.
    3. When a user logs in, authentication is performed by verifying the user's credentials. If valid, Django creates a session for the user and marks them as authenticated.
    4. Django Implementation:
        - Authentication in Django is handled through the built-in authentication system (`django.contrib.auth`). It verifies user credentials using methods like `authenticate()` and `login()`.
        - Authorization is managed via permissions and groups. After authentication, Django checks user permissions (e.g., using `user.has_perm()`) to determine if they are authorized to perform specific actions.

- How Django Manages User Sessions and Cookie Security
    1. Preserving user login state in Django
        - **Session-based Authentication**: When a user logs in, Django creates a session to store the user's authentication state. This session is linked to a session ID, which is stored in the user's browser as a cookie.
        - **Session ID in Cookies**: The cookie containing the session ID is sent back and forth between the client and server with each request. Django uses this session ID to retrieve the user's session data and remember that the user is logged in.
        - **How Django Uses Sessions**: Django doesn’t store sensitive information like passwords in cookies; it only stores the session ID. The actual session data, including the user's login status, is stored on the server.
    2. Other Uses of Cookies
        - **Preferences**: Cookies can store user preferences, like language settings or theme choices, so that the user experience is personalized across sessions.
        - **Tracking**: Cookies can be used for analytics, tracking user behavior on websites, or remembering items in a shopping cart.
        - **Authentication Tokens**: Cookies are used for storing tokens in authentication mechanisms, such as JWT (JSON Web Tokens), for stateless user authentication.
    3. Cookie Security
        - **Not All Cookies Are Safe**: Cookies can pose security risks, especially if they are not properly protected. For instance, if cookies contain sensitive information and are not encrypted, they can be intercepted and misused.
        - **Cookie Flags**: To enhance cookie security, Django supports setting flags like `HttpOnly`, `Secure`, and `SameSite`:
            - `HttpOnly` prevents client-side JavaScript from accessing cookies, mitigating the risk of cross-site scripting (XSS) attacks.
            - `Secure` ensures that cookies are only transmitted over HTTPS, protecting them from being intercepted over insecure connections.
            - `SameSite` helps prevent cross-site request forgery (CSRF) by restricting how cookies are sent with cross-site requests.

- Implementing Checklist
    1. Creating User Registration Form
        - Goal: Restrict access to the main page to logged-in users only.
        - Steps:
            1. Import `UserCreationForm` and `messages`.
            ```
            from django.contrib.auth.forms import UserCreationForm
            from django.contrib import messages
            ```
            2. Create a `register()` function in `views.py` to handle user registration.
            ```
            def register(request):
            form = UserCreationForm()
            
            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Account has been successfully registered")
                    return redirect('main:login')
            context = {'form': form}
            return render(request, "register.html", context)
            ```
            3. Create a `register.html` template to display the registration form. ==> [register.html](./main/templates/register.html)
            4. Add a register path to `urls.py` to access the registration page.
            ```
             urlpatterns = [
                ...
                path('register/', register, name='register'),
            ]
            ```
    2. Creating Login Form
        - Goal: Allow registered users to log in to the app.
        - Steps:
            1. Import `AuthenticationForm`, `authenticate`, and `login`.
            ```
            from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
            from django.contrib.auth import authenticate, login
            ```
            2. Create a `login_user()` function in `views.py` to handle the login process.
            ```
            def login_user(request):
            if request.method == 'POST':
                form = AuthenticationForm(data=request.POST)
                
                if form.is_valid():
                    user = form.get_user()
                    login(request, user)
                    response = HttpResponseRedirect(reverse("main:show_main"))
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response
                
            else:
                form = AuthenticationForm(request)
            context = {'form': form}
            return render(request, "login.html", context)
            ```
            3. Create a `login.html` template to display the login form. ==> [login.html](./main/templates/login.html)
            4. Add a login path to `urls.py` to access the login page.
            ```
            from main.views import login_user
            ...
            urlpatterns = [
            ...
            path('login/', login_user, name='login'),
            ]
            ```
    3. Implementing Logout Mechanism
        - Goal: Enable users to log out of the application.
        - Steps:
            1. Import logout in `views.py`.
            2. Create a `logout_user()` function to handle the logout process.
            ```
            from django.contrib.auth import logout
            ```
            3. Add a logout button on the main page (`main.html`) and add a logout path in `urls.py` to handle the logout.
            ```
            def logout_user(request):
                logout(request)
                return redirect('main:login')
            ```
            ```
            from main.views import logout_user
            ...
            urlpatterns = [
            ...
            path('logout/', logout_user, name='logout'),
            ]
            ```
    4. Restricting Access to Main Page
        - Goal: Ensure the main page can only be accessed by logged-in users.
        - Steps:
            1. Import `login_required` to protect page access.
            ```
            from django.contrib.auth.decorators import login_required
            ```
            2. Add the `@login_required(login_url='/login')` decorator above the `show_main()` function to require login.
    5. Using Cookies to Track Last Login
        - Goal: Display the user's last login time using cookies.
        - Steps:
            1. Add the `last_login` cookie in the `login_user()` function.
            ```
            def login_user(request):
                ...
                if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
                ...
            ```
            2. Display the `last_login` information on the main page by modifying the `main.html` template.
            ```
            ...
            <a href="{% url 'main:logout' %}">
                <button>Logout</button>
                <h5>Sesi terakhir login: {{ last_login }}</h5>
            </a>
            ```
            3. Remove the `last_login` cookie upon logout by modifying the `logout_user()` function.
            ```
            def logout_user(request):
                logout(request)
                response = HttpResponseRedirect(reverse('main:login'))
                response.delete_cookie('last_login')
                return response
            ```
    6. Linking the `Product` Model with User
        - Goal: Associate each Product with the user who created it.
        - Steps:
            1. Import User and add a ForeignKey relationship to the `Product` model.
            ```
            ...
            from django.contrib.auth.models import User
            class Product(models.Model):
                user = models.ForeignKey(User, on_delete=models.CASCADE)
            ...
            ```
            2. Modify the `create_product_request()` function to save the product request with the currently logged-in user.
            ```
            def create_product_request(request):
                form = ProductRequestForm(request.POST or None)
                
                if form.is_valid() and request.method == "POST":
                    product_request = form.save(commit=False)
                    product_request.user = request.user
                    product_request.save()
                    return redirect('main:show_main')
                
                context = {'form': form}
                return render(request, "create_product_request.html", context)
            ```
            3. Modify the `show_main()` function to display only the product requests that belongs to the logged-in user.
            ```
            def show_main(request):
                product_requests = Product.objects.filter(user=request.user)
            ```
    7. Migrating Models
        - After making changes to the models, run migrations by:
            1. Running `python manage.py makemigrations`.
            2. Set a default user when prompted (1 in this case).
            3. Apply migrations using `python manage.py migrate`.
    8. Preparing for Production
        - Set the environment for production by updating the `DEBUG` setting in `settings.py`.
        ```
        import os
        ...
        PRODUCTION = os.getenv("PRODUCTION", False)
        DEBUG = not PRODUCTION
        ...
        ```