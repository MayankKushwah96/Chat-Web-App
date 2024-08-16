# Chat Application

## Description

This project is a Django-based chat application that allows users to communicate in real time. Users can register, log in, and send messages to each other. The application uses Django for the web framework and Bootstrap for styling.

### Features

- **User Authentication**:
  - Registration: New users can create an account.
  - Login: Existing users can log in.
  - Logout: Users can log out.

- **Real-time Messaging**:
  - Send and receive messages in real-time.
  - View chat history.

- **User Profiles**:
  - Display the logged-in user's username.

- **Responsive Design**:
  - Styled with Bootstrap for a modern and responsive user interface.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/MayankKushwah96/Chat-Web-App.git
    ```

2. Navigate into the project directory:
    ```bash
    cd Chat_Application
    ```

3. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate 
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply the database migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser for accessing the Django admin panel (optional):
    ```bash
    python manage.py createsuperuser
    ```

7. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

## Running the Application

1. Make sure you're in the project directory and the virtual environment is activated.
2. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

3. Open a web browser and go to `http://127.0.0.1:8000` to access the application.

## Usage

1. **Registration and Login**:
   - Navigate to the registration page to create a new account.
   - Log in using your credentials to access the chat functionality.

2. **Real-time Messaging**:
   - Once logged in, you can send and receive messages in real-time.
   - View your chat history.

## Project Structure

- `myproject/`: Root directory of the Django project.
- `chat/`: Django app handling the chat functionality.
  - `views.py`: Contains views for handling user interactions and chat messages.
  - `models.py`: Defines models for storing user and chat data.
  - `forms.py`: Contains the form for user registration and login.
  - `urls.py`: URL routing for the chat app.
  - `templates/chat/`: HTML templates for the chat views.
  - `requirements.txt`: File listing the project's dependencies.

## Dependencies

- Python
- Django
- Bootstrap (for styling)
- Channels (for real-time communication)
- Other dependencies listed in `requirements.txt`
