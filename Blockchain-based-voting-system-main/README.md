<div class="container">
    <h1></b>Blockchain-Based-Voting-System</h1>
  <b> The Decentralized Voting System is a blockchain-based application that ensures secure, transparent, and tamper-proof elections. By leveraging Ethereum's blockchain technology, the system eliminates the need for intermediaries and prevents election fraud while maintaining voter anonymity. This solution enables remote voting, making the electoral process more accessible and reliable.</b>

   <div class="container">
     <h2>🚀 Features</h2>
    <ul>
        <li>✅ Secure voter registration and authentication</li>
        <li>✅ Transparent voting process with immutable records</li>
        <li>✅ Real-time vote counting</li>
        <li>✅ Web-based user interface for ease of access</li>
    </ul>
    <div class="container">
      <h2>🛠️ Technologies Used</h2>
    <ul>
        <li><strong>Ethereum Blockchain:</strong> Smart contract execution</li>
        <li><strong>Solidity:</strong> Smart contract programming language</li>
        <li><strong>Web3.js:</strong> Interaction between front-end and blockchain</li>
        <li><strong>HTML, CSS, JavaScript:</strong> Front-end development</li>
        <li><strong>MetaMask:</strong> Ethereum wallet for transactions</li>
    </ul>
    <div class="container">
    <h2>📋 Requirements</h2>
  <ul>
    <li><strong>Node.js</strong> (Version 18.14.0) – Backend server and package management</li>
    <li><strong>Python</strong> (Version 3.9) – Required for backend services using FastAPI</li>
    <li><strong>MetaMask</strong> – Browser extension for Ethereum transactions</li>
    <li><strong>FastAPI</strong> – Python-based web framework for API management</li>
    <li><strong>MySQL Database</strong> (Port 3306) – For storing user and voting data</li>
 </ul>
  <div class="container">
   <h2>🔗 Blockchain Dependencies</h2>
    <ul>
        <li><strong>Ethereum Blockchain</strong> – Used for secure and transparent voting</li>
        <li><strong>Solidity</strong> – Smart contract programming language</li>
        <li><strong>Web3.js</strong> – JavaScript library for blockchain interaction</li>
        <li><strong>Truffle</strong> – Development framework for Ethereum smart contracts</li>
        <li><strong>Ganache</strong> – Local Ethereum blockchain for testing</li>
    </ul>
      <div class="container">
   <h2>🖥️ System Requirements</h2>
    <ul>
        <li><strong>OS:</strong> Windows, macOS, or Linux</li>
        <li><strong>RAM:</strong> Minimum 4GB (8GB recommended)</li>
        <li><strong>Storage:</strong> At least 10GB free space</li>
    </ul>
     <div class="container">
 <h2> 📸 Screenshots</h2>
<u1>
    
