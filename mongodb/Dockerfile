FROM mongo:3.6.10
COPY collections/* /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/*