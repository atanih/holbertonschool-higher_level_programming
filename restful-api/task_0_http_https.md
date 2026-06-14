# Basics of HTTP/HTTPS

## HTTP vs HTTPS

- HTTP sends data in plain text — anyone can intercept and read it
- HTTPS encrypts data using SSL/TLS — protects from eavesdropping
- HTTP uses port 80, HTTPS uses port 443
- HTTPS requires an SSL/TLS certificate
- Sensitive sites (banking, APIs, email) always use HTTPS

---

## HTTP Request Structure

- Method: Action to perform (GET, POST, PUT, DELETE)
- URL/Path: Resource being requested (/api/users)
- Headers: Metadata (Content-Type, Authorization)
- Body: Data sent with request (POST/PUT only)

## HTTP Response Structure

- Status Line: Version + code + reason (HTTP/1.1 200 OK)
- Headers: Info about the response (Content-Type, Length)
- Body: Returned data (JSON, HTML, etc.)

---

## Common HTTP Methods

- GET: Retrieves data — fetching a user profile
- POST: Creates a resource — submitting a form
- PUT: Replaces a resource — updating a full profile
- DELETE: Removes a resource — deleting an account
- PATCH: Partially updates a resource — changing a username

---

## Common HTTP Status Codes

- 200 OK: Request succeeded
- 201 Created: New resource was created (POST)
- 301 Moved Permanently: Resource has a new URL
- 404 Not Found: Resource doesn't exist
- 500 Internal Server Error: Server-side failure