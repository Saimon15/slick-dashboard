from server.app import create_app

app = create_app()
app.app_context().push()

from server.tasks import celery