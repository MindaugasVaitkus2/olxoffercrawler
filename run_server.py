from webserver import application 


if __name__ == '__main__':
	import os
	port = int(os.environ.get('PORT', 5000))
	application.run(host="0.0.0.0", port=port, threaded=True)

