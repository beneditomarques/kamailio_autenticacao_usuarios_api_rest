FROM tiangolo/uvicorn-gunicorn:python3.8-slim-2020-12-19
COPY /conf /conf
RUN cp -rfv /conf/* / && \
    chmod +x /init_api.sh && \
    apt update && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt && \
    apt autoremove -y && \
    apt-get clean && \
    rm -rf /conf /usr/share/man/*

WORKDIR /app
CMD ["/init_api.sh"]
