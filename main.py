# Import du framework FastAPI
from fastapi import FastAPI

# Import de la documentation
from documentation import api_description, tags_metadata

# Import des routeurs
from routers import (
    users_router,
    books_router,
    reviews_router,
    recommendations_router
)

# Initialisation de l'API
app = FastAPI(
    title="BiblioMate",
    description=api_description,
    openapi_tags=tags_metadata,
    docs_url='/'
)

# Inclusion des routeurs
app.include_router(users_router.router)
app.include_router(books_router.router)
app.include_router(reviews_router.router)
app.include_router(routers.router_auth.router)


