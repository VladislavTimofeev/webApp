# Digital library (Web application written in python with deployments in AWS)

### Stack : 
- python + django
- postgres
- aws

### The architecture of the project is as follows:

![](pictures/architecture.PNG)

The user sends a request to the server, followed by the request and the database, and then the response is returned
to the user.

## Project Description:

The project consists of a server part with a database connection and further deployment to the AWS.

When entering the electronic library, the user can have 2 roles:
* guest
* authorized user

As a guest, the user can make requests for information about the book, author, genre and search for what he needs.

As an authorized user, he has all the actions of a guest, as well as (adding, deleting, downloading a book, online reading).

### Database includes user data, books, authors

The guest can only make GET requests:  
* GET /books/ - here we get a list of books  
* GET /books/byAuthor - get books by a specific author

An authorized user can make various kinds of requests:

* GET /books/ - get all books  
* POST /books/authorName/bookName - adding a book  
* DELETE /books/authorName/bookName - deleting a book

### Use cases : 

- The user can find a book by genre, author, book title.
- Upon request, the user can borrow the book if it is available, or reserve it.
- If the required book is not available, the user is placed on hold, and when a book appears, he receives a notification.
- The user can receive notifications about the approaching end of the period of use of the book, about the receipt by 
the library of the book that the user is waiting for.
- The user can renew the book when the term of use of the book comes to an end.
- If the user somehow forgets to return the book before the deadline, the book is considered overdue and the user pays
a penalty.

### HTTP requests and response with body

### Requests: 

- users:

POST /users — add new user  
GET /users  — get a list of users


GET /users/{id}  — show user 3 info  
PUT /users/{id} — edit user 3  
DELETE /users/{id} — delete user 3  


GET /users/{id}/books - get info about books {id} user  
GET /users?role=guest - get info about user where role = guest

#### GET /api/v1/users/{id}

#### GET Response:

    {
     "id" : "{id}",  
     "name" : "Mike",  
     "surname" : "Wazovski",  
     "email" : "user@example.test",  
     "password" : {  
       "value" : "12334566778"  
     },  
    }

200 - OK  
404 - Not Found  
500 - Internal Server Error  
503 - Service Unavailable  


#### POST /api/v1/users

    {
     "name" : "Mike",
     "surname" : "Wazovski",
     "email" : "user@example.test",
     "password" : {
       "value" : "12334566778"
     },
    }


#### POST Response:

201 - Created  
400 - invalid email or wrong password  
409 - email already exist  
500 - Internal Server Error  
503 - Service Unavailable  


#### PUT /api/v1/users/{id}

    {
       "name" : "Mike >> Maks",
       "surname" : "Wazovski >> Toretto",
       "email" : "user@example.test  >> maks@example.test",
       "password" : {
          "value" : "12334566778 >> 55555555"
       },
    }


#### PUT Response:

200 - OK  
204 - No Content  
400 - invalid email or wrong password  
409 - email already exist  
500 - Internal Server Error  
503 - Service Unavailable  


- books:

POST /books - create new book  
GET /books  — get a list of book  


GET /books/{id}  — show book 2 info  
PUT /books/{id} — edit book 2  
DELETE /books/{id} — delete book 2  


GET /books?genreName=horrow  
GET /book?authorName=Jules&authorSurname=Verne  


#### GET /api/v1/books/{id}

#### GET Response:

    {
       "id" : "{id}",
       "book_name" : "Another world",
       "genre_id" : "Horrow"
    }

200 - OK  
404 - Not Found  
500 - Internal Server Error  
503 - Service Unavailable  


#### POST /api/v1/books

    {
       "book_name" : "Another world",
       "genre_id" : "Horrow"
    }


#### POST Response:

201 - Created  
400 - Bad Request  
500 - Internal Server Error  
503 - Service Unavailable  


#### PUT /api/v1/books/{id}

    {
       "book_name" : "Another world  >> Underworld",
       "genre_id" : "Horrow >> Fantasy"
    }


#### PUT Response:

200 - OK  
204 - No Content  
400 - invalid email or wrong password  
409 - email already exist  
500 - Internal Server Error  
503 - Service Unavailable

- holds:

POST /holds — create new hold  
GET /holds  — get a list of hold  

GET /holds/{userId} - show what is reserved by user {userId}  
GET /holds/{id}  
PUT /holds/{id}  
DELETE /holds/{id}

#### GET /api/v1/holds/{id}

#### GET Response:

    {
       "id" : "{id}"
       "start_time" : "01.01.2023",
       "end_time" : "01.04.2023",
       "book_copies_id" : "{id}",
       "user_id" : "{id}"
    }

200 - OK  
404 - Not Found  
500 - Internal Server Error  
503 - Service Unavailable  


#### POST /api/v1/holds

    {
       "start_time" : "01.01.2023",
       "end_time" : "01.04.2023",
       "book_copies_id" : "{id}",
       "user_id" : "{id}"
    }


#### POST Response:

201 - Created  
400 - invalid email or wrong password  
409 - email already exist  
500 - Internal Server Error  
503 - Service Unavailable  


#### PUT /api/v1/holds/{id}

    {
       "start_time" : "01.01.2023",
       "end_time" : "01.04.2023 >> 01.06.2023",
       "book_copies_id" : "{id}",
       "user_id" : "{id}"
    }


#### PUT Response:

200 - OK  
204 - No Content  
400 - invalid email or wrong password  
409 - email already exist  
500 - Internal Server Error  
503 - Service Unavailable

- bookCopies:

POST /bookСopies — create new book_copies  
GET /bookСopies  — get a list of book_copies


GET /bookСopies?yearOfPublishing=1890 - show book copies where year_of_publishing is 1890  
GET /bookСopies/{bookId} - show book copies  
PUT /bookСopies/{id}  
DELETE /bookСopies/{id}

#### GET /api/v1/bookCopies/{id}

#### GET Response:

    {
       "id" : "{id}"
       "yearOfPublishing" : "1890",
       "book_id" : "{id}",
       "publisher_id" : "{id}"
    }

200 - OK  
404 - Not Found  
500 - Internal Server Error  
503 - Service Unavailable  


#### POST /api/v1/bookСopies

    {
       "id" : "{id}"
       "yearOfPublishing" : "1890",
       "book_id" : "{id}",
       "publisher_id" : "{id}"
    }

#### POST Response:

201 - Created  
400 - invalid email or wrong password  
409 - email already exist  
500 - Internal Server Error  
503 - Service Unavailable  

