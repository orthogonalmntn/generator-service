# Generator Service

Generates content from neural language models for the FTRRL game project.

(Default language model is GPT-2.)

## Setup

Set environment vars:

```export JWT_SECRET_KEY=SOME_SECRET_KEY```

To run:

```uvicorn main:app --reload```

## Documentation

API Docs are available at:

- by [Swagger](http://127.0.0.1:8000/docs)
- by [ReDoc](http://127.0.0.1:8000/redoc)

## License

*This is a hobby project and an exploration in building Ruby + ML systems, and it's meant for non-commerical, educational purposes only!*