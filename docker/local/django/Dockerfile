# Stage 1: Base Image 
ARG PYTHON_VERSION=3.12.4-bullseye

FROM python:${PYTHON_VERSION} as python


# Building dependency wheels 
# building stage one 
FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=local

RUN apt-get update && apt-get install --no-install-recommends -y \
  build-essential \
  libpq-dev

# copy requirements from host machine to docker machine
COPY ./requirements . 

# creating the dependency wheel and sub wheels 
RUN pip wheel --wheel-dir /usr/src/app/wheels \
  -r ${BUILD_ENVIRONMENT}.txt 


# stage 2 
# python run stage 

FROM python as python-run-stage 
ARG BUILD_ENVIRONMENT=local

ARG APP_HOME=/app 

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# install dependencies for this stage 
RUN apt-get update && apt-get install --no-install-recommends -y \
  libpq-dev \
  gettext \
  && apt-get purge -y  --auto-remove -o APT::AutoRemove::RecommendsImportant=false\
  && rm -rf /var/lib/apt/lists/*

# copy from the buik stage wheels and copy ti the dest wheels 
COPY --from=python-build-stage /usr/src/app/wheels  /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/*\
  && rm -rf /wheels/

COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY . ${APP_HOME}

ENTRYPOINT [ "/entrypoint" ]