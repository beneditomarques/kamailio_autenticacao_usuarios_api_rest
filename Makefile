build:
	docker build -t mongodb mongodb/
	docker build -t api api/		
	docker build -t kamailio kamailio/
	docker build -t mongo-express mongo-express/
up:
	docker-compose up 
down:
	docker-compose down
restart:
	docker-compose restart
