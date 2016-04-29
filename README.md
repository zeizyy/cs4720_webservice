# cs4720_webservice
The APIs are hosted at https://cs4720-webservice.herokuapp.com/

## APIs

### Authentication
- Create User  
URL: /user/new/  
Method: POST  
Params: username, password  
Return: user_id, authenticator  
- Login  
URL: /user/login/  
Method: POST
Params: username, password  
Return: user_id, authenticator  
- Logout  
URL: /user/logout/  
Method: POST  
Params: authenticator  
Return: Success  

### Event
- Get all Events  
URL: /events/  
Method: POST  
Params: authenticator  
Return: list of events created by the current user  

- Purge all Events
URL: /events/purge/  
Method: POST  
Params: authenticator  
Return: Success 

- Sync a Event to the server
URL: /events/sync/  
Method: POST  
Params: authenticator, UUID, name, note, location, category, start_datetime, end_datetime  
Return: Success  

### Todo
- Get all Todos  
URL: /todos/  
Method: POST  
Params: authenticator  
Return: list of todos created by the current user  

- Purge all Todos
URL: /todos/purge/  
Method: POST  
Params: authenticator  
Return: Success  

- Sync a Todo to the server
URL: /todos/sync/  
Method: POST  
Params: authenticator, UUID, name, note, due_datetime, reminder_datetime  
Return: Success  
