# Futsal Arena Project

This project is a Django-based web application for a Futsal Arena.

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dhakalsameer/FUTURE_FS_03.git
    cd FUTURE_FS_03
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install Node.js dependencies (for Tailwind CSS):**
    ```bash
    npm install
    ```

5.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser (if you don't have one):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Build Tailwind CSS:**
    ```bash
    npm run build-tailwind
    ```

8.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be accessible at `http://127.0.0.1:8000/`.

## Project Structure

*   `futsal/`: The main Django application for the Futsal Arena.
    *   `views.py`: Contains the logic for different pages (home, pricing, about, contact, gallery).
    *   `models.py`: Defines the database models (FutsalInfo, Facility, Booking, ContactMessage, GalleryImage).
    *   `urls.py`: Defines the URL patterns for the `futsal` app.
    *   `templates/futsal/`: HTML templates for the application pages.
    *   `static/`: Static assets including Tailwind CSS source and compiled output.
*   `futsal_project/`: The main Django project configuration.
    *   `settings.py`: Project-wide settings, including database configuration, static files, and media files.
    *   `urls.py`: Project-wide URL patterns, including routes for the `futsal` app and media file serving during development.
*   `media/`: Directory for uploaded user media files (e.g., gallery images, facility images).
*   `static/`: Top-level static files (e.g., gallery images for initial setup).

## New Gallery Page

A new gallery page has been added to showcase images.

*   **URL:** `http://127.0.0.1:8000/gallery/`
*   **To add images:**
    1.  Access the Django admin panel at `http://127.0.0.1:8000/admin/`.
    2.  Log in with your administrator credentials.
    3.  Navigate to the "Futsal" app and click on "Gallery images".
    4.  Click "Add Gallery image" and upload images, adding captions if desired.
    5.  Save the images. They will then appear on the gallery page.

## Tailwind CSS

This project uses Tailwind CSS for styling.

*   The source CSS is located at `futsal/static/src/input.css`.
*   The compiled CSS is output to `futsal/static/dist/output.css`.
*   To recompile Tailwind CSS after making changes to `input.css` or Tailwind configuration, run:
    ```bash
    npm run build-tailwind
    ```
