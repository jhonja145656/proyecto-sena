from flask_script import Manager
from app import inicializar_app

app = inicializar_app()

Manager = Manager(app)

if __name__ == '__main__':
    Manager.run()
