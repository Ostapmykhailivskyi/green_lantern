# to start work on project being in practice_2 folder

    $ pip install -r practice_2/grocery_store/requirements.txt
    $ pip install -e .

review config in grocery_store/config.py
    $ python grocery_store/fixtures/populate_data.py
    Database exists
    Data written in data_base succesfuly




sudo docker run --name some-postgres -e POSTGRES_PASSWORD=very_secret_password -e POSTGRES_USER=cursor -e POSTGRES_DB=cursor_sqlalchemy_db -p 5432:5432 -d postgres
run populate data
run wsgi 
send requests on postman