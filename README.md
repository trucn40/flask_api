importance commands
git clone https://github.com/trucn40/flask_api.git
cd flask_api/
pip install flask
python run.py

TESTING

test if the app is up or not
 curl -X GET http://127.0.0.1:5000/api/hello
 
 try to view user 1 and 2
 curl -X GET http://127.0.0.1:5000/api/user/1
 curl -X GET http://127.0.0.1:5000/api/user/2
 
add user to users.txt file
curl -X POST -H "Content-Type: application/json" -d '{"id": 4, "name": "Test User", "email": "testuser@verizon.net"}' http://127.0.0.1:5000/api/user
