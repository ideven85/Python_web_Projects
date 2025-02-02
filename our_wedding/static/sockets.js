const { Server } = require("socket.io");
const { createServer } = require('node:http');
const server = createServer()
const io = new Server()