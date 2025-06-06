import pytest
from flask import template_rendered
from app import app
import builtins
from unittest.mock import patch, MagicMock

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route_renders_template(client):
    with patch('app.routes.get_reviews', return_value=[{"review": "Good", "sentiment": "positive"}]):
        with captured_templates(app) as templates:
            response = client.get('/')
            assert response.status_code == 200
            template, context = templates[0]
            assert template.name == 'index.html'
            assert "reviews" in context

def test_predict_route_returns_sentiment(client):
    mock_model = MagicMock()
    mock_model.predict.return_value = ["positive"]

    with patch('app.routes.model', mock_model):
        with patch('app.routes.insert_review') as mock_insert:
            response = client.post('/predict', data={'review': 'I love it!'})
            assert response.status_code == 200
            json_data = response.get_json()
            assert json_data['sentiment'] == "positive"
            mock_insert.assert_called_once_with("I love it!", "positive")

# Helper to capture templates rendered
from contextlib import contextmanager

@contextmanager
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)
