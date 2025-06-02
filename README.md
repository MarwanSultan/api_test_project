A basic containerized API testing project utilizing Docker, Pytest, and the Requests library.

## 🧰 Features

* Containerized testing environment with Docker
* Automated API tests using Pytest
* HTTP requests handled via the Requests library
* Modular and scalable test structure

## 🚀 Getting Started

### Prerequisites

* [Docker](https://www.docker.com/get-started) installed on your machine
* Basic understanding of Python and Pytest([DEV Community][1])

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MarwanSultan/api_test_project.git
   cd api_test_project
   ```



2. **Build the Docker image:**

   ```bash
   docker build -t api_test_project .
   ```



3. **Run the tests:**

   ```bash
   docker run --rm api_test_project
   ```



## 🧪 Running Tests

The tests are executed automatically when the Docker container runs. To run tests manually:

1. **Access the container's shell:**

   ```bash
   docker run -it api_test_project /bin/bash
   ```



2. **Execute Pytest:**

   ```bash
   pytest
   ```



## 📁 Project Structure

```plaintext
api_test_project/
├── Dockerfile
├── requirements.txt
├── tests/
│   └── test_api.py
└── README.md
```


