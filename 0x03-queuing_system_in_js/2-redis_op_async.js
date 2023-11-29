#!/usr/bin/yarn dev
import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});

/**
 * Set store key value pair in memory
 * @param {*} schoolName 
 * @param {*} value 
 */
const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

/**
 * print value of a stored key
 * @param {*} schoolName 
 */
const displaySchoolValue = async (schoolName) => {
  console.log(await promisify(client.GET).bind(client)(schoolName));
};

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}
