fastapi-auth-api/
├── app/
│   ├── __init__.py
│   ├── main.py                  # FastAPI entry point
│   │
│   ├── core/                    # Core configuration & security
│   │   ├── __init__.py
│   │   ├── config.py            # App settings (DB URL, secrets)
│   │   ├── security.py          # JWT & password hashing logic
│   │
│   ├── models/                  # Database models
│   │   ├── __init__.py
│   │   ├── user.py              # SQLAlchemy User model
│   │
│   ├── schemas/                 # Pydantic models for requests/responses
│   │   ├── __init__.py
│   │   ├── user.py              # User, Token, Login, etc.
│   │
│   ├── db/                      # Database session setup
│   │   ├── __init__.py
│   │   ├── session.py           # SQLAlchemy engine/session
│   │
│   ├── api/                     # API route definitions
│   │   ├── __init__.py
│   │   ├── deps.py              # Dependencies (auth, current_user, etc.)
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py          # /login
│   │   │   ├── users.py         # /admin/add_user, /me
│   │
│   └── utils/
│       ├── __init__.py
│       ├── crud_user.py         # Create/get users helper functions
│
├── alembic/                     # (optional) for DB migrations
│   ├── env.py
│   ├── versions/
│
├── pyproject.toml               # uv/Poetry dependencies
├── uv.lock
├── .env                         # Environment variables (DB, secret key)
├── Dockerfile                   # Container definition
├── docker-compose.yml           # Optional local DB setup
└── README.md
