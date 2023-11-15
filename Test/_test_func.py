

def test_status(URL,expcted_status_code):
    import requests
    response = requests.get(URL)
    assert response.status_code == expcted_status_code