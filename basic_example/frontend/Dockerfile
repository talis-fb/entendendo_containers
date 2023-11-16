FROM node:18.18.2-bullseye

RUN npm install -g http-server

RUN mkdir -p /usr/app
COPY package*.json /usr/app/
COPY . /usr/app/

RUN cd /usr/app/ && npm install
RUN cd /usr/app/ && npm run build

CMD [ "http-server", "/usr/app/dist", "-p", "8080"]