from fastapi import FastAPI

from hw3.schema import graphql_api

app = FastAPI()
app.add_route("/", graphql_api.app)
