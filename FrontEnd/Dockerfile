FROM node:16-alpine 

WORKDIR /app

COPY . .

RUN npm ci 
RUN npm i serve

RUN npm run build

ENV NODE_ENV production

CMD [ "npx", "serve", "build" ]

#docker build -t front .
#docker run -p 3000:3000 -it front