# JobSearch API

A high-performance job listing backend API built using Django and Django REST Framework. It includes real-world features like filtering, pagination, sorting, data seeding, unit testing, caching, and Docker support.

## 🔍 Features

- List, create, update, and delete job posts
- Filter by location, company
- Search by keyword (title or description)
- Sort by salary or post date
- Paginate large result sets
- Seed 10,000+ jobs using Faker
- Load tested with ApacheBench
- Unit tested for correctness
- Caching for high-read endpoints
- Dockerized for easy deployment

## 🚀 Quick Start

```
# Local Development
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Visit: http://localhost:8000/api/jobs/

# Docker
docker-compose up --build

# Visit: http://localhost:8000/api/jobs/

# Seeding Fake Data
python manage.py generate_fake_jobs 10000

# Run Unit Tests
python manage.py test

# Load Testing with ApacheBench
ab -n 1000 -c 10 http://127.0.0.1:8000/api/jobs/
```

## 📁 Project Structure

```
jobsearch-api/
├── jobs/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   ├── tests.py
│   └── management/
│       └── commands/
│           └── generate_fake_jobs.py
├── jobsearch/
│   ├── settings.py
│   └── urls.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 📫 Author

**Hemanth Kumar Pappu**
GitHub: [phkgh](https://github.com/phkgh)
