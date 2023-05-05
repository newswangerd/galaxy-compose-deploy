FROM ghcr.io/pulp/galaxy:latest

# configure S6 to use env variables
ENV S6_KEEP_ENV=1

COPY settings.py /etc/pulp/settings.py
