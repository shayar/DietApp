const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const userRoutes = require('./routes/user');
const logger = require('./utils/logger');

// Swagger setup
const swaggerJsDoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');
const swaggerOptions = {
  swaggerDefinition: {
    openapi: '3.0.0',
    info: {
      title: 'Node API',
      version: '1.0.0',
      description: 'User management API',
    },
  },
  apis: ['./src/routes/*.js'],
};
const swaggerDocs = swaggerJsDoc(swaggerOptions);

const app = express();
app.use(helmet());
app.use(cors());
app.use(express.json());

// Swagger docs route
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocs));

// API routes
app.use('/api/users', userRoutes);

// Error handler
app.use((err, req, res, next) => {
  logger.error(err.stack || err);
  res.status(err.status || 500).json({ error: err.message });
});

module.exports = app;
