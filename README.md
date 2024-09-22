**Relationships**
# one to one
- An album belongs to one artist
# one to many
- One artist can have many albums

**Migrations**
# run:
'alembic init migrations'
- This initializes alembic and creates a migrations file
import models in the env.py file to create the tables in the database
run alembic upgrade head and refresh table