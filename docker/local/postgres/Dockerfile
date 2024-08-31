FROM postgres:16-bullseye


# Copy maintenance scripts to /usr/local/bin/maintenance
COPY ./docker/local/postgres/maintenance /usr/local/bin/maintenance

# Ensure the scripts are executable and move them to /usr/local/bin
RUN chmod +x /usr/local/bin/maintenance/* \
  && mv /usr/local/bin/maintenance/* /usr/local/bin/ \
  && rmdir /usr/local/bin/maintenance
