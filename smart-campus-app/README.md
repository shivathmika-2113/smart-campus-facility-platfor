# Smart Campus Facility & Maintenance Platform

A starter full-stack implementation for Assignment 3 using Vue 3, Django REST Framework,
PostgreSQL and Docker Compose.

## Run
1. Install Docker Desktop and start it.
2. Extract this folder.
3. Copy `.env.example` to `.env` and set a local password.
4. From this folder run: `docker compose up --build`
5. Open http://localhost:3000

API: http://localhost:8000/api/health/

## Demo accounts
This starter UI uses a demo role selector (Administrator, Facility Manager, Technician,
Approver, Faculty, Student). It is for demonstrating the interface only. Production
authentication and server-side role enforcement must be completed before real use.

## Notes
- The Vue interface includes dashboard, facilities, bookings, maintenance, sensors,
  equipment requests, approvals and DevOps views.
- Django exposes basic health, facilities, bookings and ticket endpoints.
- The booking endpoint demonstrates overlap rejection at application level. For the
  assignment's concurrent two-instance test, implement PostgreSQL exclusion constraints
  and transactional/idempotency logic as described in your expectation document.
- Replace demo data with your own test evidence. Do not claim unrun tests or load results.
