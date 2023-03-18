FROM node:16.18

# Install PostgreSQL
RUN apt-get update && \
    apt-get install -y postgresql

ENV PORT=3000

COPY . /frontend-react-js
WORKDIR /frontend-react-js
RUN npm install
EXPOSE ${PORT}
CMD ["npm", "start"]