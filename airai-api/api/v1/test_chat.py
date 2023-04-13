from unittest.mock import patch

import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from api.v1.chat import router

client = TestClient(router)


@patch("llm.air_quality.air_quality_model", return_value=[{"name": "City A", "latitude": 1.0, "longitude": 2.0}])
@patch("helpers.external_api.meteo.Meteo.fetch_air_quality", return_value={"pm10": 10, "pm2_5": 5})
def test_chat_success(mock_fetch_air_quality, mock_air_quality_model):
    response = client.get("/?query=what+is+the+air+quality+in+City+A")
    assert response.status_code == 200
    assert response.json() == {"air_qualities": [{"pm10": 10, "pm2_5": 5}]}


@patch("llm.air_quality.air_quality_model", return_value=None)
def test_chat_not_asking_about_air_quality(mock_air_quality_model):
    with pytest.raises(HTTPException) as err:
        client.get("/?query=what+is+the+weather+like+in+City+A")
    assert err.value.status_code == 400
    assert err.value.detail == "NOT_ASKING_ABOUT_AIR_QUALITY"


@patch("llm.air_quality.air_quality_model", return_value=[])
def test_chat_no_matching_cities(mock_air_quality_model):
    response = client.get("/?query=what+is+the+air+quality+in+City+A")
    assert response.status_code == 200
    assert response.json() == {"air_qualities": None}
