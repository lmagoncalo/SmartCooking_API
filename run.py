# /run.py
import os

from src.app import create_app

if __name__ == '__main__':
	#env_name = os.getenv('FLASK_ENV')
	env_name = 'production'
	app = create_app(env_name)
	# run app
	#app.run()
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0',port=port)
