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
- Create Event
URL: /events/new/  
Method: POST  
Params: name, authenticator, category, location, start_time, end_time  
Note: start_time and end_time should be in 'YYYY-MM-DD HH:MM:SS.mmmmmm' (2016-04-06 15:30:51.539410)
or 'YYYY-MM-DD HH:MM:SS' (2016-04-06 15:30:51)  
Return: Success  

- Get all Events  
URL: /events/  
Method: POST  
Params: authenticator  
Return: list of events created by the user  

### Synchronization
- to be added


