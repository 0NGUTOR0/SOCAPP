Social Media Backend
This is a backend application for a social media platform, built with FastAPI and PostgreSQL. It provides secure RESTful APIs for user authentication, user management, 
post creation, and social interactions like liking posts and following users. The application leverages OAuth2 with JWT for authentication, SQLAlchemy for database operations, and 
supports pagination and search for efficient data retrieval.

Features
User Authentication: Secure login and registration using JWT, with password hashing for enhanced security.
User Management: APIs to create users, retrieve user details, and list users with pagination and search by name.
Post Management: CRUD operations for posts, allowing users to create, read, update, and delete their own posts.
Social Interactions: Users can like posts and follow other users, with APIs to track likes and follower counts.
Pagination and Search: Supports paginated retrieval of users and posts, with search functionality for post titles and user names.
Error Handling: Robust validation and error responses for unauthorized access, invalid inputs, and non-existent resources.

Tech Stack
Backend: FastAPI 0.110.0, SQLAlchemy 2.0.27
Database: PostgreSQL (via psycopg2 2.9.9)
Authentication: OAuth2 with JWT (PyJWT 2.8.0, python-jose 3.3.0)
Password Hashing: bcrypt (via passlib 1.7.4)
Tools: Pydantic 2.6.3, python-dotenv 1.0.1, Uvicorn 0.27.1
Other: HTTPX 0.27.0, python-multipart 0.0.9

Setup Instructions
To run the application locally:
Clone the repository: git clone https://github.com/0NGUTOR0/SOCAPP.git
Set up PostgreSQL: Ensure PostgreSQL is running on localhost at port 5432. Create an empty database named social_media_db using a PostgreSQL client. Create a .env file in the 
project root and set the database URL to postgresql://your_username:your_password@localhost:5432/social_media_db. SQLAlchemy automatically generates the database schema 
(e.g., tables for users, posts, likes, and follows) on startup.
Install dependencies: Create a virtual environment with python -m venv venv, activate it (e.g., source venv/bin/activate on Linux/Mac or venv\Scripts\activate on Windows), and install
dependencies with pip install -r requirements.txt.
Run the application: Execute uvicorn main:app --reload. The API will be accessible at http://localhost:8000.

API Endpoints
Authentication:
POST /login - Authenticate a user with email and password, returning a JWT token (bearer type).

User Management:
POST /users - Create a new user with name, email, and password.
GET /users/{id} - Retrieve details for a specific user by ID.
GET /users?limit={limit}&skip={skip}&search={search} - List users with pagination and optional name search, including follower counts.

Post Management:
POST /posts - Create a new post with title and content, tied to the authenticated user.
GET /posts?limit={limit}&skip={skip}&search={search} - Retrieve a paginated list of posts with like counts and optional title search.
GET /posts/{id} - Retrieve a specific post by ID with its like count.
PUT /posts/{id} - Update a post’s title or content (restricted to the post’s owner).
DELETE /posts/{id} - Delete a post (restricted to the post’s owner).

Project Structure
APP/main.py: Entry point for the FastAPI application.
APP/Models.py: SQLAlchemy models for users, posts, likes, and follows.
APP/Schemas.py: Pydantic schemas for request/response validation.
APP/oauth2.py: JWT token creation and validation logic.
APP/Database.py: Database connection and session management.
APP/Utilities.py: Helper functions, including password hashing and verification.

Authentication
The application uses OAuth2 with JWT for secure authentication:
Registration: Users sign up via /users, storing hashed passwords in a users table managed by SQLAlchemy.
Login: Users authenticate via /login, receiving a JWT token for accessing protected endpoints.
Protected Endpoints: APIs like /posts and /users/{id} require a valid JWT in the Authorization header (e.g., Bearer <token>).

Future Enhancements
-Add real-time notifications for likes and follows using WebSockets.
-Implement post commenting and threaded replies.
-Integrate Redis for caching frequently accessed data.

Contributing
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes.

Contact
For questions or feedback, reach out to ngutorugbor1@gmail.com or open an issue on GitHub.

