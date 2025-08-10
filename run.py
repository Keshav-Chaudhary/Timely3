from app import create_app

app = create_app()

if __name__ == "__main__":
    # Only runs locally, not on Vercel
    app.run(debug=True)
