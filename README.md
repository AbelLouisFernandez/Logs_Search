## Installation

### A. Run with Docker

### Prerequisites

Ensure you have Docker and docker compose both latest version installed on your system before proceeding. Docker compose  will be used to build and run the application in a containerized environment. For installation please refer the offcial documneation of docker [Docker Installation Guide](https://docs.docker.com/compose/install/linux/)


- **Gemini API Key**: 
- **Google Drive Storage**:
    - Certain Json files are needed to authenicate our application with google drive to access it files.
    - Please refer this link to know more [Connect Pathway LLM App with GDrive](https://pathway.com/developers/user-guide/connectors/gdrive-connector#setting-up-google-drive)
- **Voyage API Key**:
    - Create an [Voyage](https://www.voyageai.com/) account and generate a new API Key: 
    - To access the Voyage API, you will need to create an API Key. You can do this by logging into the [Voyage Dashboard] (https://dash.voyageai.com/) and navigating to the API Key management page.


### 1. Environment Setup

1. Create a `.env` file in the root directory of your project.
2. Add the following lines to the `.env` file, replace with you API keys:

   ```env
   GEMINI_API_KEY="Enter your gemini api key here"
   VOYAGE_API_KEY="Enter your voyage api key here"
   EMBEDDING_DIMENSION=1024
   LOCAL_FOLDER_PATH='/Desktop/dockercontainers'
   ```

This file will be used by Docker to set the environment variables inside the container.

### 2. Build and Run the Docker Image

With the environment variables set up, you can now build the Docker and run the image for the project.

- Open a terminal or command prompt.
- Navigate to the root directory of your project.
- Execute the following command to build and run the docker:

  ```sh
  docker compose up
  ```

This step compiles your application and its dependencies into a Docker image.


### 3. Access the Application

- Open your web browser.
- Navigate to `localhost:8501` to access the application.

You should see the application's interface if the setup was successful. This confirms that your Docker container is running and the application is accessible.

### 4. Troubleshooting

If you encounter any issues during the setup or execution process, please check the following:

- Ensure Docker is running on your system.
- Verify that the `.env` file contains the correct API key and settings.
- Make sure the Docker image was built successfully without errors.
- Check if the Docker container is running and the ports are correctly mapped.

For further assistance, consult the Docker documentation or seek help from Docker community forums.

### B. Streamlit UI 

### Setting Up th streamlit ui and logs uploading


1. Create a new Conda environment with the required dependencies:

    ```bash
    
    ```

    Replace `myenv` with a name of your choice for the Conda environment.

4. Install dependencies
   ```
   pip install -r requirements.txt
   ```

5. Activate the newly created Conda environment:

    ```bash
    conda activate myenv
    ```

6. Run the Backend Server:

    ```bash
    python main.py
    ```
    <p align="center">
    <img src="./assets/backend_layout.png" alt="layout" width="800"/>
    </p>


7. Launching the Streamlit UI for AURA user interface:
    ```bash
    streamlit run ./ui/server.py
    ```
  - Open your web browser.
  - Navigate to `localhost:8501` to access the application.
