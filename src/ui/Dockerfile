# Stage 1: Build the SvelteKit app
FROM node:22-alpine AS build

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and pnpm-lock.yaml files to the working directory
COPY package.json pnpm-lock.yaml ./

# Install pnpm
RUN npm install -g pnpm

# Install dependencies
RUN pnpm install

# Copy the rest of the application code to the working directory
COPY . .

# Build the SvelteKit app
RUN pnpm run build

# Stage 2: Serve the built SvelteKit app
FROM node:22-alpine AS serve

# Install serve globally
RUN npm install -g serve

# Set the working directory in the container
WORKDIR /app

# Copy the built files from the build stage
COPY --from=build /app/build .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the app
CMD ["serve", "-s", ".", "-l", "5000"]