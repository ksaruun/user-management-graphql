# 🚀 Spring Boot User Management Service (GraphQL & REST)

A robust User Management microservice built with **Spring Boot 3**, featuring a dual-interface approach: **GraphQL** for flexible, client-driven data fetching and **REST** for standard system integrations.

## ✨ Features
* **Hybrid API**: Support for both GraphQL mutations/queries and standard REST endpoints.
* **One-to-One Relationships**: Linked `User` and `Profile` entities.
* **Shared Service Layer**: Business logic is decoupled from the API layer for consistency.
* **Automatic Persistence**: JPA with H2 In-Memory database.
* **Infinite Recursion Protection**: Configured with Jackson annotations (`@JsonManagedReference`) to prevent StackOverflow errors in REST responses.

---

## 🛠 Tech Stack
* **Java 17**
* **Spring Boot 3.x** (Data JPA, GraphQL, Web)
* **H2 Database** (In-memory)
* **Lombok**
* **Maven**

---

## 🚦 Getting Started

### Prerequisites
* JDK 17 or higher
* Maven 3.6+

### Installation & Run
1. **Clone the repository**
2. **Build the project:**
   ```bash
   mvn clean install
   
