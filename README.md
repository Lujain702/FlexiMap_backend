# FlexiMap – Backend

This repository contains the backend API for FlexiMap, a collaborative mapping platform. It is built with Django REST Framework and provides endpoints for map creation, marker management, user authentication, and more.

## 🌐 Tech Stack

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)
- Docker / Docker Compose

## 🚀 Live API (once deployed)

[https://fleximap.onrender.com/api](https://fleximap.onrender.com/api)

## 🔗 Related Projects

- [Frontend Repository](https://github.com/Lujain207/FlexiMap-frontend)

## 📦 Setup Instructions

To run this project locally using Docker:

```bash
git clone https://github.com/Lujain702/FlexiMap-backend
cd FlexiMap-backend
docker-compose up --build
To run it manually (without Docker):

python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
🧱 API Models Overview
Map: Created by a user, can be public or private.

Marker: Location marker belonging to a map.

Category: Classification for markers (e.g., Food, Tourism).

Comment: User comments on markers.

🔐 Authentication
JWT-based authentication using SimpleJWT.

Auth is required for any POST/PUT/DELETE operations on maps, markers, and comments.

📚 API Routing Table

HTTP Method	Endpoint	Description	Auth Required
POST	/api/register/	Register a new user	❌
POST	/api/login/	Login & obtain JWT	❌
GET	/api/maps/	List all public maps	❌
GET	/api/maps/:id/	Retrieve map by ID	❌
POST	/api/maps/	Create a new map	✅
PUT	/api/maps/:id/	Update a map (owner only)	✅
DELETE	/api/maps/:id/	Delete a map (owner only)	✅
GET	/api/maps/:map_id/markers/	Get markers for a map	❌
POST	/api/maps/:map_id/markers/	Add marker to a map	✅
PUT	/api/markers/:id/	Update a marker	✅
DELETE	/api/markers/:id/	Delete a marker	✅
GET	/api/categories/	Get all categories	❌
GET	/api/markers/:id/comments/	Get comments on a marker	❌
POST	/api/markers/:id/comments/	Add comment to marker	✅
DELETE	/api/comments/:id/	Delete comment (owner only)	✅

🔄 Future Features (Icebox)
Sharing maps via links or QR codes

Adding polyline paths to maps

User profile pages with saved maps

Marker search and filter by category

📊 Entity Relationship Diagram (ERD)
(Attach link or image here, e.g., from dbdiagram.io or drawSQL)

