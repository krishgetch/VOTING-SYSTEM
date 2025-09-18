const HDWalletProvider = require('@truffle/hdwallet-provider');
require('dotenv').config(); // Load environment variables

module.exports = {
  networks: {
    development: {
      host: "127.0.0.1", // Localhost
      port: 7545, // Default Ganache port
      network_id: "*", // Match any network
    },
    ropsten: {
      provider: () => new HDWalletProvider(
        process.env.MNEMONIC, // Your MetaMask seed phrase stored in .env file
        `https://ropsten.infura.io/v3/${process.env.INFURA_PROJECT_ID}` // Infura API Key
      ),
      network_id: 3, // Ropsten Testnet
      gas: 5500000, 
      confirmations: 2,
      timeoutBlocks: 200,
      skipDryRun: true,
    },
  },
  
  compilers: {
    solc: {
      version: "0.8.0", // Solidity version
      settings: {
        optimizer: {
          enabled: true,
          runs: 200,
        },
      },
    },
  },
};
