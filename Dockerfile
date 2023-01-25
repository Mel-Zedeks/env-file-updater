FROM alpine:3.10

COPY src/env-file-updater.py ./

ENTRYPOINT ["/env-file-updater.py"]