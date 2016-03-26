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
Return: None  

### Event
- Create Event (simple event model for now)
URL: /events/new/  
Method: POST  
Params: name, authenticator  
Return: None  

- Get all Events
URL: /events/  
Method: POST  
Params: authenticator  
Return: list of events created by the user  

### Synchronization
- to be added


