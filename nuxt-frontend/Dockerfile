FROM node:12.22.12

WORKDIR /Proyecto

COPY package*.json ./

#Se instalan los requerimientos de Vue y Nuxt
RUN npm install -g npm@6.14.16

RUN npm install nuxt
RUN npm install

COPY . ./
#Se expone el puerto 3000 para que se puedan conectar entre Containers
EXPOSE 3000
#Se define la variable de entorno del HOST y su puerto
ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000
ENV PATH /Proyecto/node_modules/.bin:$PATH
#Comando para correr la aplicacion en modo dev

CMD [ "npm", "run", "dev" ]
