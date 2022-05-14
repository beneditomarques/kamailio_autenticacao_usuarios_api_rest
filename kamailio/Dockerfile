FROM kamailio/kamailio-ci:5.4.4-alpine

# COPY have to be after any apt command
COPY conf/ /conf
RUN cp -rfv /conf/* / && \
    apk add curl sngrep && \
    rm -rf /var/cache/apk/* /conf

WORKDIR /etc/kamailio

