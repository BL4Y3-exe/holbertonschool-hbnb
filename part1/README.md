# HBnB Evolution – Part 1: Technical Documentation

## 📌 Overview

This project is part of the HBnB Evolution application, a simplified AirBnB-like system developed for learning software engineering principles.

The goal of this part is to design and document the system architecture before implementation. It focuses on understanding how different components of the system interact and how the application is structured.

---

## 🏗 Architecture

The application follows a **three-layer architecture**:

- **Presentation Layer**: Handles user interactions through API endpoints and services.
- **Business Logic Layer**: Contains the core domain models and business rules.
- **Persistence Layer**: Manages data storage and retrieval.

Communication between layers is handled using the **Facade design pattern**, which provides a simplified interface between the API and the internal system logic.

---

## 📊 Diagrams Included

This documentation includes the following diagrams:

### 1. High-Level Package Diagram
- Shows the overall system architecture
- Illustrates the three-layer structure
- Demonstrates communication via the Facade pattern

### 2. Business Logic Class Diagram
- Defines the main entities: User, Place, Review, and Amenity
- Shows attributes, methods, and relationships
- Includes inheritance from a BaseModel class

### 3. Sequence Diagrams
- User Registration flow
- Place Creation flow
- Review Submission flow
- Fetching Places flow

These diagrams illustrate how requests move through the system from the API to the database and back.

---

## 🎯 Purpose

This documentation serves as a blueprint for the implementation phase of the project. It ensures a clear understanding of system structure, responsibilities of each layer, and interactions between components.

---

## 📁 Directory Structure
part1/
|
├── technical_documentation.md
└── README.md

---

## ✍️ Author

BL4Y3