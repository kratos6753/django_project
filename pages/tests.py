from http import HTTPStatus

from django.test import SimpleTestCase


class RobotsTxtTests(SimpleTestCase):
    def test_get(self):
        response = self.client.get("/robots.txt")
        assert response.status_code == HTTPStatus.OK
        assert response["content-type"] == "text/plain"

    def test_pages_get(self):
        response = self.client.get("/pages/robots.txt")
        assert response.status_code == HTTPStatus.OK
        assert response["content-type"] == "text/plain"
