import requests
from app import get_resultados_nba,app,jsonify

@app.route('/v1/resultados_nba', methods=['GET'])
def test_validate_nba_request():
    with app.app_context():
        resultados_nba = [
        {"data": "2024-04-26", "time_casa": "Los Angeles Lakers", "pontos_casa": 110, "time_visitante": "Golden State Warriors", "pontos_visitante": 105},
        {"data": "2024-04-25", "time_casa": "Brooklyn Nets", "pontos_casa": 115, "time_visitante": "Milwaukee Bucks", "pontos_visitante": 120},
        {"data": "2024-04-24", "time_casa": "Los Angeles Clippers", "pontos_casa": 98, "time_visitante": "Phoenix Suns", "pontos_visitante": 102}
        ]
        body = jsonify(resultados_nba)
        assert body.status_code == 200




