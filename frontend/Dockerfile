# Use the official nginx image from the Docker Hub
FROM nginx:alpine

# Copy the index.html and other static files to the nginx html directory
COPY index.html /usr/share/nginx/html/index.html
COPY static /usr/share/nginx/html/static

# Expose port 8080 for the web server
EXPOSE 8080

# Start nginx server
CMD ["nginx", "-g", "daemon off;"]
