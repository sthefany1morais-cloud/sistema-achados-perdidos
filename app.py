from app_factory import create_app

app = create_app()

if __name__ == "__main__":
    # Servidor local de desenvolvimento. Não usar debug=True em produção.
    app.run(debug=True)
