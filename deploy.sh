#!/bin/bash

# Build the project
echo "Building project..."
npm run build

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "Build successful!"
    echo "Dist files are in the 'dist' directory."
    echo ""
    echo "To deploy to Nginx:"
    echo "1. Copy the contents of 'dist' to your Nginx web root (e.g., /usr/share/nginx/html)"
    echo "2. Configure Nginx to serve the static files"
    echo ""
    echo "To deploy to GitHub Pages:"
    echo "1. Push the 'dist' directory to the 'gh-pages' branch"
    echo "2. Or use a deployment service like Vercel, Netlify, or Cloudflare Pages"
    echo ""
    echo "For local preview:"
    echo "npx serve dist"
else
    echo "Build failed!"
    exit 1
fi