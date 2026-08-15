## Request Types

## Get
This is used when we want to fetch a resource/data from the backend.

## Post
This is used when we want to create a new resource in the Backend.

## Put
This is used when we want to update an existing resource in Backend.

## Delete
This is used when we want to delete an existing resource in Backend.

## Patch
Thisis used when we want to update an existing resource partially in Backend.

## Example to understand put & patch
```json
{
    "id" : 101,
    "name" : "Amar S",
    "email" : "amarshiva08@gmail.com",
    "age" : 25,
    "city" : "Mysore"
}
```

To Update: It will do a complete record update - 
`Put/users/101`
```json
{
    "name" : "Amar S",
    "email" : "amarshiva08@gmail.com",
    "age" : 26,
    "city" : "Mysore"
}
```

To Partial Update: It will only update a smaall part instead of complete record - 
`Patch/users/101`
```json
{
    "age" : 26
}
```
#
# Data in Request

## Body
It is the data which will usually be sent in the format of json

## Query parameter also known as Request parameter
- This is appended to the url.
- This is __non-mandaory__ data.
- It __doesn't contribute__ to the URL Signature of the request.

https://localhost:8000/add?a=10&b=5 => Here a and b is the query parameter

## Path Parameter
- This is appended to the url
- This is __mandatory__ data.
- It __does contribute__ to the URL Signature of the request.

https://localhost:8000/users/:user_id --> /users/101 => If we do not send the userId it considers it as a different request

## Header

This is a key value pair. This is a usually mandatory data. It contains information related to auth and the type of request response, and Some other information.