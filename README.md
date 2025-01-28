[![Django CI](https://github.com/Goldenhubuz/unit-converter/actions/workflows/django.yml/badge.svg?branch=main)](https://github.com/Goldenhubuz/unit-converter/actions/workflows/django.yml)

# Unit Converter Project

This is a Django-based web application for converting units of measurement. The project includes both backend and frontend components and does not require a database to store results.

## Project Structure

- **manage.py**: The entry point for managing Django commands.
- **requirements.txt**: Contains a list of Python dependencies required to run the project.
- **Makefile**: Defines useful commands for managing the project environment.
- **db.sqlite3**: A sample SQLite database (not required for the application).
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **.idea/**, **.venv/**, **.git/**: IDE, virtual environment, and Git-related files and directories.

### `config/`

This directory contains the Django project's backend code.

- **__init__.py**: Marks the directory as a Python package.
- **asgi.py**: ASGI configuration for Django.
- **wsgi.py**: WSGI configuration for Django.
- **urls.py**: URL configurations for the Django application.
- **settings.py**: Configuration settings for the Django project.

### `frontend/`

This directory handles the frontend views, templates, and validation logic.

- **templates/**: Contains HTML templates for rendering the website pages.
- **__init__.py**: Marks the directory as a Python package.
- **models.py**: (Currently not in use) Placeholder for database models.
- **admin.py**: (Currently not in use) Placeholder for Django admin configurations.
- **views.py**: Contains Django views to handle user requests and provide responses.
- **tests.py**: Test cases for the application.
- **apps.py**: Application configuration.
- **migrations/**: Directory for database migrations (not needed for this project).
- **urls.py**: URL routing specific to the frontend application.
- **validators.py**: Contains input validation logic.
- **services.py**: (If applicable) Contains service-related functions and logic.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Goldenhubuz/unit-converter.git
    cd unit-converter
    ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations** (if necessary):
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage

- Enter the values and select units to convert on the homepage.
- The application provides immediate results without needing to save or store them in a database.

## Idea Source

The idea for the Expense Tracker CLI project was inspired by [roadmap.sh's Unit Converter project](https://roadmap.sh/projects/unit-converter). Visit the link to see more details and learn about similar project ideas.

### Contribution

Contributions are welcome! If you have any ideas or improvements for the game, feel free to fork the repository and submit a pull request.

### License

This project is licensed under the GPL License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [goldendevuz@gmail.com].

---

Enjoy using the Unit Converter, and happy converting!