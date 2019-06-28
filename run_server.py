from webserver import server


if __name__ == '__main__':
	import os
	port = int(os.environ.get('PORT', 5000))
	server.run(host="0.0.0.0", port=port)
