# bean-scape
Platform Based Programming (PBP) Course --- Tugas Individu 

## Bookmarks
- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)
- [Tugas 4](#tugas-4)
- [Tugas 5](#tugas-5)
- [Tugas 6](#tugas-6)

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

## Tugas 5 <a id="tugas-5"></a>

* CSS Selector Priority
    1. **Specificity Hierarchy**: CSS selectors have a specificity hierarchy that determines which styles are applied when multiple selectors target the same element. The order of priority, from highest to lowest, is:
        - Inline styles
        - IDs
        - Classes, attributes, and pseudo-classes
        - Elements and pseudo-elements
    2. **Inline Styles**: Styles applied directly to an HTML element using the `style` attribute have the highest priority.
    3. **IDs**: Selectors using the ID of an element (e.g., `#myElement`) have the next highest specificity.
    4. **Classes, Attributes, and Pseudo-classes**: These include selectors like `.myClass`, `[type="text"]`, or `:hover`.
    5. **Elements and Pseudo-elements**: Selectors using element names (e.g., `div`) or pseudo-elements (e.g., `::before`) have the lowest specificity.
    6. **Cascading Rule**: When selectors have equal specificity, the rule that appears later in the CSS file takes precedence.
    7. **!important**: The `!important` declaration overrides normal specificity rules and should be used sparingly.

* Importance of *responsive design* and its example
    1. **Importance of Responsive Design**:
        - **Device Diversity**: With the proliferation of devices with varying screen sizes (smartphones, tablets, desktops), responsive design ensures a consistent user experience across all platforms.
        - **Mobile-First Approach**: As mobile internet usage surpasses desktop, responsive design caters to this shift in user behavior.
        - **SEO Benefits**: Search engines favor mobile-friendly websites, improving search rankings.
        - **Cost-Effective**: It's more efficient to maintain one responsive site than separate mobile and desktop versions.
        - **User Experience**: Improves user satisfaction by providing optimal viewing and interaction experience across devices.

    2. **Examples**:
        - **Responsive Design**:
            - Amazon: Adapts seamlessly from desktop to mobile, maintaining functionality and readability.
            - The New York Times: Content layout adjusts fluidly across devices.
        - **Non-Responsive Design**:
            - Old government websites: Often designed for desktop only, requiring horizontal scrolling on mobile.
            - Legacy business sites: May have separate mobile versions instead of a single responsive design.

* Difference between *margin*, *border*, and *padding*. Steps in implementing
    1. **Margin**:
        - **Definition**: Space outside the element's border.
        - **Usage**: Creates space between elements.
        - **Implementation**: `margin: 10px;` or `margin-top: 5px;`

    2. **Border**:
        - **Definition**: Line surrounding the element's content and padding.
        - **Usage**: Visually separates elements or adds decorative lines.
        - **Implementation**: `border: 1px solid black;` or `border-bottom: 2px dashed red;`

    3. **Padding**:
        - **Definition**: Space between the element's content and its border.
        - **Usage**: Creates space within an element.
        - **Implementation**: `padding: 15px;` or `padding-left: 20px;`

    4. **Implementation Example**:
        ```css
        .box {
            margin: 10px;
            border: 2px solid blue;
            padding: 15px;
        }
        ```

* Concept of *flex box* and *grid layout* and its usage
    1. **Flexbox**:
        - **Concept**: One-dimensional layout model for arranging items in rows or columns.
        - **Key Features**:
            - Flexible container and item sizes
            - Easy alignment and distribution of space
            - Dynamic ordering of items
        - **Usage**:
            - Navigation menus
            - Card layouts
            - Centering content
        - **Implementation**:
            ```css
            .container {
                display: flex;
                justify-content: space-between;
            }
            ```

    2. **Grid Layout**:
        - **Concept**: Two-dimensional layout system for rows and columns simultaneously.
        - **Key Features**:
            - Precise control over both row and column layouts
            - Gap control between grid items
            - Overlapping capabilities
        - **Usage**:
            - Complex page layouts
            - Image galleries
            - Responsive design without media queries
        - **Implementation**:
            ```css
            .container {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 10px;
            }
            ```

    3. **Comparison**:
        - Flexbox is ideal for one-dimensional layouts (either row or column).
        - Grid is perfect for two-dimensional layouts (rows and columns simultaneously).
        - Both can be used together for complex, responsive designs.

- Implementing Checklists
    1. **Implementing Functions to Edit and Delete Products**
        - Goal: Enable users to edit and delete existing products.
        - Steps:
            1. Edit Product:
                - Create an edit view function in `views.py` to handle the product update.
                ```
                def edit_product(request, id):
                # Get product from id
                product = Product.objects.get(pk = id)
                
                # Set product as instance of forms
                form = ProductRequestForm(request.POST or None, instance=product)
                
                if form.is_valid() and request.method == "POST":
                    # Save form
                    form.save()
                    # Return to main page
                    return HttpResponseRedirect(reverse('main:show_main'))
                
                context = {'form': form}
                return render(request, "edit_product.html", context)
                ```
                - Add an edit route in `urls.py`.
                ```
                path('edit_product/<int:product_id>/', edit_product, name='edit_product'),
                ```
            2. Delete Product:
                - Create a delete view function in `views.py` to handle the deletion.
                ```
                def delete_product(request, id):
                # Get product from id
                product = Product.objects.get(pk = id)
                
                # Delete product
                product.delete()
                
                # Return to main page
                return HttpResponseRedirect(reverse('main:show_main'))
                ```
                - Add a delete route in `urls.py`.
                ```
                path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
                ```
    2. **Customizing HTML Templates**
        - Goal: Enhance the visual appeal of login, register, and product pages using CSS or CSS frameworks.
        - Steps:
            1. Use a CSS Framework: Link Tailwind in templates.
            2. Login, Register, Request Product Pages: Apply attractive styling by customizing forms and buttons.
                - [login.html](main/templates/login.html)
                - [register.html](main/templates/register.html)
                - [create_product_request.html](main/templates/create_product_request.html)
    3. Customizing the Product List Page
        - Goal: Make the product list page visually engaging and responsive. Handle cases where no products exist.
        - Steps:
            1. Empty Product List: Show an image and a message when no products exist. ([main.html](main/templates/main.html))
            ```
            {% else %}
            <div class="text-center py-8">
                <div class="max-w-xs mx-auto mb-6">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="w-full h-auto">
                        <defs>
                            <style>
                                .coffee-dark { fill: #6F4E37; }
                                .coffee-medium { fill: #967259; }
                                .coffee-light { fill: #B87A5B; }
                            </style>
                        </defs>
                        <!-- Empty Coffee Cup -->
                        <path class="coffee-medium" d="M384 64H128c-17.7 0-32 14.3-32 32v64c0 17.7 14.3 32 32 32h256c17.7 0 32-14.3 32-32V96c0-17.7-14.3-32-32-32z"/>
                        <path class="coffee-dark" d="M96 160v192c0 35.3 28.7 64 64 64h192c35.3 0 64-28.7 64-64V160H96zm64-32h192c17.7 0 32-14.3 32-32s-14.3-32-32-32H160c-17.7 0-32 14.3-32 32s14.3 32 32 32z"/>
                        <!-- Steam -->
                        <g class="animate-steam">
                            <path class="coffee-light" d="M200 48c0-8.8-7.2-16-16-16s-16 7.2-16 16 7.2 16 16 16 16-7.2 16-16zM256 16c0-8.8-7.2-16-16-16s-16 7.2-16 16 7.2 16 16 16 16-7.2 16-16zM312 48c0-8.8-7.2-16-16-16s-16 7.2-16 16 7.2 16 16 16 16-7.2 16-16z">
                                <!-- Animation handled by global.css -->
                            </path>
                        </g>
                        <!-- Plus Sign -->
                        <circle class="coffee-light" cx="256" cy="256" r="48"/>
                        <rect class="coffee-dark" x="248" y="224" width="16" height="64" rx="8"/>
                        <rect class="coffee-dark" x="224" y="248" width="64" height="16" rx="8"/>
                    </svg>
                </div>
                <p class="text-xl text-gray-600 mb-4">Your coffee inventory is empty!</p>
                <p class="text-gray-500 mb-6">Start by adding your favorite coffee products.</p>
                <a href="{% url 'main:create_product_request' %}" 
                class="inline-block bg-coffee-medium hover:bg-coffee-dark text-white font-bold py-3 px-6 rounded-lg transition-colors duration-300 shadow-md hover:shadow-lg transform hover:-translate-y-1">
                    Add Your First Product
                </a>
            </div>
            ```
            2. Display Products in Cards: Show product details using card components with edit and delete buttons.
                - [card_product.html](main/templates/card_product.html)
    4. Adding a Responsive Navigation Bar (Navbar)
        - Goal: Create a responsive navigation bar that adapts to both desktop and mobile views.
        - Steps:
            1. Create a Navbar: Include navigation links for the main features like login, logout, product list, etc.
                - [navbar.html](templates/navbar.html)
            2. Responsive Design: Use CSS or framework classes to make the navbar responsive on mobile devices
            ```
            ...
            <div class="mobile-menu hidden md:hidden px-4 w-full md:max-w-full bg-coffee-dark">
            ...
            ```

## Tugas 6 <a id="tugas-6"></a>

* Benefits of using JavaScript in web application development:
    1. **Interactivity**: JavaScript makes web elements more responsive. For example, it can validate form inputs or display instant messages when buttons are clicked, providing users with immediate feedback for a better user experience.
    2. **Dynamic Page Updates**: Developers can modify webpage content and appearance in real-time without page reloads. Elements can be added, removed, or edited based on user interactions, allowing for dynamic content updates.
    3. **Animations and Visual Effects**: JavaScript enables the creation of animations and visual effects like transitions or color changes on hover, enhancing the visual appeal and interactivity of websites.
    4. **Data Exchange**: JavaScript facilitates seamless data retrieval and submission to servers without page refreshes using AJAX, resulting in faster and smoother user experiences.
    5. **Code Examples**:
        - AJAX GET: Functions like `getProductEntries()` and `refreshProductEntries()` fetch product data from the server and dynamically update HTML elements.
        - AJAX POST: The `addProductEntry()` function sends data to the server using `fetch()` without refreshing the page when a form is submitted.

* Purpose of await with `fetch()`:
    - The `await` keyword is essential when using `fetch()` for asynchronous operations. It ensures JavaScript waits for the server response before proceeding with code execution. Without `await`, JavaScript would continue executing subsequent code before receiving the server response, potentially causing errors when trying to manipulate unavailable data.

* Necessity of `csrf_exempt` decorator for AJAX POST views:
    - The `csrf_exempt` decorator exempts AJAX POST views from Django's default CSRF (Cross-Site Request Forgery) protection. While Django typically requires CSRF tokens for POST requests as a security measure, AJAX requests may not include these tokens. Using ``csrf_exempt` allows POST requests without CSRF verification, simplifying AJAX handling but potentially reducing security.

* Backend vs. Frontend data validation:
    1. While frontend validation using JavaScript improves user experience, backend validation is crucial for ensuring data security and integrity. Frontend validation can be bypassed by disabling JavaScript or modifying requests, so backend validation ensures all data entering the server is properly sanitized and safe for database storage.
    2. **Code Examples**:
        - `add_product_ajax()` view validates and processes form data before saving it to the database using `strip_tags`

* Implementing Checklists
    1. **Creating Data Reception and Addition Functions via AJAX**
        - The first step is to develop a function in views.py that processes AJAX POST requests. This function receives product data sent through AJAX, sanitizes it, adds it to the database, and sends back a response.
        ```
        @csrf_exempt
        @require_POST
        def add_product_ajax(request):
            user = request.user
            name = strip_tags(request.POST.get('name'))
            price = request.POST.get('price')
            description = strip_tags(request.POST.get('description'))
            category = request.POST.get('category')
            bitterness = request.POST.get('bitterness')
            
            new_product = Product(
                user=user,
                name=name,
                price=price,
                description=description,
                category=category,
                bitterness=bitterness
            )
            new_product.save()
            
            return HttpResponse(b"CREATED", status=201)
        ```
        - This function captures product details transmitted from a modal (such as product name, description, price, etc.), cleans the data, then incorporates it into the Product model.

2. **Setting Up URL Routing**
    - After creating the AJAX product addition function, a new path must be added to urls.py to make this view accessible.
    ```
    urlpatterns = [
        ...
        path('add-product-ajax', add_product_ajax, name='add_product_ajax'),
        ...
    ]
    ```
3. **Displaying Data in the Main Template**
    - Create HTML elements in main.html that serve as containers for showing products. Use a specific ID, such as product_cards, which JavaScript will populate dynamically.
    ```
    <div id="product_cards"></div>
    ```
4. **Developing Scripts for Data Retrieval and Display**
    - To show existing products, include a script in main.html that uses fetch to retrieve product data in JSON format from the server, then displays it in the previously created HTML elements.
    ```
    async function getProductEntries() {
        return fetch("{% url 'main:show_json' %}").then((res) => res.json());
    }

    async function refreshProductEntries() {
            document.getElementById("product_cards").innerHTML = "";
            document.getElementById("product_cards").classname = "";
            const productEntries = await getProductEntries();
            let htmlString = "";
            let classNameString = "";

            if (productEntries.length === 0) {
                classNameString = "mt-5 text-center py-8";
                htmlString = `
                    <div class="max-w-xs mx-auto mb-6">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -50 512 512" class="w-full h-auto">
                            <defs>
                                <style>
                                    .coffee-dark { fill: #6F4E37; }
                                    .coffee-medium { fill: #967259; }
                                    .coffee-light { fill: #B87A5B; }
                                </style>
                            </defs>
                            <!-- Empty Coffee Cup -->
                            <path class="coffee-medium" d="M384 64H128c-17.7 0-32 14.3-32 32v64c0 17.7 14.3 32 32 32h256c17.7 0 32-14.3 32-32V96c0-17.7-14.3-32-32-32z"/>
                            <path class="coffee-dark" d="M96 160v192c0 35.3 28.7 64 64 64h192c35.3 0 64-28.7 64-64V160H96zm64-32h192c17.7 0 32-14.3 32-32s-14.3-32-32-32H160c-17.7 0-32 14.3-32 32s14.3 32 32 32z"/>
                            <!-- Steam -->
                            <g class="animate-steam" transform="translate(256, -40)">
                                <path class="coffee-light" d="M200 48c0-8.8-7.2-16-16-16s-16 7.2-16 16 7.2 16 16 16 16-7.2 16-16zM256 16c0-8.8-7.2-16-16-16s-16 7.2-16 16 7.2 16 16 16 16-7.2 16-16zM312 48c0-8.8-7.2-16-16-16s-16 7.2-16 16 7.2 16 16 16 16-7.2 16-16z"/>
                            </g>
                            <!-- Plus Sign -->
                            <circle class="coffee-light" cx="256" cy="256" r="48"/>
                            <rect class="coffee-dark" x="248" y="224" width="16" height="64" rx="8"/>
                            <rect class="coffee-dark" x="224" y="248" width="64" height="16" rx="8"/>
                        </svg>
                    </div>
                    <p class="text-xl text-gray-600 mb-4">Your coffee inventory is empty!</p>
                    <p class="text-gray-500 mb-6">Start by adding your favorite coffee products.</p>
                    <button onclick="showModal()" 
                            class="inline-block bg-coffee-medium hover:bg-coffee-dark text-white font-bold py-3 px-6 rounded-lg transition-colors duration-300 shadow-md hover:shadow-lg transform hover:-translate-y-1">
                        Add Your First Product
                    </button>
                `;
            }
            else {
                classNameString = "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
                productEntries.forEach((item) => {
                htmlString += `
                    <div class="bg-coffee-medium rounded-lg shadow-md p-6 relative">
                        <h2 class="text-2xl font-bold text-coffee-dark mb-1">${item.fields.name}</h2>
                        
                        <div class="flex items-center mb-3">
                            <span class="text-xl font-semibold text-coffee-dark">Rp${item.fields.price}</span>
                            <span class="ml-2 px-2 py-1 bg-coffee-light rounded-full text-sm text-coffee-dark">
                                ${item.fields.category === 'Beverage' ? 'Beverage' : 'Beans'}
                            </span>
                        </div>
                        
                        <p class="text-coffee-dark/80 mb-4 leading-relaxed">${item.fields.description}</p>
                        
                        <div class="mb-4">
                            <label class="block text-sm font-medium text-coffee-dark mb-1">Bitterness Level</label>
                            <div class="w-full bg-coffee-light rounded-full h-2">
                                <div class="bg-coffee-dark h-2 rounded-full" style="width: ${item.fields.bitterness * 10}%"></div>
                            </div>
                            <div class="flex justify-between text-xs mt-1 text-coffee-dark/70">
                                <span>Mild</span>
                                <span class="font-medium">${item.fields.bitterness}/10</span>
                                <span>Strong</span>
                            </div>
                        </div>
                        
                        <div class="absolute top-4 right-4 flex space-x-2">
                            <a href="/edit-product/${item.pk}" 
                                class="text-coffee-dark hover:text-coffee-accent transition-colors duration-300">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                                    <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                                </svg>
                            </a>
                            <a href="/delete-product/${item.pk}" 
                                onclick="return confirm('Are you sure you want to delete this item?');"
                                class="text-red-500 hover:text-red-700 transition-colors duration-300">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                                </svg>
                            </a>
                        </div>
                    </div>
                `;
                });
            }
            document.getElementById("product_cards").className = classNameString;
            document.getElementById("product_cards").innerHTML = htmlString;
        }
        refreshProductEntries();
        ```

5. **Creating an Input Modal**
    - Within main.html, develop a modal for adding new products using AJAX. This modal should contain input fields for all necessary product details.
    ```
    <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
            <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 border-b rounded-t">
                    <h3 class="text-xl font-semibold text-coffee-dark">Add New Product</h3>
                    <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
                        <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                        </svg>
                    </button>
                </div>
                <!-- Modal body -->
                <div class="px-6 py-4 space-y-6">
                    <form id="productForm" method="POST" action="{% url 'main:create_product_request' %}">
                        {% csrf_token %}
                        <div class="mb-4">
                            <label for="name" class="block text-sm font-medium text-coffee-dark">Product Name</label>
                            <input type="text" id="name" name="name" class="mt-1 block w-full border border-coffee-light rounded-md p-2 hover:border-coffee-dark" required>
                        </div>
                        <div class="mb-4">
                            <label for="price" class="block text-sm font-medium text-coffee-dark">Price (Rp)</label>
                            <input type="number" id="price" name="price" class="mt-1 block w-full border border-coffee-light rounded-md p-2 hover:border-coffee-dark" required>
                        </div>
                        <div class="mb-4">
                            <label for="description" class="block text-sm font-medium text-coffee-dark">Description</label>
                            <textarea id="description" name="description" rows="3" class="mt-1 block w-full resize-none border border-coffee-light rounded-md p-2 hover:border-coffee-dark" required></textarea>
                        </div>
                        <div class="mb-4">
                            <label for="category" class="block text-sm font-medium text-coffee-dark">Category</label>
                            <select id="category" name="category" class="mt-1 block w-full border border-coffee-light rounded-md p-2 hover:border-coffee-dark" required>
                                <option value="BEV">Beverage</option>
                                <option value="BNS">Beans</option>
                            </select>
                        </div>
                        <div class="mb-4">
                            <label for="bitterness" class="block text-sm font-medium text-coffee-dark">Bitterness (1-10)</label>
                            <input type="range" id="bitterness" name="bitterness" min="1" max="10" value="5" class="mt-1 block w-full" required oninput="updateBitternessValue()">
                            <div class="flex justify-between text-xs mt-1 text-coffee-dark/70">
                                <span>Mild (1)</span>
                                <span id="bitternessValue">5</span>
                                <span>Strong (10)</span>
                            </div>
                        </div>
                    </form>
                </div>
                <!-- Modal footer -->
                <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
                    <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
                    <button type="submit" form="productForm" class="bg-coffee-dark hover:bg-coffee-medium text-white font-bold py-2 px-4 rounded-lg">Save Product</button>
                </div>
            </div>
        </div>
    </div>
    ```
6. **Implementing Modal Control Functions**
    - Create two functions, `showModal()` and `hideModal()`, which control the visibility of the modal. These functions are triggered by buttons on the main page.
    ```
    function showModal() {
        document.getElementById('crudModal').classList.remove('hidden');
    }

    function hideModal() {
        document.getElementById('crudModal').classList.add('hidden');
    }

    document.getElementById("cancelButton").addEventListener("click", hideModal);
    ```

7. **Implementing AJAX Data Addition**
    - Develop an addProductEntry() function to send product data to the server via AJAX POST. After successful addition, the modal closes and the form resets.
    ```
    function addProductEntry() {
        fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#productForm')),
        })
        .then(response => refreshProductEntries())

        document.getElementById("productForm").reset();
        document.querySelector("[data-modal-toggle='crudModal']").click();

        return false;
    }
    ```
8. **Form Submission Event Handling**
    - Add an event listener to the modal form to handle form submissions and trigger addProductEntry().
    ```
    document.getElementById("productEntryForm").addEventListener("submit", (e) => {
        e.preventDefault();
        addProductEntry();
    });
    ```