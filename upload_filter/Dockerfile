FROM ubuntu:22.04

RUN apt update && apt install -y curl  && apt clean && mkdir -p /app/src && ln -s /app/src/main.py /app/main.py
WORKDIR /app
RUN curl -LO https://github.com/indygreg/python-build-standalone/releases/download/20230507/cpython-3.11.3+20230507-x86_64-unknown-linux-gnu-install_only.tar.gz && \
    tar xzvf cpython-3.11.3+20230507-x86_64-unknown-linux-gnu-install_only.tar.gz -C /usr/local/ && \
    rm cpython-3.11.3+20230507-x86_64-unknown-linux-gnu-install_only.tar.gz
RUN bash -c  "/usr/local/python/bin/python3 -m venv .venv && \
    source .venv/bin/activate && \
    pip install -U pip setuptools wheel && \
    pip install fastapi 'uvicorn[standard]'"

Expose 8080/tcp
CMD bash -c "source .venv/bin/activate && uvicorn main:app --reload --port 8080 --host 0.0.0.0"