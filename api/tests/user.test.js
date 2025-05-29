const request = require('supertest');
const app = require('../src/app');

describe('User API', () => {
  it('registers and logs in a user', async () => {
    const res = await request(app)
      .post('/api/users/register')
      .send({ email: 'test@example.com', password: 'pass' });
    expect(res.statusCode).toBe(201);

    const login = await request(app)
      .post('/api/users/login')
      .send({ email: 'test@example.com', password: 'pass' });
    expect(login.statusCode).toBe(200);
    expect(login.body.token).toBeTruthy();
  });
});
