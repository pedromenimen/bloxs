setup:
  addons:
    - plan: cleardb-mysql
      as: DATABASE
build:
  docker:
    web: dockerfile
run:
  web: flask run --host=0.0.0.0 --port=5000
