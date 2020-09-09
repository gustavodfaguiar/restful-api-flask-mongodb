# Create api RESTFul with Flask and MongoDB

## API Endpoints
GET /lang
```json
{
    "languages": [
        {
            "_id": "5a0ed3acbc3f2d000be78088",
            "name": "GO"
        }
    ]
}
```

GET /lang/:name
```json
{
    "language": {
        "_id": "5a0ed3acbc3f2d000be78088",
        "name": "GO"
    }
}
```


POST /lang
```json
{
    "name": "Python"
}
```

PUT /lang/:language_id
```json
{
    "name": "Go"
}
```

DELETE /lang/:language_id


## Requirements
* Docker Compose

## RUN
```
docker-compose up
```

http://localhost:5000/lang
