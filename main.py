from app import app
# from app.models import UserModel, DirectoryModel, DeckModel, CardModel

# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User, 'Card': Card}

def run():
  app.run(host="0.0.0.0", port=8000)

if __name__ == '__main__':
  run()





