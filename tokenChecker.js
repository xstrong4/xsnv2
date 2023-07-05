const Discord = require('discord.js');
const fs = require('fs');

// Define the intents that you want the bot to have
const intents = new Discord.Intents();
intents.add(Discord.Intents.FLAGS.GUILDS);
intents.add(Discord.Intents.FLAGS.DIRECT_MESSAGES);

async function checkToken(token) {
  try {
    const client = new Discord.Client({ intents });
    await client.login(token);
    const servers = client.guilds.cache.size;
    const members = client.guilds.cache.reduce((a, g) => a + g.memberCount, 0);
    return { valid: true, servers, members };
  } catch (error) {
    return { valid: false };
  }
}

fs.readFile('src/json/tokens.txt', 'utf8', async (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  const tokens = data.trim().split(' ');

  for (const token of tokens) {
    const { valid, servers, members } = await checkToken(token.trim());
    if (valid) {
      console.log('\x1b[32m%s\x1b[0m', `${token.trim()} - Servers: ${servers}\n`);
    } else {
      console.log('\x1b[31m%s\x1b[0m', `${token.trim()} - Invalid token\n`);
    }
  }
});
