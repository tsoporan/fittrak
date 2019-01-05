# Dockerfile for fittrak node development

FROM node:carbon-alpine

WORKDIR /usr/src/app

ADD fittrak-client/public public
ADD fittrak-client/__mocks__ __mocks__
ADD fittrak-client/src src

COPY fittrak-client/babel.config.js \
     fittrak-client/package.json \
     fittrak-client/vue.config.js \
     fittrak-client/package-lock.json ./

RUN npm install

EXPOSE 8080

CMD ["npm", "run", "serve"]
