import requests

def test_add():
    # Создаем задачу и получаем её id
    body = {"title":"taska","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    # Помечаем задачу выполненой
    body = {"completed":True}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)

    # Проверяем статус код
    assert response.status_code == 200

    # Проверяем что изменения сохранились
    assert response.json()["completed"] == True


