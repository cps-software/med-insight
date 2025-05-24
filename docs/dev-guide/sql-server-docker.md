To install **Microsoft SQL Server** and **SQL Server Integration Services (SSIS)** on a Mac using Docker, follow these steps:

---

### 1. Install Docker on macOS
1. Download and install Docker Desktop from the official Docker website: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/).
2. Follow the installation instructions and ensure Docker is running on your Mac.

---

### 2. Install Microsoft SQL Server on Docker
1. Pull the official SQL Server Docker image:
   ```bash
   docker pull mcr.microsoft.com/mssql/server:2019-latest
   ```
   Replace `1999-latest` with the specific version if you need a different one (e.g., `2022-latest`).

2. Create and run a container:
   ```bash
   docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=AllieD#1993" -p 1433:1433 --name sqlserver -d mcr.microsoft.com/mssql/server:2019-latest
   ```
\* Replace `YourStrongPassword!` with a strong password that meets SQL Server's complexity requirements.
\* The `-p 1433:1433` flag maps SQL Server's default port (1433) on the container to your host system.
\* `--name sqlserver` names your container for easy reference.

3. Verify the container is running:
   ```bash
   docker ps
   ```

4. Connect to SQL Server using:
   - **Azure Data Studio** (available on macOS): [Download here](https://learn.microsoft.com/en-us/sql/azure-data-studio/download-azure-data-studio).
   - **SQL Server Management Studio (SSMS)** via a remote Windows machine or virtual machine.

---

### **3. Install SSIS on Docker**
Unfortunately, **SSIS is not directly available on Linux-based Docker images**. SSIS is a Windows-only feature and is not officially supported on macOS or Linux.

#### Workarounds:
1. **Run SSIS on a Windows Virtual Machine**:
   - Use a virtual machine (e.g., Parallels, VMware Fusion, or VirtualBox) to run Windows on your Mac.
   - Install SQL Server and SSIS on the virtual machine.

2. **Set Up SSIS on a Remote Windows Server**:
   - If you have access to a Windows Server or a Windows machine, you can install SQL Server and SSIS there.
   - Use tools like Azure Data Studio or SQL Server Agent to manage SSIS packages remotely from your Mac.

3. **Alternative ETL Tools**:
   - If SSIS is not mandatory, you can use open-source tools like **Python with pandas** or **Apache NiFi** to handle ETL workflows on macOS.

---

### **4. Verify SQL Server Functionality**
1. Use Azure Data Studio to connect to SQL Server on Docker:
   - **Server name:** `localhost,1433`
   - **Authentication type:** SQL Login
   - **Username:** `sa`
   - **Password:** The password you set in the `docker run` command.

2. Run a test query to ensure everything works:
   ```sql
   SELECT @@VERSION;
   ```

---

### **Final Notes**
- While SQL Server runs seamlessly on Docker, SSIS requires a Windows environment. Using a virtual machine or a remote Windows server is the best way to access SSIS if you are working on a Mac.
- If your goal is purely ETL workflows and you're open to alternatives, consider using **Python** or cloud-based ETL tools like **Azure Data Factory** for cross-platform compatibility.