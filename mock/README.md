# Data Source Subsystem
This subsystem simulates exteranl data sources, including a Microsoft SQL Server database, a RESTful web service, and a sample website.

## PHP API
Talk about this...

## SQL Server Database
### Local Setup
Setting up a local instance of Microsoft SQL Server 2019 or 2020 on a Mac is a little more entailed, since this software does not run natively on macOS. One approach is to use a Docker image that runs Microsoft SQL Server 2019 within an Ubuntu Linux container.  

Follow these steps to install Docker Desktop on your macOS laptop and then run Microsoft SQL Server inside a Docker container.
#### Step 1: Install Docker Desktop on macOS
1. Download Docker Desktop:
   - Visit [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
   - Click "Download for Mac (Apple Chip)" or "Download for Mac (Intel Chip)" based on your Mac type.

2. Install Docker Desktop:
   - Open the downloaded `.dmg` file.
   - Drag and drop Docker into the Applications folder.
   - Open Docker Desktop from Applications and follow the setup instructions.

3. Verify Installation:
   - Open Terminal and run:  
   ```sh
   docker --verson
   ```

   - If Docker is installed correctly, you should see the version number.

4. Ensure Docker is Running:
   - Click on the Docker icon in the menu bar and ensure it's running.

#### Step 2: Download and Run SQL Server 2019 (or 2020) on Docker
1. Pull the SQL Server 2019 Docker Image:
   - Open Terminal and run:

   ```sh
   docker pull mcr.microsoft.com/mssql/server:2019-latest
   ```

   - This downloads the latest Microsoft SQL Server 2019 image.

2. Run SQL Server in a Docker Container:
   ```sh
   docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=YourStrong!Passw0rd' \
   -p 1433:1433 --name sqlserver2019 \
   -d mcr.microsoft.com/mssql/server:2019-latest
   ```

   - Replace YourStrong!Passw0rd with a secure password that meets SQL Server password complexity rules.

   - `-p 1433:1433` maps port 1433 from the container to your Mac, allowing you to connect.

   - The `-d` flag runs the container in the background.

3. Verify the Running Container
   - Run:
   ```sh
   docker ps
   ```

   - You should see the sqlserver2019 container running.

For more details, refer to the Docker and Microsoft websites for installation instructions.

### Database Load
Once Docker, Ubuntu, and Microsft SQL Server are installed and running in a container, proceed to running the SQL scripts located in the `_dbscript\sqlserver\cdwwork` folder. Begin with the "create" scripts, and then run the "insert" scripts.

## Website
Talk about this...
