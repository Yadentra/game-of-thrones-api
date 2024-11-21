from app import create_app  # Import the create_app function

# Create and run the Flask app
app = create_app()

# Start the app in debug mode
app.run(debug=True)