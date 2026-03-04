# 🚀 Spring Boot User Management Service (GraphQL & REST)

A User Management microservice built with **Spring Boot 3**, featuring a dual-interface approach: **GraphQL** for flexible, client-driven data fetching and **REST** for standard system integrations.

---

## ✨ Features
- **Hybrid API**: Support for both GraphQL mutations/queries and standard REST endpoints.
- **One-to-One Relationships**: Linked `User` and `Profile` entities.
- **Shared Service Layer**: Business logic is decoupled from the API layer for consistency.
- **Automatic Persistence**: JPA with H2 In-Memory database.
- **Infinite Recursion Protection**: Configured with Jackson annotations (`@JsonManagedReference`) to prevent StackOverflow errors in REST responses.

---

## 🛠 Tech Stack
- Java 17
- Spring Boot 3.x (Data JPA, GraphQL, Web)
- H2 Database (In-memory)
- Lombok
- Maven

---

## 📁 Project Structure
```
UserSvcGraphQL/
├── src/main/java/com/example/
│   ├── UserManagementApplication.java
│   ├── controller/
│   │   ├── UserController.java
│   │   └── UserRestController.java
│   ├── model/
│   │   ├── User.java
│   │   ├── Profile.java
│   │   ├── ProfileInput.java
│   │   └── UserRequest.java
│   ├── repository/
│   │   └── UserRepository.java
│   └── service/
│       └── UserService.java
├── src/main/resources/
│   ├── application.properties
│   └── graphql/
│       └── schema.graphqls
└── pom.xml
```

---

## 🚦 Getting Started

### Prerequisites
- JDK 17 or higher
- Maven 3.6+

### Installation & Run
1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd UserSvcGraphQL
   ```
2. **Build the project:**
   ```bash
   mvn clean install
   ```
3. **Run the application:**
   ```bash
   mvn spring-boot:run
   ```

---

## 🔗 API Endpoints

### GraphQL
- **Endpoint:** `http://localhost:8080/graphql`
- Use [GraphiQL](https://github.com/graphql/graphiql), [Altair](https://altair.sirmuel.design/), or [Postman](https://www.postman.com/) to interact.

#### Example Queries
- **Get all users:**
  ```graphql
  query {
    getAllUsers {
      id
      username
      email
      profile {
        phoneNumber
        address
      }
    }
  }
  ```
- **Get user by ID:**
  ```graphql
  query {
    getUser(id: 1) {
      id
      username
      email
      profile {
        phoneNumber
        address
      }
    }
  }
  ```
- **Create user:**
  ```graphql
  mutation {
    createUser(username: "john", email: "john@example.com") {
      id
      username
      email
    }
  }
  ```
- **Update user:**
  ```graphql
  mutation {
    updateUser(id: 1, username: "johnny", email: "johnny@example.com") {
      id
      username
      email
    }
  }
  ```
- **Delete user:**
  ```graphql
  mutation {
    deleteUser(id: 1)
  }
  ```

### REST
- **Base URL:** `http://localhost:8080/api/users`
- Example endpoints:
  - `GET /api/users` — Get all users
  - `GET /api/users/{id}` — Get user by ID
  - `POST /api/users` — Create user
  - `PUT /api/users/{id}` — Update user
  - `DELETE /api/users/{id}` — Delete user

---

## 📝 License
This project is licensed under the MIT License.

---

## 🙏 Acknowledgements
- [Spring Boot](https://spring.io/projects/spring-boot)
- [Spring for GraphQL](https://spring.io/projects/spring-graphql)
- [GraphQL Java](https://www.graphql-java.com/)
- [H2 Database](https://www.h2database.com/)
- [Lombok](https://projectlombok.org/)
