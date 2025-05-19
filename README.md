# JobSearch API (v1.1)

A clean, production-grade REST API built with Django and PostgreSQL.  
Includes fast job listings, resume-score AI endpoint, pagination, filtering, ordering, caching, benchmarking, and Docker support.

---

## Features

- RESTful Job Posting API (`/api/jobs/`)
- Resume vs Job Description AI Score (`/resume-score/`)
- Pagination, filtering, ordering
- PostgreSQL for realistic SQL integration
- Faker-based data seeding for testing
- Caching using `django.core.cache`
- Performance benchmarking with ApacheBench (`ab`)
- Unit tests for key endpoints
- Docker-ready (`Dockerfile`, `docker-compose.yml`)
- Clean Git structure with versioning and `.gitignore`

---

## Project Structure

```
jobsearch-api/
├── jobs/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── jobsearch/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .gitignore
```

---

## Resume AI Endpoint

**Endpoint:**  
`POST /resume-score/`

**Request JSON:**
```json
{
  "resume": "Python, Django, REST",
  "job_description": "Django and REST API"
}
```

**Response JSON:**
```json
{
  "score": 33,
  "match_summary": "2 of 6 key terms matched: django, rest"
}
```

**Key Notes:**
- Tokenized, case-insensitive matching
- Configurable key term logic
- Fast: responds in < 30ms on local server

---

## Database

**Production DB:** PostgreSQL  
- Database: `jobsearch_db`
- User: `jobsearch_user`
- Password: `securepass123456789`

Ensure PostgreSQL is running:

```bash
brew services start postgresql
psql postgres
# Then:
CREATE DATABASE jobsearch_db;
CREATE USER jobsearch_user WITH PASSWORD 'securepass123456789';
GRANT ALL PRIVILEGES ON DATABASE jobsearch_db TO jobsearch_user;
```

---

## How to Run (Local)

```bash
# Clone the repo
git clone https://github.com/phkgh/jobsearch-api.git
cd jobsearch-api

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
```

---

## Performance Benchmarks

Tested with 1000 requests, 10 concurrency:

```bash
ab -n 1000 -c 10 http://127.0.0.1:8000/api/jobs/
```

**Results:**
- Requests per second: **~64.08**
- Failed requests: **0**
- Average response time: **156ms**
- Caching reduced cold-start latency by **~70%**

---

## Versioning

- `v1.0`: Initial SQLite-based REST API
- `v1.1`: PostgreSQL + resume-score AI endpoint

---

## License

MIT License

---

## Contact

**Author:** Hemanth Kumar Pappu  
**GitHub:** [phkgh](https://github.com/phkgh)
