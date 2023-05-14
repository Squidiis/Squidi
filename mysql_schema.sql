

CREATE DATABASE IF NOT EXISTS `DiscordBot` ;

USE DiscordBot;


------------  Tables for the Level System -------------

DROP TABLE IF EXISTS `LevelSystemStats`;

CREATE TABLE `LevelSystemStats` (
    guildId BIGINT UNSIGNED NOT NULL, 
    userId BIGINT UNSIGNED NOT NULL,
    userLevel BIGINT UNSIGNED NOT NULL,
    userXp BIGINT UNSIGNED NOT NULL,
    userName VARCHAR(255) NOT NULL,
	voiceTime TIMESTAMP(6) NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `LevelSystemBlacklist`;

CREATE TABLE LevelSystemBlacklist (
    guildId BIGINT UNSIGNED NOT NULL,
    guildName VARCHAR(255) NOT NULL,
    channelId BIGINT UNSIGNED NULL,
    categoryId BIGINT UNSIGNED NULL,
    roleId BIGINT UNSIGNED NULL,
    userId BIGINT UNSIGNED NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `LevelSystemRoles`;

CREATE TABLE LevelSystemRoles (
    guildId BIGINT UNSIGNED NOT NULL,
    roleId BIGINT UNSIGNED NOT NULL,
    roleLevel INT UNSIGNED NOT NULL,
    guildName VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- The table contains data for processe that can be used to overwrite the level roles.
DROP TABLE IF EXISTS `LevelSystemRolesProcess`;

CREATE TABLE LevelSystemRolesProcess (
    guildId BIGINT UNSIGNED NOT NULL,
    roleId BIGINT UNSIGNED NOT NULL,
    roleLevel INT UNSIGNED NOT NULL,
    status VARCHAR(20) NOT NULL,
    messageId BIGINT UNSIGNED NOT NULL,
    guildName VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


------------- Table for the Marry system --------------

DROP TABLE IF EXISTS `MarryStats`;

CREATE TABLE MarryStats (
    guildId BIGINT UNSIGNED NOT NULL,
    userOneId BIGINT UNSIGNED NOT NULL,
    userOneName VARCHAR(255) NOT NULL,
    userTwoId BIGINT UNSIGNED NOT NULL,
    userTwoName VARCHAR(255) NOT NULL,
    WeddingDate DATE NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


------------- Table for the Bot settigs -----------------

DROP TABLE IF EXISTS `BotSettings`;

CREATE TABLE BotSettings (
    guildId BIGINT UNSIGNED NOT NULL,
    prefix VARCHAR(20) DEFAULT '?',
    levelStatus VARCHAR(50) DEFAULT 'on',
    levelUpChannel BIGINT UNSIGNED NULL,
    econemyStatus VARCHAR(50) DEFAULT 'on'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-------------- Table for the Autoreaction ---------------

DROP TABLE IF EXISTS `AutoReactionSetup`;

CREATE TABLE AutoReactionSetup (
    guildId BIGINT UNSIGNED NOT NULL, 
    channelId BIGINT UNSIGNED NOT NULL,
    categoryId BIGINT UNSIGNED NOT NULL,
    emojiOne VARCHAR(255) NULL,
    emojiTwo VARCHAR(255) NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `AutoReactionSettings`;

CREATE TABLE AutoReactionSettings (
    guildId BIGINT UNSIGNED NOT NULL,
    teServerReaction INT NULL,
    reactionParameter VARCHAR(255) NULL,
    mainReactionEmoji VARCHAR(255) NOT NULL,
    reactionKeyWords VARCHAR(4000) NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--------------- Table for Econemy System ------------

DROP TABLE IF EXISTS `EconomySystemStats`;

CREATE TABLE EconomySystemStats (
    guildId BIGINT UNSIGNED NOT NULL,
    userId BIGINT UNSIGNED NOT NULL,
    moneyCount BIGINT UNSIGNED DEFAULT 0,
    userName VARCHAR(255) NOT NULL,
    voiceTime TIMESTAMP(6) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `EconomySystemBlacklist`;

CREATE TABLE EconomySystemBlacklist (
    guildId BIGINT UNSIGNED NOT NULL,
    guildName VARCHAR(255) NOT NULL,
    channelId BIGINT UNSIGNED NULL,
    categoryId BIGINT UNSIGNED NULL,
    roleId BIGINT UNSIGNED NULL,
    userId BIGINT UNSIGNED NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `EconomySystemShopRoles`;

CREATE TABLE EconomySystemShopRolles (
    guildId BIGINT UNSIGNED NOT NULL,
    guildName VARCHAR(255) NOT NULL,
    rolesId BIGINT UNSIGNED NOT NULL,
    rolesPrice INT UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;




