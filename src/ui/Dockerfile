
FROM node:22-alpine AS build

WORKDIR /app
COPY package.json pnpm-lock.yaml ./

RUN npm install -g pnpm
RUN pnpm install

COPY . .

RUN pnpm run build
RUN pnpm prune --production

FROM node:22-alpine AS serve

RUN npm install -g serve
WORKDIR /app
COPY --from=build /app/build .

CMD ["serve", "-s", ".", "-l", "5000"]