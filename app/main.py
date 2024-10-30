from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema
from app.db.data import init_db
from app.gql.query import Query

app = Flask(__name__)

schema = Schema(query=Query)

init_db()

if __name__ == '__main__':
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )
    app.run()
