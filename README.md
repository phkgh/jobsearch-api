# JobSearch API (v1.1)

A robust backend API for job listings built with Django and PostgreSQL. It features pagination, filtering, ordering, and performance benchmarking. A lightweight resume-matching endpoint is included to showcase experimental logic for future AI enhancements.

---

## Features

- RESTful API for job listings (CRUD)
- Resume-job matching endpoint using key-term relevance scoring
- PostgreSQL database with environment-specific config
- Caching enabled for repeated API calls
- Performance benchmarking using ApacheBench
- Dockerized setup with docker-compose
- Clean project structure and modular code
- Versioned releases with GitHub integration

## API Endpoints

| Method | Endpoint           | Description                        |
|--------|--------------------|------------------------------------|
| GET    | /api/jobs/         | List all job posts                 |
| POST   | /api/jobs/         | Create a new job post              |
| GET    | /api/jobs/{id}/    | Retrieve a specific job post       |
| PUT    | /api/jobs/{id}/    | Update a job post                  |
| DELETE | /api/jobs/{id}/    | Delete a job post                  |
| POST   | /resume-score/     | Returns a relevance score for a resume vs job description

## Resume Scoring Endpoint

Takes in resume and job description as plain text and returns:

- Score (percentage of keyword match)
- Summary of matched key terms
---

## Project Structure

```
.
├── Dockerfile
├── LICENSE
├── README.md
├── docker-compose.yml
├── jobs
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── management
│   │   ├── __init__.py
│   │   └── commands
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_jobpost_company_alter_jobpost_location_and_more.py
│   │   └── __init__.py
│   ├── models.py
│   ├── pagination.py
│   ├── serializers.py
│   ├── test.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── jobsearch
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt

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

Tokenized, case-insensitive keyword matching

Clean logic that avoids complex NLP libraries

Fast response time: ~14ms average per request on local server using PostgreSQL

Supports easy testing via Postman or curl using simple JSON payloads

---

## Database

**Production DB:** PostgreSQL  default credentials
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

Tested using ApacheBench with 1000 requests and 10 concurrent users on the /resume-score/ endpoint.

Requests per second: 695.32

Average response time: 14 ms

Failed requests: 0

Total transferred: 401,000 bytes

Total body sent: 351,000 bytes

HTML transferred: 83,000 bytes

Transfer rate:

    Received: 272.29 Kbytes/sec

    Sent: 238.34 Kbytes/sec

    Total: 510.63 Kbytes/sec

Latency:

    50% of requests completed in 14 ms

    99% of requests completed under 43 ms

    100% of requests completed under 48 ms
---

## Versioning

- `v1.0`: Initial version with core job posting API and performance benchmarking
- `v1.1`: PostgreSQL + resume-score AI endpoint with AI keyword matching

---

## License

MIT License

---

## Contact

**Author:** Hemanth Kumar Pappu  
**GitHub:** [phkgh](https://github.com/phkgh)
