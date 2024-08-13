# AI-Blogger
AI-Blogger for content creators to create content from youtube videos.


![Screenshot from 2024-08-13 22-52-15](https://github.com/user-attachments/assets/659b589c-4300-4c9e-a3aa-7bdfe56ae69e)

![Screenshot from 2024-08-13 22-52-24](https://github.com/user-attachments/assets/73934a49-2a9b-45db-a299-f809a2385193)

![Screenshot from 2024-08-13 22-51-33](https://github.com/user-attachments/assets/0779bdd2-1444-4ab6-ab97-f2aafb3a0bbf)



# AI Blogger

AI Blogger is a web application designed to assist content creators in generating content from YouTube videos. Users can input a YouTube video link, and the application will fetch and provide the video transcript, which can be easily copied for use in content creation.

## Features

- **Generate Content**: Input a YouTube video link and get the transcript of the video.
- **Copy Content**: Easily copy the generated content to the clipboard for convenience.
- **User Authentication**: Secure login and registration for users.
- **Admin Dashboard**: Admin can view all users and their posts.

## Technologies Used

- **Django**: Web framework for building the web application.
- **youtube-transcript-api**: Python library for fetching YouTube video transcripts.
- **BeautifulSoup**: Library for web scraping (used if you need to parse or extract specific content from HTML).

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
2. **Navigate to the project directory::**
    ```bash
    cd <project-directory>
3. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
5. **Apply migrations:**
   ```bash
   python manage.py migrate
5. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
6. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser

7. **Run the development server:**
   ```bash
  python manage.py runserver

5. **Access the application:**
   ```bash
  Open your browser and go to http://127.0.0.1:8000/.
  
Usage
1.Register/Login: Create an account or log in to access the dashboard.
2.Generate Content: Enter a YouTube video link in the provided input field and click "Generate Content" to fetch the transcript.
3.Copy Content: Click "Copy Content" to copy the generated transcript to your clipboard.

![Screenshot from 2024-08-13 22-51-48](https://github.com/user-attachments/assets/7c5da12b-3b52-4d70-a41e-cdc66c7f578a)

Requirements
The requirements.txt file includes:

Django==4.2.4
youtube-transcript-api==0.6.0
beautifulsoup4==4.12.2

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
If you want to contribute to this project, please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and passes all tests.

