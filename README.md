# Create api RESTFul with Flask and MongoDB

## API Endpoints
GET /lang
```
{
    "languages": [
        {
            "_id": "5a0ed3acbc3f2d000be78088",
            "name": "GO"
        }
    ]
}
```

GET /lang/ < name >
```
{
    "language": {
        "_id": "5a0ed3acbc3f2d000be78088",
        "name": "GO"
    }
}
```


POST /lang
```
{
    "name": "Python"
}
```

PUT /lang/< language_id >
```
{
    "name": "Go"
}
```

DELETE /lang/< language_id >


## Requirements
* Docker Compose

## RUN
```
docker-compose up
```

http://localhost:5000/lang
