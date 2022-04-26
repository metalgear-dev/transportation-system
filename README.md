# Transportation System

This is the Django implementation of the backend API server for dealing with geographic data.

## Overview

- Provider management
- Service Area management

## Polygon Area Management

GeoDjango is used to implement CRUD of polygon service areas. The used database is the postgresql with PostGIS.

The sample API methods for polygon areas are as follows.

- POST

To create a service area, polygon data needs to set with the following format.
`/api/areas`

```
{
    "provider_id": 1,
    "name": "area-1",
    "price": 100.00,
    "region": 'POLYGON((0 0, 0 50, 50 50, 50 0, 0 0))
}
```

- GET

There are two query parameters for searching for service areas.

`provider_id` : Provider's foreign key id

`point` : The coordinate of the point which is placed in the service areas to be found

The following API URL is looking for search areas which belongs to the provider(id = 1) and includes that point.

```
/api/areas?provider_id=1&point=POINT(10 10)
```
