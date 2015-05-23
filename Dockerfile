FROM node
COPY package.json /src/
RUN cd /src && npm install
COPY app.js /src/
COPY /api/ /src/api/
COPY /bin/ /src/bin/
COPY /public/ /src/public/
COPY /routes/ /src/routes/
COPY /views/ /src/views/
WORKDIR /src
CMD ["npm", "start"]
EXPOSE 3000
