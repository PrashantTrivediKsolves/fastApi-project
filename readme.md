# FastAPI CRUD Example

This is a simple FastAPI application demonstrating CRUD operations on an in-memory list of items.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn

Install dependencies:

```sh
pip install fastapi uvicorn
```

## Running the Application

```sh
uvicorn main:app --reload
```

## API Endpoints

### 1. Create Item

- **URL:** `/items/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "id": 1,
    "name": "Apple",
    "price": 10.5,
    "is_offer": true
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "name": "Apple",
    "price": 10.5,
    "is_offer": true
  }
  ```
- **Error Response:**  
  Status: 400
  ```json
  {
    "detail": "Item with this ID already exists"
  }
  ```

### 2. Get All Items

- **URL:** `/items/`
- **Method:** `GET`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Apple",
      "price": 10.5,
      "is_offer": true
    }
  ]
  ```

### 3. Get Item by ID

- **URL:** `/items/{item_id}`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "id": 1,
    "name": "Apple",
    "price": 10.5,
    "is_offer": true
  }
  ```
- **Error Response:**  
  Status: 404
  ```json
  {
    "detail": "Item not found"
  }
  ```

### 4. Update Item

- **URL:** `/items/{item_id}`
- **Method:** `PUT`
- **Request Body:**
  ```json
  {
    "id": 1,
    "name": "Banana",
    "price": 12.0,
    "is_offer": false
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "name": "Banana",
    "price": 12.0,
    "is_offer": false
  }
  ```
- **Error Response:**  
  Status: 404
  ```json
  {
    "detail": "Item not found"
  }
  ```

### 5. Delete Item

- **URL:** `/items/{item_id}`
- **Method:** `DELETE`
- **Response:**
  ```json
  {
    "message": "Item 1 deleted successfully"
  }
  ```
- **Error Response:**  
  Status: 404
  ```json
  {
    "detail": "Item not found"
  }
  ```

## License

MIT
