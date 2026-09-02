import requests
 #создать задачу, изменить и проверить что ИД не поменялся
def test_add_edit():
    body = {"title":"new_task_S","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    
    id = response.json()["id"]
    body2 =  {"title":"EDIT_task_S","completed":False}
       
    response2 = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body2)
    
    assert response2.status_code == 200    
    assert response2.json()["id"] == id
    assert response2.json()['title'] == 'EDIT_task_S'



   