### 🔑 Login Page
![login png](https://github.com/user-attachments/assets/d2dbef93-229f-49ea-9ae0-52394a8261f1)

### 🏛 Admin Panel
![admin png](https://github.com/user-attachments/assets/f02934ae-c04b-4ee3-badc-fb08512e8e13)


### 🗳 Voting Page
![voting png](https://github.com/user-attachments/assets/3176856c-b3c7-47c1-ba36-b69bab26a1a7)


### 📊 Results Page
![results png](https://github.com/user-attachments/assets/f2cbfc2f-c0df-4a2f-a444-e6bc5e17585c)   

</u1>
       
<h2>📦 Installation</h2>
    <ol>
        <li>Open a terminal.</li>
        <li>Clone the repository by using the command:
            <pre><code>git clone https://github.com/ayujais45/Blockchain-based-voting-system.git</code></pre>
        </li>
        <li>Download and install <a href="https://trufflesuite.com/ganache/">Ganache</a>.</li>
        <li>Create a workspace named <code>development</code> in Truffle projects and add <code>truffle-config.js</code>.</li>
        <li>Download <a href="https://metamask.io/">MetaMask</a> extension for the browser.</li>
        <li>Create a wallet and import accounts from Ganache.</li>
        <li>Add a network to MetaMask (Network Name - Localhost 7575, RPC URI - <a href="http://localhost:7545">http://localhost:7545</a>, Chain ID - 1337, Currency Symbol - ETH).</li>
        <li>Open MySQL and create a database named <code>voter_db</code> (Do not use XAMPP).</li>
        <li>In the database, create a table named <code>voters</code> using the following SQL command:
            <pre><code>CREATE TABLE voters (
    voter_id VARCHAR(36) PRIMARY KEY NOT NULL,
    role ENUM('admin', 'user') NOT NULL,
    password VARCHAR(255) NOT NULL
);</code></pre>
        </li>
        <l1>
        </l1>
    </ol>
     <h2>📊 Voters Table</h2>
    <table>
        <tr>
            <th>voter_id</th>
            <th>role</th>
            <th>password</th>
        </tr>
        <tr>
            <td>------------------------------</td>
            <td>------------------------------</td>
            <td>------------------------------</td>
        </tr>
    </table>
    <h2>🛠️ Final Setup</h2>
    <ul>
    <ol>
        <li>Install Truffle globally:
            <pre><code>npm install -g truffle</code></pre>
        </li>
        <li>Install project dependencies:
            <pre><code>npm install</code></pre>
        </li>
        <li>Install Python dependencies:
            <pre><code>pip install fastapi mysql-connector-python pydantic python-dotenv uvicorn</code></pre>
        </li>
        <li>Install the number library:
            <pre><code>pip install number</code></pre>
      </li>
    <ol>
    </ul>
    <div class="container">
    <h2>Usage</h2>

<h3>1. Start the Blockchain Network</h3>
<ol>
    <li>Open <strong>Ganache</strong> and start a new workspace.</li>
    <li>Run the local Ethereum blockchain.</li>
</ol>

<h3>2. Deploy the Smart Contracts</h3>
<ol>
    <li>Navigate to the project directory in the terminal.</li>
    <li>Compile the smart contracts using:
        <pre><code>truffle compile</code></pre>
    </li>
    <li>Deploy the smart contracts using:
        <pre><code>truffle migrate --network development</code></pre>
    </li>
</ol>

<h3>3. Run the Backend Server</h3>
<ol>
    <li>Start the FastAPI backend:
        <pre><code>uvicorn main:app --reload</code></pre>
    </li>
    <li>Verify the API is running by visiting:
        <pre><code>http://127.0.0.1:8000/docs</code></pre>
    </li>
</ol>

<h3>4. Run the Frontend</h3>
<ol>
    <li>Navigate to the frontend directory.</li>
    <li>Start the development server:
        <pre><code>npm start</code></pre>
    </li>
    <li>Access the application in the browser:
        <pre><code>http://localhost:3000</code></pre>
    </li>
</ol>

<h3>5. Cast a Vote</h3>
<ol>
    <li>Log in to the platform using your credentials.</li>
    <li>Select the election you want to participate in.</li>
    <li>Click on your preferred candidate and confirm your vote.</li>
    <li>Your vote is securely recorded on the blockchain.</li>
</ol>

<h3>6. View Results</h3>
<ol>
    <li>After the voting period ends, go to the results section.</li>
    <li>The system will display real-time vote counts.</li>
    <li>The results are immutable and verifiable through the blockchain.</li>
</ol>
 <div class="container">
<h2>Code Structure</h2>

<p>The project is organized into different directories for better maintainability and scalability:</p>

<pre><code>
📦 Blockchain-Based-Voting-System
├── 📂 backend
│   ├── main.py                 # FastAPI backend
│   ├── database.py              # MySQL connection and models
│   ├── auth.py                  # Authentication and user management
│   ├── routes.py                # API endpoints
│   ├── config.py                # Environment variables and settings
│   ├── requirements.txt         # Python dependencies
│
├── 📂 blockchain
│   ├── contracts/
│   │   ├── Voting.sol           # Smart contract for voting
│   ├── migrations/
│   ├── truffle-config.js        # Truffle configuration
│
├── 📂 frontend
│   ├── public/
│   ├── src/
│   │   ├── components/          # React UI components
│   │   ├── pages/               # Main application pages
│   │   ├── App.js               # Main application entry point
│   │   ├── index.js             # Renders React application
│   ├── package.json             # Frontend dependencies
│
├── 📜 .env                      # Environment variables
├── 📜 README.md                 # Project documentation
├── 📜 package.json              # Node.js dependencies
</code></pre>

<p>This structure separates concerns between the <strong>backend</strong>, <strong>blockchain</strong>, and <strong>frontend</strong>, making the system modular and easy to manage.</p>
 <div class="container">
   <h2>📜 License</h2>
    <p>This project is open-source and free to use.</p> 
     <div class="container">
   <h2>📞 Contact</h2>
         <p>📧 Email: aayushijaiswal88@gmail.com</p>
         <p>🔗 GitHub: ayujais45</p>
<p><b>Thank you for exploring the Blockchain-Based Voting System! 🚀 This project is designed to bring transparency and security to the voting process. If you have any feedback, suggestions, or contributions, feel free to collaborate. Let's build a future of trust in digital elections! 🗳️</p></b>

    
   
